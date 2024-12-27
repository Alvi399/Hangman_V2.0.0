import pygame
import random
import os
from abc import ABC, abstractmethod

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)

# Initialize window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hangman Game")
clock = pygame.time.Clock()

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

class Data(AbstractPlayer, IMekanisme):
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

    def draw_hangman(self, attempts_left):
        # TODO: Draw hangman image based on attempts_left
        # screen.blit(self.hangman_images[5 - attempts_left], (50, 50))
        pass

    # [Other methods remain the same as in original code]

class GameGUI(Data):
    def __init__(self):
        super().__init__()
        self.username = ""
        self.total_score = 0
        self.is_solved = False
        self.is_game_over = False
        self.game_state = "USERNAME"  # States: USERNAME, PLAYING, GAMEOVER
        
        # TODO: Load button images and other UI elements
        # self.button_bg = pygame.image.load("assets/button.png")
        # self.input_box_bg = pygame.image.load("assets/input_box.png")
        # self.background = pygame.image.load("assets/background.png")

    def draw_text(self, text, size, x, y, color=BLACK):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    def draw_username_screen(self):
        # TODO: Draw background image
        # screen.blit(self.background, (0, 0))
        
        self.draw_text("HANGMAN", 64, WINDOW_WIDTH//2, 100)
        self.draw_text("Enter Username:", 32, WINDOW_WIDTH//2, 250)
        # Draw input box and username

    def draw_game_screen(self):
        # TODO: Draw game background
        # screen.blit(self.background, (0, 0))
        
        # Draw current state
        self.draw_text(f"Topic: {self.current_question[0]}", 32, WINDOW_WIDTH//2, 50)
        self.draw_text(f"Score: {self.current_question[2]}", 32, 700, 30)
        self.draw_text(f"Chances: {self.chances}", 32, 700, 60)
        
        # Draw word progress
        progress_text = " ".join(self.progress)
        self.draw_text(progress_text, 48, WINDOW_WIDTH//2, 400)
        
        # Draw available letters
        letters_text = " ".join(self.guessed_letters)
        self.draw_text(letters_text, 32, WINDOW_WIDTH//2, 500)
        
        # Draw hangman
        self.draw_hangman(self.chances)

    def draw_game_over_screen(self):
        # TODO: Draw game over background
        # screen.blit(self.game_over_bg, (0, 0))
        
        self.draw_text("Game Over!", 64, WINDOW_WIDTH//2, 200)
        self.draw_text(f"Final Score: {self.total_score}", 48, WINDOW_WIDTH//2, 300)
        # Draw leaderboard

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if self.game_state == "USERNAME":
                        # Handle username input
                        pass
                    elif self.game_state == "PLAYING":
                        # Handle letter input
                        pass

            # Clear screen
            screen.fill(WHITE)

            # Draw current game state
            if self.game_state == "USERNAME":
                self.draw_username_screen()
            elif self.game_state == "PLAYING":
                self.draw_game_screen()
            elif self.game_state == "GAMEOVER":
                self.draw_game_over_screen()

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()

if __name__ == "__main__":
    game = GameGUI()
    game.run()