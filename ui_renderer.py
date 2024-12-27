import pygame
from constants import screen, BLACK, WINDOW_WIDTH

class UIRenderer:
    @staticmethod
    def draw_text(text, size, x, y, color=BLACK):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    @staticmethod
    def draw_username_screen(username):
        # TODO: Draw background image
        # screen.blit(background_image, (0, 0))
        
        UIRenderer.draw_text("HANGMAN", 64, WINDOW_WIDTH//2, 100)
        UIRenderer.draw_text("Enter Username:", 32, WINDOW_WIDTH//2, 250)
        UIRenderer.draw_text(username, 32, WINDOW_WIDTH//2, 300)

    @staticmethod
    def draw_game_screen(current_question, chances, progress, guessed_letters, total_score):
        # TODO: Draw game background
        # screen.blit(background_image, (0, 0))
        
        UIRenderer.draw_text(f"Topic: {current_question[0]}", 32, WINDOW_WIDTH//2, 50)
        UIRenderer.draw_text(f"Score: {current_question[2]}", 32, 700, 30)
        UIRenderer.draw_text(f"Total Score: {total_score}", 32, 700, 90)
        UIRenderer.draw_text(f"Chances: {chances}", 32, 700, 60)
        
        progress_text = " ".join(progress)
        UIRenderer.draw_text(progress_text, 48, WINDOW_WIDTH//2, 400)
        
        letters_text = " ".join(guessed_letters)
        UIRenderer.draw_text(letters_text, 32, WINDOW_WIDTH//2, 500)

    @staticmethod
    def draw_game_over_screen(total_score, top_players):
        # TODO: Draw game over background
        # screen.blit(game_over_bg, (0, 0))
        
        UIRenderer.draw_text("Game Over!", 64, WINDOW_WIDTH//2, 100)
        UIRenderer.draw_text(f"Final Score: {total_score}", 48, WINDOW_WIDTH//2, 200)
        
        # Draw leaderboard
        UIRenderer.draw_text("Leaderboard", 40, WINDOW_WIDTH//2, 300)
        for i, (name, score) in enumerate(top_players[:5]):
            UIRenderer.draw_text(f"{i+1}. {name}: {score}", 32, WINDOW_WIDTH//2, 350 + i*40)