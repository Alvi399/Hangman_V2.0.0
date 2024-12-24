import pygame, sys
from pygame.locals import * 

#inisialisasi program 
pygame.init()

#inisialisasi layar
DISPLAYSURF = pygame.display.set_mode((100, 200))

#loop untuk game 
running = True 
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == K_q:
            sys.exit()