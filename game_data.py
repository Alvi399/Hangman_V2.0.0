import random
from abstract_classes import AbstractPlayer, IMekanisme

class GameData(AbstractPlayer, IMekanisme):
    def __init__(self):
        super().__init__()
        self.questions = []
        self.current_question = ["", "", ""]
        self.guessed_letters = [""] * 15
        self.progress = []
        self.chances = 5
        # TODO: Load hangman images
        # self.hangman_images = [
        #     pygame.image.load("assets/hangman0.png"),  # Empty gallows
        #     pygame.image.load("assets/hangman1.png"),  # Head
        #     pygame.image.load("assets/hangman2.png"),  # Body
        #     pygame.image.load("assets/hangman3.png"),  # One arm
        #     pygame.image.load("assets/hangman4.png"),  # Two arms
        #     pygame.image.load("assets/hangman5.png"),  # One leg
        #     pygame.image.load("assets/hangman6.png")   # Complete hangman
        # ]

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

    def get_letters(self, word):
        self.guessed_letters = [""] * 15
        unique_letters = list(set(word))
        random.shuffle(unique_letters)

        for i, letter in enumerate(unique_letters):
            self.guessed_letters[i] = letter

        while "" in self.guessed_letters:
            self.guessed_letters[self.guessed_letters.index("")] = chr(
                random.randint(97, 122)
            )

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
        # screen.blit(self.hangman_images[5 - attempts_left], (50, 50))
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