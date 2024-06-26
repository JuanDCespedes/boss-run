import pygame
from pygame.locals import *
from imagenes1 import *
from fondo import *

#Clase encargada de los funcionamientos del Jugador
class Jugador():    
    #Inicializacion de variables
    def __init__(self):
        self.direccion = "d"
        self.contador_j = 0
        self.x = 0
        self.y = 450
        self.contador_ataque = 0
        self.contador_salto = 0
    
    #Funcion encargada del recorrido horizontal del jugador
    def mover(self):
        teclas = pygame.key.get_pressed()
        
        #Movimiento hacia el lado derecho
        if teclas[K_RIGHT]:
            if self.contador_j == 7:
                self.contador_j = 0
            else:
                self.contador_j += 1
            self.jugador = jugador_caminar[self.contador_j]
            self.jugador = pygame.transform.scale(self.jugador, (130, 130))
            if self.x < 960:
                self.x += 15
            self.direccion = "d"
        
        #Movimiento hacia el lado izquierdo
        elif teclas[K_LEFT]:
            if self.contador_j == 7:
                self.contador_j = 0
            else:
                self.contador_j += 1
            self.jugador = jugador_caminar[self.contador_j]
            self.jugador = pygame.transform.scale(self.jugador, (130, 130))
            self.jugador = pygame.transform.flip(self.jugador, True, False)
            if self.x > -75:
                self.x -= 15
            self.direccion = "i"
        
        #Posicion estatica del jugador
        else:
            if self.direccion == "d":
                self.jugador = jugador_caminar[0]
                self.jugador = pygame.transform.scale(self.jugador, (130, 130))
            elif self.direccion == "i":
                self.jugador = jugador_caminar[0]
                self.jugador = pygame.transform.scale(self.jugador, (130, 130))
                self.jugador = pygame.transform.flip(self.jugador, True, False)
    
    #Funcion encargada de la animacion de ataque del jugador
    def pegar(self):
        teclas = pygame.key.get_pressed()
        
        #Lectura del boton de ataque
        if teclas[K_z]:
            self.atacando = True
            self.contador_ataque = 0

        #Logica de la animacion del ataque
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

    #Funcion encargada de la animacion de salto del jugador
    def saltar(self):
        teclas = pygame.key.get_pressed()
        
        #Lectura del boton de salto
        if teclas[K_SPACE] and not self.saltando:
            self.saltando = True
            self.contador_salto = 0
        
        #Logica de la animacion del salto
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

    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0

    def dibujar_vida(self, screen):
        largo_barra = 200
        ancho_barra = 20
        borde_barra = 2

        vida_actual = int((self.vida / 20) * largo_barra)
        
     
        pygame.draw.rect(screen, (255, 0, 0), (10, 10, largo_barra, ancho_barra))
        pygame.draw.rect(screen, (0, 255, 0), (10, 10, vida_actual, ancho_barra))
        pygame.draw.rect(screen, (255, 255, 255), (10, 10, largo_barra, ancho_barra), borde_barra)
        
        
        font = pygame.font.SysFont("ravie", 24)  
        texto_vida = font.render(f"{self.vida}/20", True, (0, 0, 255))  
        screen.blit(texto_vida, (10, 35))