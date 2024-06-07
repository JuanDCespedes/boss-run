import pygame
from pygame.locals import*
import random
from imagenes1 import *

class Boss:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.boss = pygame.transform.scale(boss2_atacar[4], (200, 200))  # Usamos solo la primera imagen
        self.boss = pygame.transform.flip(self.boss, True, False)
        self.rect = self.boss.get_rect(topleft=(self.x, self.y))
        self.direccion = -1  # -1 para izquierda
        self.cooldown_ataque = 60  # 60 frames a 10 FPS = 6 segundos
        self.ultimo_ataque = 0
        self.vida = 100
        self.vida_max = 100
        self.muriendo = False
        self.frame_muerte = 0
        self.frames_muerte = len(boss2_morir)

    def atacar(self):
        if pygame.time.get_ticks() - self.ultimo_ataque > self.cooldown_ataque:
            self.fuego = Fuego(self.x, self.y, self.direccion)
            self.ultimo_ataque = pygame.time.get_ticks()

    def recibir_dano(self, cantidad):
        pygame.mixer.init()
        pygame.mixer.music.load("sonido/efecto/0.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0

    def esta_muerto(self):
        return self.vida <= 0

    def dibujar(self, pantalla):
        pantalla.blit(self.boss, self.rect)

    def dibujar_vida(self, screen): 
        vida_actual = int((self.vida / self.vida_max) * 200)  # Asumiendo una barra de 200 píxeles
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y - 20, 200, 10))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y - 20, vida_actual, 10))
    def morir(self):
        if not self.muriendo:
            self.muriendo = True
            self.frame_muerte = 0

        if self.frame_muerte < self.frames_muerte:
            self.boss = pygame.transform.scale(boss2_morir[self.frame_muerte], (200, 200))
            self.frame_muerte += 1
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load("sonido/musica/0.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1) 
        else:
            return True

        return False

class Fuego:
    def __init__(self, x, y, direccion):
        self.x = x - 50  # Ajusta la posición inicial del fuego
        self.y = y + 50
        self.direccion = direccion
        self.velocidad = 10
        self.imagen = pygame.image.load("imagenes/boss2/caminar/fuego.png")
        self.rect = self.imagen.get_rect(topleft=(self.x, self.y))

    def mover(self):
        self.x += self.velocidad * self.direccion
        self.rect.x = self.x

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)