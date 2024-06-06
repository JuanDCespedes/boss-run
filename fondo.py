import pygame
from pygame.locals import *
from imagenes1 import *
from jugador import *
from boss1 import *
#Clase dedicada al manejo del fondo
class Fondo():
    def __init__(self, jugador):
        self.contador_f = 0
        self.lobby = lobby[self.contador_f]
        self.num_fondo = 0
        self.imagen_fondo = lobby[self.contador_f]
        self.jugador = jugador
        self.transicion = False
        self.tiempo_transicion = 0
        self.tiempo_transicion_total = 10  # 10 frames a 10 FPS = 1 segundo
        self.fondo_destino = None  # Para guardar el fondo al que vamos a transicionar
        self.portal_usado = None  # Para saber qué portal se usó: "izquierda", "centro" o "derecha"
        self.opacidad = 0
        self.transicion_completa = False
    
    #Función dedicada a refrezcar el fondo
    def animar_fondo(self):
        if self.num_fondo == 0:
            if self.contador_f == 31:
                self.contador_f = 0
            else:
                self.contador_f += 1
            self.imagen_fondo = lobby[self.contador_f]
            pass
        elif self.transicion and self.portal_usado:
            self.imagen_fondo = pantalla_carga
            self.tiempo_transicion += 1
            if self.tiempo_transicion > self.tiempo_transicion_total:
                self.transicion = False
                self.tiempo_transicion = 0
                self.imagen_fondo = self.fondo_destino
                self.portal_usado = None
        elif self.num_fondo == 1:
            self.imagen_fondo = pygame.image.load("imagenes/habitacion.png")
            if self.transicion:
                self.imagen_fondo = pantalla_carga
                self.tiempo_transicion += 1
                if self.tiempo_transicion > 10:  # 10 frames a 10 FPS = 1 segundo
                    self.transicion = False
                    self.tiempo_transicion = 0
                    self.imagen_fondo = pygame.image.load("imagenes/habitacion.png")
            else:
                self.imagen_fondo = pygame.image.load("imagenes/habitacion.png")
        elif self.num_fondo == 2:
            self.imagen_fondo = pygame.image.load("imagenes/jefe_1.png")
            if self.transicion:
                self.imagen_fondo = pantalla_carga
                self.tiempo_transicion += 1
                if self.tiempo_transicion > 10:
                    self.transicion = False
                    self.tiempo_transicion = 0
                    self.imagen_fondo = pygame.image.load("imagenes/jefe_1.png")
            else:
                self.imagen_fondo = pygame.image.load("imagenes/jefe_1.png")
        elif self.num_fondo == 3:
            self.imagen_fondo = pygame.image.load("imagenes/jefe_2.png")
            if self.transicion:
                self.imagen_fondo = pantalla_carga
                self.tiempo_transicion += 1
                if self.tiempo_transicion > 10:
                    self.transicion = False
                    self.tiempo_transicion = 0
                    self.imagen_fondo = pygame.image.load("imagenes/jefe_2.png")
                    self.transicion_completa=True
            else:
                self.imagen_fondo = pygame.image.load("imagenes/jefe_2.png")
        elif self.num_fondo == 4:
            self.imagen_fondo = pygame.image.load("imagenes/jefe_3.png")
            if self.transicion:
                self.imagen_fondo = pantalla_carga
                self.tiempo_transicion += 1
                if self.tiempo_transicion > 10:
                    self.transicion = False
                    self.tiempo_transicion = 0
                    self.imagen_fondo = pygame.image.load("imagenes/jefe_3.png")
            else:
                self.imagen_fondo = pygame.image.load("imagenes/jefe_3.png")
    
    
    #Función dedicada al cambio de habitación
    def cambiar_fondo(self, boss1_muerto=False, boss3_muerto=False):
        teclas = pygame.key.get_pressed()
        
        if teclas[K_UP]:
            if 402 <= self.jugador.x <= 510 and self.num_fondo == 0:
                self.num_fondo = 1
                self.imagen_fondo = pygame.image.load("imagenes/habitacion.png")
            elif self.num_fondo == 1:
                print(f"posicion del jugador: ({self.jugador.x}, {self.jugador.y})")
                print(f"Fondo actual: {self.num_fondo}")
                if 0 <= self.jugador.x <= 210 and not boss1_muerto:  # Verifica si el Boss1 no ha sido derrotado
                    print("Entrando al portal izquierdo")
                    self.transicion = True
                    self.tiempo_transicion = 0
                    self.num_fondo = 2
                    self.fondo_destino = pygame.image.load("imagenes/jefe_1.png")
                    self.portal_usado = "izquierda"
                    self.jugador.cambiar_tamano(120, 90, 440, 170)
                elif 360 <= self.jugador.x <= 540:
                    print("Entrando al portal del centro (Boss2)")
                    self.transicion = True
                    self.tiempo_transicion = 0
                    self.num_fondo = 3
                    self.fondo_destino = pygame.image.load("imagenes/jefe_2.png")
                    self.portal_usado = "centro"
                elif 690 <= self.jugador.x <= 870 and not boss3_muerto:
                    print ("Entrando al portal derecho")
                    self.transicion = True
                    self.tiempo_transicion = 0
                    self.num_fondo = 4
                    self.fondo_destino = pygame.image.load("imagenes/jefe_3.png")
                    self.portal_usado = "derecha"
        if teclas[K_LEFT] and self.num_fondo == 1 and self.jugador.x == -75:
            self.num_fondo = 0
            self.imagen_fondo = lobby[self.contador_f]
            self.jugador.cambiar_tamano(130, 0, 450, 40)
    
    #Función encargada de cambiar el fondo a fondo de muerte
    def pantalla_muerte(self):
        if self.jugador.vida == 0:
            if self.opacidad < 255:
                self.opacidad += 17
        

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