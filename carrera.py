import pygame
import sys


class Game:
    corredores = []

    def __init__(self):
        # Creamos la pantalla.
        self.__screen = pygame.display.set_mode((640, 480))
        # Creamos el nombre.
        pygame.display.set_caption('Carrera de bichos')
        # Le decimos cual es el fondo que queremos. 
        self.background = pygame.image.load('images/background.png')
        self.runner = pygame.image.load('images/small_ball.png')
    
    def competir(self):
        x = 0
        hayganador = False
        
        while not hayganador:
            # Comprobación de eventos.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # Renderizar la pantalla
            self.__screen.blit(self.background, (0, 0))
            self.__screen.blit(self.runner, (x, 240))
            pygame.display.flip()
            
            x += 3
            if x >= 630:
                hayganador = True

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    pygame.font.init()
    game = Game()
    game.competir()
