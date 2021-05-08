"""
    __main__.py
"""

import sys

from PyQt6.QtWidgets import QApplication
from Quizzo.controller import Control
from Quizzo.questions import Question
from Quizzo.view import View


def main():
    """Start of the program"""
    
    # Create QApplication object
    app = QApplication([])
    
    # Create a View object
    viewObj = View()
    viewObj.show()

    # Create a Question object
    questionObj = Question("question-data.json")

    # Create Controller
    controller = Control(view=viewObj, question=questionObj)

    # Execute app
    sys.exit(app.exec())
    



if __name__ == "__main__":
    main()
