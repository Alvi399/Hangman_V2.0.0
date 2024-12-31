import pygame
from constants import screen, WHITE, clock, FPS, WINDOW_WIDTH, WINDOW_HEIGHT
from game_data import GameData
from ui_renderer import UIRenderer
# from dashboard import HangmanDashboard
class Game(GameData):
    def __init__(self):
        super().__init__()
        self.username = ""
        self.total_score = 0
        self.coins = 0  # Add coin attribute
        self.is_solved = False
        self.is_game_over = False
        self.game_state = "DASHBOARD"  # States: USERNAME, PLAYING, GAMEOVER, DASHBOARD, PAUSE
        self.initial_chances = 5  # Store the initial number of chances
        
        # UI elements
        self.back_button_react = pygame.Rect((10, 10), (40, 40))
        self.play_button_rect = pygame.Rect((WINDOW_WIDTH//2 - 50, WINDOW_HEIGHT//2), (200, 100)) #tengah
        self.setting_icon_rect = pygame.Rect((WINDOW_WIDTH - 50, 10), (40, 40)) #pojok kanan atas
        self.trophy_icon_rect = pygame.Rect((10, WINDOW_HEIGHT - 50), (40, 40)) #pojok kiri bawah
        self.hint_button_rect = pygame.Rect((10, WINDOW_HEIGHT - 50), (80, 40))  # Hint button

        self.resume_button_rect = pygame.Rect((WINDOW_WIDTH//2 - 300, WINDOW_HEIGHT//2), (200, 100)) #kiri
        self.restart_button_rect = pygame.Rect((WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2), (200, 100)) #tengah
        self.home_button_rect = pygame.Rect((WINDOW_WIDTH//2 + 100, WINDOW_HEIGHT//2), (200, 100)) #kanan

        self.pause_button_rect = pygame.Rect((WINDOW_WIDTH - 50, WINDOW_HEIGHT - 50), (40, 40)) #pojok kiri atas
        self.home_button_gameover_rect = pygame.Rect((WINDOW_WIDTH - 50, WINDOW_HEIGHT - 50), (200, 100)) #tengah
        self.leaderboard_back_button_rect = pygame.Rect((WINDOW_WIDTH - 100, WINDOW_HEIGHT - 50), (80, 40))  # Back button for leaderboard
        self.exit_button_rect = pygame.Rect((WINDOW_WIDTH - 50, 10), (40, 40))  # Exit button

        # Load UI assets
        self.button_bg = pygame.image.load("./Asset/coba_button.png")
        self.background = pygame.image.load("./Asset/backgroud_game.jpg")
        self.back_button = pygame.image.load("./Asset/coba_button.png")
        self.play_button = pygame.image.load("./Asset/coba_button.png")
        self.setting_icon = pygame.image.load("./Asset/back_button.png")
        self.trophy_icon = pygame.image.load("./Asset/coba_button.png")
        self.resume_button = pygame.image.load("./Asset/coba_button.png")
        self.restart_button = pygame.image.load("./Asset/coba_button.png")
        self.home_button = pygame.image.load("./Asset/coba_button.png")
        self.pause_button = pygame.image.load("./Asset/coba_button.png")
        self.home_button_gameover = pygame.image.load("./Asset/coba_button.png")
        self.hint_button = pygame.image.load("./Asset/coba_button.png")  # Load hint button image

    def dashboard(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.play_button_rect.collidepoint(event.pos):
                self.game_state = "USERNAME"
            elif self.setting_icon_rect.collidepoint(event.pos):
                pygame.quit()  # Exit the game
            elif self.trophy_icon_rect.collidepoint(event.pos):
                self.game_state = "LEADERBOARD"

    def pause(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game_state = "PLAYING"

    def display_leaderboard(self):
        self.read_leaderboard()
        return self.topPlayer

    def display_leaderboard_screen(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.leaderboard_back_button_rect.collidepoint(event.pos):
                self.game_state = "DASHBOARD"

    def setting(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.resume_button_rect.collidepoint(event.pos):
                self.game_state = "PLAYING"
            elif self.restart_button_rect.collidepoint(event.pos):
                self.game_state = "USERNAME"
            elif self.setting_button_rect.collidepoint(event.pos):
                # HangmanDashboard.run_setting()
                print("Setting")

    def handle_username_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_button_react.collidepoint(event.pos):
                self.game_state = "DASHBOARD"
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and self.username:
                self.game_state = "PLAYING"
                self.initialize_questions()
                self.generate_question()
                self.progress = ["-"] * len(self.current_question[1])
                self.get_letters(self.current_question[1])  # Pass the current question word
            elif event.key == pygame.K_BACKSPACE:
                self.username = self.username[:-1]
            else:
                if len(self.username) < 10:
                    self.username += event.unicode

    def handle_game_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.pause_button_rect.collidepoint(event.pos):
                self.game_state = "PAUSE"
            elif self.hint_button_rect.collidepoint(event.pos) and self.coins > 0:  # Handle hint button click
                self.coins -= 1
                self.show_hint()
        if event.type == pygame.KEYDOWN and event.unicode.isalpha():
            self.check_input(event.unicode.lower())
            if "-" not in self.progress:
                self.is_solved = True
                self.total_score += int(self.current_question[2])
                self.coins += 1  # Increment coins when the player correctly guesses a word
                self.generate_question()
                self.progress = ["-"] * len(self.current_question[1])
                self.get_letters(self.current_question[1])  # Pass the current question word
                self.is_solved = False
            if self.chances == 0:
                self.game_state = "GAMEOVER"
                self.read_leaderboard()
                self.update_leaderboard(self.username, self.total_score)

    def show_hint(self):
        # Show a hint by revealing one of the letters in the current word
        for i, letter in enumerate(self.current_question[1]):
            if self.progress[i] == "-":
                self.progress[i] = letter
                break

    def handle_pause_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.resume_button_rect.collidepoint(event.pos):
                self.game_state = "PLAYING"
            elif self.restart_button_rect.collidepoint(event.pos):
                self.reset_game()
                self.game_state = "PLAYING"  # Stay in playing mode
            elif self.home_button_rect.collidepoint(event.pos):
                self.save_score()
                self.reset_game()
                self.game_state = "DASHBOARD"

    def handle_game_over_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.home_button_gameover_rect.collidepoint(event.pos):
                self.save_score()
                self.reset_game()
                self.game_state = "DASHBOARD"

    def reset_game(self):
        self.total_score = 0
        self.coins = 0  # Reset coins
        self.chances = self.initial_chances
        self.is_solved = False
        self.is_game_over = False
        self.progress = []
        self.guessed_letters = [""] * 15
        self.current_question = ["", "", ""]
        self.initialize_questions()
        self.generate_question()
        self.progress = ["-"] * len(self.current_question[1])
        self.get_letters(self.current_question[1])
        # Do not reset the username

    def save_score(self):
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
                    elif self.game_state == "PAUSE":
                        self.handle_pause_input(event)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game_state == "DASHBOARD":
                        self.dashboard(event)
                    elif self.game_state == "USERNAME":
                        self.handle_username_input(event)
                    elif self.game_state == "PLAYING":
                        self.handle_game_input(event)
                    elif self.game_state == "PAUSE":
                        self.handle_pause_input(event)
                    elif self.game_state == "GAMEOVER":
                        self.handle_game_over_input(event)
                    elif self.game_state == "LEADERBOARD":
                        self.display_leaderboard_screen(event)

            screen.fill(WHITE)

            if self.game_state == "USERNAME":
                UIRenderer.draw_username_screen(self.username, self.background, self.back_button)
            elif self.game_state == "PLAYING":
                UIRenderer.draw_game_screen(
                    self,
                    self.current_question,
                    self.chances,
                    self.progress,
                    self.guessed_letters,
                    self.total_score,
                    self.background,
                    self.pause_button,
                    self.pause_button_rect
                )
                screen.blit(self.hint_button, self.hint_button_rect)  # Draw hint button
                self.draw_hangman(self.chances)
            elif self.game_state == "GAMEOVER":
                UIRenderer.draw_game_over_screen(
                    self.total_score,
                    self.display_leaderboard(),
                    self.background,
                    self.current_question[1],  # correct_answer argument
                    self.home_button_gameover,  # Add home_button argument
                    self.home_button_gameover_rect  # Add home_button_rect argument
                )
            elif self.game_state == "DASHBOARD":
                UIRenderer.draw_dashboard_screen(self.play_button_rect, self.setting_icon_rect, self.trophy_icon_rect, self.background, self.play_button, self.setting_icon, self.trophy_icon)
            elif self.game_state == "PAUSE":
                UIRenderer.draw_pause_screen(self.resume_button_rect, self.restart_button_rect, self.home_button_rect, self.background, self.resume_button, self.restart_button, self.home_button)
            elif self.game_state == "LEADERBOARD":
                UIRenderer.draw_leaderboard_screen(self.display_leaderboard(), self.background, self.leaderboard_back_button_rect)

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()