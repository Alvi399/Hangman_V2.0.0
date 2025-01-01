import random
import pygame
from abstract_classes import AbstractPlayer, IMekanisme
from constants import screen
class GameData(AbstractPlayer, IMekanisme):
    def __init__(self):
        super().__init__()
        self.questions = []
        self.current_question = ["", "", ""]
        self.guessed_letters = [""] * 15
        self.progress = []
        self.chances = 5
        # TODO: Load hangman images
        self.hangman_images = [
            pygame.image.load("./Asset/phase1.png"),  # Empty gallows
            pygame.image.load("./Asset/phase2.png"),  # Head
            pygame.image.load("./Asset/phase3.png"),  # Body
            pygame.image.load("./Asset/phase4.png"),  # One arm
            pygame.image.load("./Asset/phase5.png"),  # Two arms
            pygame.image.load("./Asset/phase6.png"),  # One leg
            pygame.image.load("./Asset/phase7.png")   # Complete hangman
        ]

        #transform icon size to 50x50
        # self.hangman_images = [pygame.transform.scale(image, (50, 50)) for image in self.hangman_images]

    def initialize_questions(self):
        file_path = r"./Data/bankSoal.txt"
        try:
            with open(file_path, "r") as file:
                lines = [line.strip() for line in file if line.strip()]
            
            self.questions = []
            for i in range(0, len(lines), 11):
                topic = lines[i]
                words = lines[i + 1:i + 11]
                self.questions.append([topic] + words)
        except FileNotFoundError:
            print("File soal tidak ditemukan.")
        except IndexError:
            print("Format file soal tidak sesuai.")

    def generate_question(self):
        if not self.questions:
            print("Error: Tidak ada soal yang dimuat.")
            return

        row = random.randint(0, len(self.questions) - 1)
        col = random.randint(1, len(self.questions[row]) - 1)
        score_index = random.randint(0, 9)

        self.current_question = [
            self.questions[row][0],
            self.questions[row][col],
            str(self.scores[score_index]),
        ]

    # Update get_letters method to include all alphabet letters
    def get_letters(self, word):
        alphabet = set("abcdefghijklmnopqrstuvwxyz")
        word_letters = set(word)
        unused_letters = alphabet - word_letters
        self.guessed_letters = list(word_letters) + list(unused_letters)
        self.guessed_letters.sort()

    def check_input(self, input_letter):
        found = False
        for i, letter in enumerate(self.current_question[1]):
            if letter == input_letter:
                self.progress[i] = input_letter
                found = True

        if input_letter in self.guessed_letters:
            self.guessed_letters[self.guessed_letters.index(input_letter)] = "-"

        if not found:
            self.chances -= 1

    def draw_hangman(self, attempts_left):
        # TODO: Draw hangman image based on attempts_left
        screen.blit(self.hangman_images[5 - attempts_left], (200, 150))
        pass

    def read_leaderboard(self):
        file_path = r"./Data/leaderBoard.txt"
        try:
            with open(file_path, "r") as file:
                for i, line in enumerate(file):
                    if i >= 10:
                        break
                    name, score = line.strip().split(":")
                    self.topPlayer[i] = [name, score]
        except FileNotFoundError:
            print("File leaderboard tidak ditemukan.")

    def update_leaderboard(self, username, score):
        self.topPlayer.append([username, str(score)])
        self.topPlayer.sort(key=lambda x: int(x[1]), reverse=True)
        self.topPlayer = self.topPlayer[:10]

    def display_leaderboard(self):
        return self.topPlayer
