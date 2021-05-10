"""
    questions.py

    [1] Read questions form json file.
    [2] Set up a mechanism for sharing questions one by one with controller.py
"""

import json

from random import shuffle
from os.path import join


class Question:
    """Read question data"""

    def __init__(self):
        self.filename = join("Data", "question-data.json")
        self.question_list = []

        # Read the json data
        with open(self.filename) as file:
            self.question_list = json.load(file)

        # Shuffle question list
        shuffle(self.question_list)

    def _getQuestion(self):
        """Send a question dict to the controller"""
        return self.question_list.pop(0)

    def __repr__(self):
        return f"Question() => Keeps the list of all questions"
