import random
import os
from abc import ABC, abstractmethod


# Abstract base class untuk player leaderboard
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


# Interface untuk mekanisme hangman
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


# Kelas utama yang mengimplementasikan AbstractPlayer dan IMekanisme
class Data(AbstractPlayer, IMekanisme):
    def __init__(self):
        super().__init__()
        self.questions = []
        self.current_question = ["", "", ""]
        self.guessed_letters = [""] * 15
        self.progress = []
        self.chances = 5

    def draw_hangman(self, attempts_left):
        stages = [
            "   ___\n  |     |\n  |\n  |\n  |\n",                          # Awal (kosong)
            "   ___\n  |     |\n  |     O\n  |\n  |\n",                    # Kepala
            "   ___\n  |     |\n  |     O\n  |     |\n  |\n",               # Badan
            "   ___\n  |     |\n  |     O\n  |    /|\n  |\n",               # Tangan
            "   ___\n  |     |\n  |     O\n  |    /|\\\n  |\n",             # Tangan lengkap
            "   ___\n  |     |\n  |     O\n  |    /|\\\n  |    /\n",        # Satu kaki
            "   ___\n  |     |\n  |     O\n  |    /|\\\n  |    / \\\n",     # Gantung lengkap
        ]
        # Indeks stage dihitung dari jumlah kesempatan tersisa
        print(stages[5 - attempts_left])


    def initialize_questions(self):
        file_path = r"./bankSoal.txt"
        try:
            with open(file_path, "r") as file:
                lines = [line.strip() for line in file if line.strip()]  # Hilangkan baris kosong

            self.questions = []
            for i in range(0, len(lines), 11):  # Iterasi setiap 11 baris
                topic = lines[i]
                words = lines[i + 1:i + 11]  # Ambil 10 kata berikutnya
                self.questions.append([topic] + words)

            # print("Questions loaded:", self.questions)  # Debugging
        except FileNotFoundError:
            print("File soal tidak ditemukan.")
        except IndexError:
            print("Format file soal tidak sesuai. Pastikan setiap topik memiliki 10 kata.")

    def generate_question(self):
        if not self.questions:  # Pastikan ada data
            print("Error: Tidak ada soal yang dimuat.")
            return

        row = random.randint(0, len(self.questions) - 1)
        col = random.randint(1, len(self.questions[row]) - 1)
        score_index = random.randint(0, 9)

        self.current_question = [
            self.questions[row][0],  # Topik
            self.questions[row][col],  # Kata
            str(self.scores[score_index]),  # Skor
        ]

        # print("Generated Question:", self.current_question)  # Debugging

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
            print(f"Huruf '{input_letter}' tidak ditemukan.")

    def read_leaderboard(self):
        file_path = r"./leaderBoard.txt"
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
        print("===========TOP PLAYER==========")
        print("|No|      Nama         |Skor  |")
        print("===============================")
        for i, (name, score) in enumerate(self.topPlayer):
            print(f"{i+1}. {name} {score}")


class Game(Data):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.total_score = 0
        self.is_solved = False
        self.is_game_over = False

    def play_game(self):
        self.initialize_questions()
        while not self.is_game_over:
            self.generate_question()
            self.progress = ["-"] * len(self.current_question[1])
            self.get_letters(self.current_question[1])

            while not self.is_solved and self.chances > 0:
                print(
                    f"Topik: {self.current_question[0]} | Skor: {self.current_question[2]} | Total Skor: {self.total_score} | Kesempatan: {self.chances}"
                )
                self.draw_hangman(self.chances)

                print("Progres: ", " ".join(self.progress))
                print("Huruf Tersedia: ", " ".join(self.guessed_letters))
                input_letter = input("Masukkan tebakan huruf: ")

                self.check_input(input_letter)

                if "-" not in self.progress:
                    self.is_solved = True
                    self.total_score += int(self.current_question[2])
                    print("Selamat! Kamu berhasil menjawab semua kata.")

                if self.chances == 0 and not self.is_solved:
                    self.is_game_over = True
                    print(f"Kamu gagal menjawab. Jawaban adalah: {self.current_question[1]}")

            if self.is_solved:
                self.is_solved = False

    def end_game(self):
        os.system("cls" if os.name == "nt" else "clear")
        self.read_leaderboard()
        self.update_leaderboard(self.username, self.total_score)
        self.display_leaderboard()
        print(f"Skor kamu: {self.total_score} dengan username: {self.username}")


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    print("---------------------------------------------")
    print("==================HANGMAN====================")
    print("---------------------------------------------")
    username = input("Masukkan username anda: ")
    os.system("cls" if os.name == "nt" else "clear")
    game = Game(username)
    game.play_game()
    game.end_game()
