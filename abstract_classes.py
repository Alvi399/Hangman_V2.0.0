from abc import ABC, abstractmethod

class AbstractPlayer(ABC):
    def __init__(self):
        self.scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        self.topPlayer = [["", "0"]] * 10

    @abstractmethod
    def read_leaderboard(self):
        pass

    @abstractmethod
    def update_leaderboard(self, name, score):
        pass

    @abstractmethod
    def display_leaderboard(self):
        pass

class IMekanisme(ABC):
    @abstractmethod
    def draw_hangman(self, attempts_left):
        pass

    @abstractmethod
    def initialize_questions(self):
        pass

    @abstractmethod
    def generate_question(self):
        pass

    @abstractmethod
    def get_letters(self, word):
        pass

    @abstractmethod
    def check_input(self, input_letter):
        pass