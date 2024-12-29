import pygame
from constants import screen, BLACK, WINDOW_WIDTH, WHITE

class UIRenderer:
    @staticmethod
    def draw_text(text, size, x, y, color=BLACK):
        font = pygame.font.SysFont("comicsansms", size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    @staticmethod
    def draw_username_screen(username, background_image, back_button):
        back_button = pygame.transform.scale(back_button, (40, 40))
        screen.blit(background_image, (0, 0))
        screen.blit(back_button, (10, 10))

        UIRenderer.draw_text("Enter Username:", 32, WINDOW_WIDTH//2, 250)
        UIRenderer.draw_text(username, 32, WINDOW_WIDTH//2, 300)

    @staticmethod
    def draw_game_screen(current_question, chances, progress, guessed_letters, total_score, background_image, pause_button, pause_button_rect):
        # TODO: Draw game background
        screen.blit(background_image, (0, 0))
        pause_button = pygame.transform.scale(pause_button, (40, 40))
        screen.blit(pause_button, pause_button_rect)
        
        UIRenderer.draw_text(f"Topic: {current_question[0]}", 32, WINDOW_WIDTH//2, 50)
        UIRenderer.draw_text(f"Score: {current_question[2]}", 32, 100, 30)
        UIRenderer.draw_text(f"Total Score: {total_score}", 32, 200, 30)
        UIRenderer.draw_text(f"Chances: {chances}", 32, 300, 30)
        
        progress_text = " ".join(progress)
        UIRenderer.draw_text(progress_text, 48, WINDOW_WIDTH//2, 400)
        
        letters_text = " ".join(guessed_letters)
        UIRenderer.draw_text(letters_text, 32, WINDOW_WIDTH//2, 500)

       
    @staticmethod
    def draw_game_over_screen(total_score, top_players, game_over_bg):
        # TODO: Draw game over background
        screen.blit(game_over_bg, (0, 0))
        
        UIRenderer.draw_text("Game Over!", 64, WINDOW_WIDTH//2, 100)
        UIRenderer.draw_text(f"Final Score: {total_score}", 48, WINDOW_WIDTH//2, 200)
        
        # Draw leaderboard
        UIRenderer.draw_text("Leaderboard", 40, WINDOW_WIDTH//2, 300)
        for i, (name, score) in enumerate(top_players[:5]):
            UIRenderer.draw_text(f"{i+1}. {name}: {score}", 32, WINDOW_WIDTH//2, 350 + i*40)

    @staticmethod
    def draw_dashboard_screen(play_button_rect, setting_icon_rect, trophy_icon_rect, background_image, play_button, setting_icon, trophy_icon):
        #transform icon size to rect size
        setting_icon = pygame.transform.scale(setting_icon, (40, 40))
        trophy_icon = pygame.transform.scale(trophy_icon, (40, 40))
        play_button = pygame.transform.scale(play_button, (200, 100))
        
        #draw background game 
        screen.blit(background_image, (0, 0))

        #draw play button
        screen.blit(play_button, play_button_rect)

        #draw setting icon
        screen.blit(setting_icon, setting_icon_rect)

        #draw trophy icon
        screen.blit(trophy_icon, trophy_icon_rect)

        #draw title
        UIRenderer.draw_text("HANGMAN", 64, WINDOW_WIDTH//2, 50)
        #draw rope placeholder
        pygame.draw.line(screen, (0, 0, 255), (WINDOW_WIDTH // 2, 120), (WINDOW_WIDTH // 2, 180), 5)
        pygame.draw.circle(screen, (0, 0, 255), (WINDOW_WIDTH // 2, 190), 10, 2)

    @staticmethod
    def draw_pause_screen(resume_button_rect, restart_button_rect, setting_button_rect, background_image, resume_button, restart_button, setting_button):
        #transform icon size to rect size
        resume_button = pygame.transform.scale(resume_button, (200, 100))
        restart_button = pygame.transform.scale(restart_button, (200, 100))
        setting_button = pygame.transform.scale(setting_button, (200, 100))
        
        #draw background game 
        screen.blit(background_image, (0, 0))

        #draw resume button
        screen.blit(resume_button, resume_button_rect)

        #draw restart button
        screen.blit(restart_button, restart_button_rect)

        #draw setting button
        screen.blit(setting_button, setting_button_rect)

        #draw title
        UIRenderer.draw_text("PAUSE", 64, WINDOW_WIDTH//2, 50)
        #draw rope placeholder
        pygame.draw.line(screen, (0, 0, 255), (WINDOW_WIDTH // 2, 120), (WINDOW_WIDTH // 2, 180), 5)
        pygame.draw.circle(screen, (0, 0, 255), (WINDOW_WIDTH // 2, 190), 10, 2)

    @staticmethod
    def draw_pause_screen(resume_button_rect, restart_button_rect, home_button_rect, background_image, resume_button, restart_button, home_button):
        resume_button = pygame.transform.scale(resume_button, (200, 100))
        restart_button = pygame.transform.scale(restart_button, (200, 100))
        home_button = pygame.transform.scale(home_button, (200, 100))
        
        screen.blit(background_image, (0, 0))

        screen.blit(resume_button, resume_button_rect)
        screen.blit(restart_button, restart_button_rect)
        screen.blit(home_button, home_button_rect)

        UIRenderer.draw_text("PAUSED", 64, WINDOW_WIDTH//2, 50)
