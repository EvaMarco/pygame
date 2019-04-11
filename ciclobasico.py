import pygame
import sys

width = 640
height = 480
# Tamaño de la pantalla
screen = pygame.display.set_mode((width, height))
# Color de la pantalla
screen.fill((255, 0, 0))
# Le damos nombre
pygame.display.set_caption('Ciclo básico de pygame')
# Iniciamos pygame.
pygame.font.init()
# Creamos condición.

gameover = False
while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    # Refrescar la pantalla.
    pygame.display.flip()

pygame.quit()
sys.exit()

