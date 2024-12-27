import pygame
from constants import screen, WHITE, clock, FPS
from game_data import GameData
from ui_renderer import UIRenderer

class Game(GameData):
    def __init__(self):
        super().__init__()
        self.username = ""
        self.total_score = 0
        self.is_solved = False
        self.is_game_over = False
        self.game_state = "USERNAME"  # States: USERNAME, PLAYING, GAMEOVER
        
        # TODO: Load UI assets
        # self.button_bg = pygame.image.load("assets/button.png")
        # self.input_box_bg = pygame.image.load("assets/input_box.png")
        # self.background = pygame.image.load("assets/background.png")

    def handle_username_input(self, event):
        if event.key == pygame.K_RETURN and self.username:
            self.game_state = "PLAYING"
            self.initialize_questions()
            self.generate_question()
            self.progress = ["-"] * len(self.current_question[1])
            self.get_letters(self.current_question[1])
        elif event.key == pygame.K_BACKSPACE:
            self.username = self.username[:-1]
        else:
            if len(self.username) < 10:
                self.username += event.unicode

    def handle_game_input(self, event):
        if event.unicode.isalpha():
            self.check_input(event.unicode.lower())
            if "-" not in self.progress:
                self.is_solved = True
                self.total_score += int(self.current_question[2])
                self.generate_question()
                self.progress = ["-"] * len(self.current_question[1])
                self.get_letters(self.current_question[1])
                self.is_solved = False
            if self.chances == 0:
                self.game_state = "GAMEOVER"
                self.read_leaderboard()
                self.update_leaderboard(self.username, self.total_score)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if self.game_state == "USERNAME":
                        self.handle_username_input(event)
                    elif self.game_state == "PLAYING":
                        self.handle_game_input(event)
                    elif self.game_state == "GAMEOVER" and event.key == pygame.K_RETURN:
                        running = False

            screen.fill(WHITE)

            if self.game_state == "USERNAME":
                UIRenderer.draw_username_screen(self.username)
            elif self.game_state == "PLAYING":
                UIRenderer.draw_game_screen(
                    self.current_question,
                    self.chances,
                    self.progress,
                    self.guessed_letters,
                    self.total_score
                )
                self.draw_hangman(self.chances)
            elif self.game_state == "GAMEOVER":
                UIRenderer.draw_game_over_screen(self.total_score, self.display_leaderboard())

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()