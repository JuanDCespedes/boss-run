import pygame
from imagenes1 import *

class Fondo():
    def __init__(self):
        self.contador_f = 0
        self.lobby = lobby[self.contador_f]
        
    def animar_fondo(self):
        if self.contador_f == 31:
            self.contador_f = 0
        else:
            self.contador_f += 1
        self.lobby = lobby[self.contador_f]         