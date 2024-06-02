import pygame
from pygame.locals import *
from imagenes1 import *

class Boss1:
    def __init__(self):
        self.vida = 1000  # Vida inicial del jefe
        self.x = 780  # Posición x inicial
        self.y = 340  # Posición y inicial
        self.imagen = boss1_imagen
        self.rect = self.imagen.get_rect(topleft=(self.x, self.y))
        # Variables para la cinemática
        self.cinematica_activa = False
        self.frame_actual = 0
        self.frames_por_imagen = 10  # Cambia de imagen cada 6 frames (a 10 FPS, esto es cada 0.6 segundos)
        self.contador_frames = 0
        self.cinematica_mostrada = False
        
    def actualizar_cinematica(self):
        if self.cinematica_activa and not self.cinematica_mostrada:
            self.contador_frames += 1
            if self.contador_frames >= self.frames_por_imagen:
                self.contador_frames = 0
                self.frame_actual += 1
                print(f"Mostrando frame {self.frame_actual} de la cinemática")  # Para depuración
                if self.frame_actual >= len(boss1_cinematica):
                    self.cinematica_activa = False
                    self.frame_actual = 0
                    self.cinematica_mostrada = True
                    print("Cinemática terminada")
                    
    def iniciar_cinematica(self):
        if not self.cinematica_mostrada:
            self.cinematica_activa = True
            self.frame_actual = 0
            self.contador_frames = 0
            print("Iniciando cinemática")
            
    def draw(self, screen):
        if self.cinematica_activa:
            screen.blit(boss1_cinematica[self.frame_actual], (0, 0))
        else:
            screen.blit(self.imagen, self.rect)