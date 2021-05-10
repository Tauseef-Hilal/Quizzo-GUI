"""
    __main__.py
"""

import sys

from PyQt6.QtWidgets import QApplication
from Quizzo.controller import Control
from Quizzo.view import View


def main():
    """Start of the program"""

    # Create QApplication object
    app = QApplication([])

    # Initiate UI
    viewObj = View()
    viewObj.show()

    # Initiate Controller
    Control(view=viewObj)

    # Execute app
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
