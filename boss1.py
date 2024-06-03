# boss1.py
import pygame
from pygame.locals import *
from imagenes1 import *

class Boss1:
    def __init__(self):
        self.vida = 1000  # Vida inicial del jefe
        self.vida_max = 1000
        self.x = 780  # Posición x inicial
        self.y = 350  # Posición y inicial ajustada
        self.imagen = boss1_imagen
        self.rect = self.imagen.get_rect(topleft=(self.x, self.y))
        # Variables para la cinemática
        self.cinematica_activa = False
        self.frame_actual = 0
        self.frames_por_imagen = 2  # Cambia de imagen cada 2 frames
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
            
    def draw(self, screen, fondo):
        if self.cinematica_activa:
            screen.blit(fondo, (0, 0))  # Dibuja el fondo primero
            screen.blit(boss1_cinematica[self.frame_actual], (self.x, self.y))  # Dibuja la cinemática en la posición correcta
        else:
            screen.blit(self.imagen, self.rect)
    
    def dibujar_vida(self, screen):
        # Calcula la longitud de la barra de vida basada en la vida actual
        vida_actual = int((self.vida / self.vida_max) * 300)  # 300 es el ancho de la barra
        barra_completa = "<" + "=" * (vida_actual // 10) + " " * ((300 - vida_actual) // 10) + ">"
        
        font = pygame.font.SysFont("Courier New", 24)
        texto_barra = font.render(barra_completa, True, (255, 0, 0))
        screen.blit(texto_barra, (360, 550))  # Centrando en la parte inferior de la pantalla