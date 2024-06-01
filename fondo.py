import pygame
from pygame.locals import *
from imagenes1 import *
from jugador import *

class Fondo():
    def __init__(self, jugador):
        self.contador_f = 0
        self.lobby = lobby[self.contador_f]
        self.num_fondo = 0
        self.imagen = lobby[self.contador_f]
        self.jugador = jugador
        
    def animar_fondo(self):
        if self.num_fondo == 0:
            if self.contador_f == 31:
                self.contador_f = 0
            else:
                self.contador_f += 1
            self.imagen = lobby[self.contador_f]
        elif self.num_fondo == 1:
            self.imagen = pygame.image.load("imagenes/habitacion.png")
    
    def cambiar_fondo(self):
        teclas = pygame.key.get_pressed()
        
        if teclas[K_UP] and 402 <= self.jugador.x <= 510 and self.num_fondo == 0:
            self.num_fondo = 1

class Portal():
    def __init__(self):
        ola