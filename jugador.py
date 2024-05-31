import pygame
from pygame.locals import *
from imagenes1 import *

class Jugador():
    def __init__(self):
        self.contador_j = 0
        self.jugador = jugador_caminar[self.contador_j]
        self.jugador = pygame.transform.scale(self.jugador, (200, 200))
        self.x = 0
        self.y = 300
    
    def mover(self):
        teclas = pygame.key.get_pressed()

        if teclas[K_RIGHT]:
            if self.contador_j == 7:
                self.contador_j = 0
            else:
                self.contador_j += 1
            self.jugador = jugador_caminar[self.contador_j]
            self.jugador = pygame.transform.scale(self.jugador, (200, 200))
            
        if teclas[K_LEFT]:
            if self.contador_j == 7:
                self.contador_j = 0
            else:
                self.contador_j += 1
            self.jugador = jugador_caminar[self.contador_j]
            self.jugador = pygame.transform.scale(self.jugador, (200, 200))
            self.jugador = pygame.transform.flip(self.jugador, True, False)