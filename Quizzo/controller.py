"""
    controller.py
"""

from os.path import join
from functools import partial
from playsound import playsound


class Control():
    """Controller class for the game"""

    def __init__(self, view, question):
        self._view = view
        self._question = question
        self.currentQuestion = {}
        self.answer = ""

        self._controlSignals()
    
    def _newQuestion(self):
        """Grab a question from the question list"""
        
        self.currentQuestion = self._question._getQuestion()

        self.answer = self.currentQuestion['answer']
        questionDetail = self.currentQuestion['question']
        questionOptions = self.currentQuestion['options']

        if len(questionDetail) > 50:
            self._view.question_detail.setFixedSize(900, 250)
        else:
            self._view.question_detail.setFixedSize(900, 200)
        
        self._view.question_detail.setText(questionDetail)
        for i, option in enumerate(self._view.options.values()):
            option.setText(questionOptions[i])
        
        self._view._centralWidget.setCurrentWidget(self._view.quizpage)
    
    def _checkAns(self, option):
        """Check user guess"""
        btn = self._view.options[option]

        if btn.text() == self.answer:
            playsound(join("Sounds", "correct.mp3"), block=False)
            self._view.score.setText(str(int(self._view.score.text())+5))
            self._newQuestion()
        else:
            playsound(join("Sounds", "buzzer.mp3"), block=False)
            self._view.score.setText("0")
            self._view._centralWidget.setCurrentWidget(self._view.homepage)
    
    def _controlSignals(self):
        """Control signals"""
        
        # Homepage
        button = self._view.buttons
        button['Play'].clicked.connect(self._newQuestion)

        # Quizpage
        option = self._view.options
        option['A'].clicked.connect(partial(self._checkAns, 'A'))
        option['B'].clicked.connect(partial(self._checkAns, 'B'))
        option['C'].clicked.connect(partial(self._checkAns, 'C'))
        option['D'].clicked.connect(partial(self._checkAns, 'D'))
