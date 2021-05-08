"""
    view.py

    Setup the GUI with PyQt6
"""

from os.path import join
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor, QIcon
from PyQt6.QtWidgets import (
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QGridLayout,
    QWidget,
)


class View(QMainWindow):
    """Main class"""

    def __init__(self):
        super().__init__()

        # Create a central widget
        self._centralWidget = QStackedWidget()
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setCursor(Qt.CursorShape.ClosedHandCursor)

        # Customize window
        stylesheet = join("Styles", "main_window.css")
        icon = join("Icon", "icon.jpg")

        with open(stylesheet) as style:
            self.setStyleSheet(style.read())
        
        self.setWindowTitle("Quizzo")
        self.setFixedSize(1000, 500)
        self.setWindowIcon(QIcon(icon))

        # Crearte pages
        self._home()
        self._quiz()
    
    def _home(self):
        """Create Homepage"""
        stylesheet = join("Styles", "homepage.css")

        self.homepage = QWidget()
        self.homeLayout = QVBoxLayout()
        self.homepage.setLayout(self.homeLayout)

        logo = QLabel("Welcome To Quizzo")
        logo.setAlignment(Qt.Alignment.AlignCenter)
        self.homeLayout.addWidget(logo)

        self.buttons = {
            "Play": 0,
        }

        for btnText, pos in self.buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self.homeLayout.addWidget(self.buttons[btnText], pos)
        
        with open(stylesheet) as style:
            self.homepage.setStyleSheet(style.read())
        
        self._centralWidget.addWidget(self.homepage)

    def _quiz(self):
        """Create Quiz page"""
        stylesheet = join("Styles", "quizpage.css")

        self.quizpage = QWidget()
        self.quizLayout = QVBoxLayout()
        self.quizpage.setLayout(self.quizLayout)

        self.score = QLineEdit("0")
        self.score.setAlignment(Qt.Alignment.AlignCenter)
        self.score.setReadOnly(True)
        self.quizLayout.addWidget(self.score)

        self.question_detail = QLabel("Question #0")
        self.question_detail.setAlignment(Qt.Alignment.AlignCenter)
        self.quizLayout.addWidget(self.question_detail)

        optionsWidget = QWidget()
        optionLayout = QGridLayout()
        optionsWidget.setLayout(optionLayout)

        self.options = {
            'A': (0, 0),
            'B': (0, 1),
            'C': (1, 0),
            'D': (1, 1)
        }

        for btnText, pos in self.options.items():
            self.options[btnText] = QPushButton(f"Option {btnText}")

            btn = self.options[btnText]
            btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

            optionLayout.addWidget(btn, *pos)
        
        self.quizLayout.addWidget(optionsWidget)

        with open(stylesheet) as style:
            self.quizpage.setStyleSheet(style.read())

        self._centralWidget.addWidget(self.quizpage)
