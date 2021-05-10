"""
    controller.py
"""

from os.path import join
from functools import partial
from playsound import playsound
from Quizzo.questions import Question


class Control:
    """Controller class for the game"""

    def __init__(self, view):
        self._view = view
        self._questionObj = Question()
        self.currentQuestion = {}
        self.answer = ""
        self.questionFamiliarity = 0
        self.notified = False
        self.currentScore = int(self._view.score.text())
        self.highScore = 0

        try:
            with open(join("Data", "highscore.txt")) as hScore:
                self.highScore = int(hScore.read())
        except FileNotFoundError:
            with open(join("Data", "highscore.txt"), mode="w") as hScore:
                hScore.write(str(self.highScore))

        self._controlSignals()

    def _newQuestion(self):
        """Grab a question from the question list"""

        try:
            self.currentQuestion = self._questionObj._getQuestion()

        except IndexError:
            with open(join("Data", "highscore.txt"), mode="w") as score:
                score.write(str(self.currentScore))

            playsound(join("Sounds", "after-highscore.mp3"), block=False)
            return self._mainMenu()

        self.questionFamiliarity = self.currentQuestion["id"]
        self.answer = self.currentQuestion["answer"]
        questionDetail = self.currentQuestion["question"]
        questionOptions = self.currentQuestion["options"]

        if len(questionDetail) > 65:
            questionDetail = questionDetail[:65] + "-\n-" + questionDetail[65:]

        self._view.question_detail.setText(questionDetail)
        for i, option in enumerate(self._view.options.values()):
            option.setText(questionOptions[i])

        self._view._centralWidget.setCurrentWidget(self._view.quizpage)

    def _checkAns(self, option):
        """Check user guess"""
        btn = self._view.options[option]

        if btn.text() == self.answer:
            self.currentScore += 5
            self._view.score.setText(str(self.currentScore))
            playsound(join("Sounds", "correct.mp3"), block=False)

            if self.currentScore > self.highScore and not self.notified:
                playsound(join("Sounds", "ingame-highscore.mp3"), block=False)
                self.notified = True

            self._newQuestion()
        else:
            playsound(join("Sounds", "wrong.mp3"), block=False)

            self._view._score.setText(str(self.currentScore))
            if self.currentScore > self.highScore:
                playsound(join("Sounds", "after-highscore.mp3"), block=False)
                self._view._score.setText(f"*{self.currentScore}*")
                self.highScore = self.currentScore
                self.notified = False

                with open(join("Data", "highscore.txt"), mode="w") as score:
                    score.write(str(self.highScore))

            self._view._centralWidget.setCurrentWidget(self._view.wrongpage)

    def _restartGame(self):
        """Restart game"""
        self._questionObj = Question()
        self.currentScore = 0
        self._view.score.setText("0")
        self._view._centralWidget.setCurrentWidget(self._view.quizpage)
        self._newQuestion()

    def _mainMenu(self):
        """Head to main menu"""
        self._questionObj = Question()
        self.currentScore = 0
        self._view.score.setText("0")
        self._view._centralWidget.setCurrentWidget(self._view.homepage)

    def _showCredits(self):
        """Show Credits page"""
        self._view._centralWidget.setCurrentWidget(self._view.creditspage)

    def _controlSignals(self):
        """Control signals"""

        # Homepage
        button = self._view.buttons
        button["Play"].clicked.connect(self._newQuestion)
        button["Credits"].clicked.connect(self._showCredits)

        # Quizpage
        option = self._view.options
        option["A"].clicked.connect(partial(self._checkAns, "A"))
        option["B"].clicked.connect(partial(self._checkAns, "B"))
        option["C"].clicked.connect(partial(self._checkAns, "C"))
        option["D"].clicked.connect(partial(self._checkAns, "D"))

        # Wrongpage
        choice = self._view.choices
        choice["Try Again"].clicked.connect(self._restartGame)
        choice["Return To Main Menu"].clicked.connect(self._mainMenu)

        # Creditspage
        btn = self._view.menuBtn
        btn.clicked.connect(self._mainMenu)
