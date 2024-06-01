import pygame
from pygame.locals import *
from imagenes1 import *

class Jugador():    
    
    def __init__(self):
        self.contador_j = 0
        self.jugador = jugador_caminar[self.contador_j]
        self.jugador = pygame.transform.scale(self.jugador, (200, 200))
        self.x = 0
        self.y = 450
        self.atacando = False
        self.contador_ataque = 0
        self.direccion = "d"
        self.saltando = False
        self.contador_salto = 0
    
    def mover(self):
        teclas = pygame.key.get_pressed()
        
        if teclas[K_RIGHT]:
            if self.contador_j == 7:
                self.contador_j = 0
            else:
                self.contador_j += 1
            self.jugador = jugador_caminar[self.contador_j]
            self.jugador = pygame.transform.scale(self.jugador, (130, 130))
            self.x += 15
            self.direccion = "d"
            
        elif teclas[K_LEFT]:
            if self.contador_j == 7:
                self.contador_j = 0
            else:
                self.contador_j += 1
            self.jugador = jugador_caminar[self.contador_j]
            self.jugador = pygame.transform.scale(self.jugador, (130, 130))
            self.jugador = pygame.transform.flip(self.jugador, True, False)
            self.x -= 15
            self.direccion = "i"
        
        else:
            if self.direccion == "d":
                self.jugador = jugador_caminar[0]
                self.jugador = pygame.transform.scale(self.jugador, (130, 130))
            elif self.direccion == "i":
                self.jugador = jugador_caminar[0]
                self.jugador = pygame.transform.scale(self.jugador, (130, 130))
                self.jugador = pygame.transform.flip(self.jugador, True, False)
    
    def pegar(self):
        teclas = pygame.key.get_pressed()
        
        if teclas[K_z]:
            self.atacando = True
            self.contador_ataque = 0

        if self.atacando:
            if self.contador_ataque < len(jugador_pegar):
                if self.direccion == "i":
                    self.jugador = jugador_pegar[self.contador_ataque]
                    self.jugador = pygame.transform.scale(self.jugador, (130, 130))
                    self.jugador = pygame.transform.flip(self.jugador, True, False)
                    self.contador_ataque += 1
                else:
                    self.jugador = jugador_pegar[self.contador_ataque]
                    self.jugador = pygame.transform.scale(self.jugador, (130, 130))
                    self.contador_ataque += 1
            else:
                self.atacando = False
                self.contador_j = 0
                
    def saltar(self):
        teclas = pygame.key.get_pressed()
        
        if teclas[K_SPACE] and not self.saltando:
            self.saltando = True
            self.contador_salto = 0
        
        if self.saltando:
            if self.contador_salto < len(jugador_saltar):
                if self.direccion == "i":
                    self.jugador = jugador_saltar[self.contador_salto]
                    self.jugador = pygame.transform.scale(self.jugador, (130, 130))
                    self.jugador = pygame.transform.flip(self.jugador, True, False)
                    if -1 < self.contador_salto < 2:
                        self.y -= 40
                    elif 2 < self.contador_salto < 5:
                        self.y += 40
                    self.contador_salto += 1
                else:
                    self.jugador = jugador_saltar[self.contador_salto]
                    self.jugador = pygame.transform.scale(self.jugador, (130, 130))
                    if -1 < self.contador_salto < 2:
                        self.y -= 40
                    elif 2 < self.contador_salto < 5:
                        self.y += 40
                    self.contador_salto += 1
            else:
                self.saltando = False
                self.contador_salto = 0