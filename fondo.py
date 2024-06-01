import pygame
from pygame.locals import *
from imagenes1 import *
from jugador import *

#Clase dedicada al manejo del fondo
class Fondo():
    #Inicialización de variables
    def __init__(self, jugador):
        self.contador_f = 0
        self.lobby = lobby[self.contador_f]
        self.num_fondo = 0
        self.imagen_fondo = lobby[self.contador_f]
        self.jugador = jugador
    
    #Función dedicada a refrezcar el fondo
    def animar_fondo(self):
        #Logica de animación del lobby
        if self.num_fondo == 0:
            if self.contador_f == 31:
                self.contador_f = 0
            else:
                self.contador_f += 1
            self.imagen_fondo = lobby[self.contador_f]
        #Refrezco de fondos alternativos
        elif self.num_fondo == 1:
            self.imagen_fondo = pygame.image.load("imagenes/habitacion.png")
        elif self.num_fondo == 2:
            self.imagen_fondo = pygame.image.load("imagenes/jefe_1.png")
        elif self.num_fondo == 3:
            self.imagen_fondo = pygame.image.load("imagenes/jefe_2.png")
        elif self.num_fondo == 4:
            self.imagen_fondo = pygame.image.load("imagenes/jefe_3.png")
    
    #Función dedicada al cambio de habitación
    def cambiar_fondo(self):
        teclas = pygame.key.get_pressed()
        
        if teclas[K_UP]:
            if 402 <= self.jugador.x <= 510 and self.num_fondo == 0:
                self.num_fondo = 1
            elif self.num_fondo == 1:
                if 105 <= self.jugador.x <= 165:
                    self.num_fondo = 2
                elif 440 <= self.jugador.x <= 500:
                    self.num_fondo = 3
                elif 780 <= self.jugador.x <= 840:
                    self.num_fondo = 4
        if teclas[K_LEFT] and self.num_fondo == 1 and self.jugador.x == -75:
            self.num_fondo = 0

#Clase dedicada al manejo de los portales
class Portal():
    #Inicializacion de variables
    def __init__(self, num_fondo):
        self.contador_p = 0
        self.imagen_portal = portal[self.contador_p]
        self.num_fondo = num_fondo
    
    #Función dedicada a la animación del portal
    def animar_portal(self):
        if self.contador_p == 5:
            self.contador_p = 0
        else:
            self.contador_p += 1
        self.imagen_portal = portal[self.contador_p]
        self.imagen_portal = pygame.transform.scale(self.imagen_portal, (250, 250))