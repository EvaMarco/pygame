import pygame
import sys
import random


class Runner:

    def __init__(self, x=0, y=0):
        ixcustom = random.randint(0, 4)

        self.custome = pygame.image.load('images/turtle.png')
        self.position = [x, y]
        self.name = 'Tortuga'

    def avanzar(self):
        self.position[0] += random.randint(1, 6)


class Game:
    runners = []
    __posy = (150, 202, 255, 307)
    __names = ('Roja', 'Naranja', 'Amarilla', 'Azul')
    __starline = 5
    __finishline = 620
    __customes = (pygame.image.load('images/turtle1.png'), pygame.image.load('images/turtle2.png'), pygame.image.load
    ('images/turtle3.png'), pygame.image.load('images/turtle4.png'))

    def __init__(self):

        # Creamos la pantalla.
        self.__screen = pygame.display.set_mode((640, 480))
        # Creamos el nombre.
        pygame.display.set_caption('Carrera de bichos')
        # Le decimos cual es el fondo que queremos. 
        self.background = pygame.image.load('images/background.png')
        for i in range(4):
            therunner = Runner(self.__starline, self.__posy[i])
            therunner.name = self.__names[i]
            therunner.custome = self.__customes[i]
            self.runners.append(therunner)

    def close(self):
        pygame.quit()
        sys.exit()

    def competir(self):

        gameover = False
        
        while not gameover:
            # Comprobación de eventos.

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = True

            # Actualizamos posiciones
            for runner in self.runners:
                runner.avanzar()
                if runner.position[0] >= self.__finishline:
                    print('{} ha ganado'.format(runner.name))
                    gameover = True

            # Renderizar la pantalla
            self.__screen.blit(self.background, (0, 0))

            # Renderizar los corredores moviendose

            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
            
            pygame.display.flip()

        while True:
            # Es un bucle infinito que se cierra cuando cerramos la pantalla. Así va limpiando los eventos.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()


if __name__ == '__main__':
    pygame.font.init()
    game = Game()
    game.competir()
