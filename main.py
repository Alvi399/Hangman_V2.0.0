import pygame
import sys
import threading
import os

def run_setting():
    os.system("setting.py")
def main():
    pygame.init()

    # Screen setup
    screen_width, screen_height = 900, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Hangman Landing Page")

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (0, 153, 255)
    green = (0, 255, 128)
    yellow = (255, 223, 0)

    # Fonts 
    title_font = pygame.font.SysFont("comicsansms", 60)
    button_font = pygame.font.SysFont("comicsansms", 40)

    # Assets placeholders
    hangman_rope = None  # Insert rope image later
    settings_icon = pygame.image.load("./Asset/settings_icon.png")
    trophy_icon = pygame.image.load("./Asset/trophy_icon.png")  # Insert trophy icon later

    # Load placeholder assets
    # try:
    #     hangman_rope = pygame.image.load("rope.png")
    #     settings_icon = pygame.image.load("./Asset/settings_icon.png")
    #     trophy_icon = pygame.image.load("trophy.png")
    # except Exception as e:
    #     print("Missing asset files. Replace placeholders later.")

    # Button setup
    play_button_rect = pygame.Rect((screen_width // 2 - 75, screen_height // 2 - 50), (150, 100))

    #setting icon
    setting_icon_react = pygame.Rect((screen_width - 50, 10), (40,40))

    #tropy react 
    tropy_icon_react = pygame.Rect((20, screen_height - 70), (40, 40))
    # Main loop
    running = True
    while running:
        screen.fill(white)

        # Draw title
        title_text = title_font.render("HANGMAN", True, blue)
        screen.blit(title_text, (screen_width // 2 - title_text.get_width() // 2, 50))

        # Draw rope placeholder
        if hangman_rope:
            screen.blit(hangman_rope, (screen_width // 2 - 50, 120))
        else:
            pygame.draw.line(screen, blue, (screen_width // 2, 120), (screen_width // 2, 180), 5)
            pygame.draw.circle(screen, blue, (screen_width // 2, 190), 10, 2)

        # Draw play button
        pygame.draw.rect(screen, black, play_button_rect, border_radius=20)
        pygame.draw.rect(screen, green, play_button_rect.inflate(-10, -10), border_radius=20)
        play_text = button_font.render("Play", True, white)
        screen.blit(play_text, (play_button_rect.centerx - play_text.get_width() // 2, play_button_rect.centery - play_text.get_height() // 2))

        # Draw Setings icon 
        # Draw settings icon placeholder
        if settings_icon:
            # pygame.draw.rect(screen, blue, setting_icon_react, border_radius=20)
            screen.blit(settings_icon, (screen_width - 50, 10))
        else:
            pygame.draw.rect(screen, blue, setting_icon_react, border_radius=20)
            # pygame.draw.circle(screen, blue, (screen_width - 50, 50), 20, 2)

        # Draw trophy icon placeholder
        if trophy_icon:
            screen.blit(trophy_icon, (20, screen_height - 70))
        else:
            pygame.draw.rect(screen, yellow, tropy_icon_react, border_radius=20)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    print("Play button clicked")
                    # threading.Thread(target=run_setting).start()
                if setting_icon_react.collidepoint(event.pos):
                    print("Settings icon clicked")
                    threading.Thread(target=run_setting).start()
                if tropy_icon_react.collidepoint(event.pos):
                    print("Tropy is clicked")
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
