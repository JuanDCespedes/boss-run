import pygame
import random
from imagenes1 import *

class Boss:
    def __init__(self, x, y):
        self.vida = 100
        self.vida_max = 100
        self.imagenes_caminar = boss2_caminar
        self.imagenes_ataque = boss2_atacar
        self.imagenes_saltar = boss2_saltar
        self.imagenes_muerte = boss2_morir
        self.frame_actual = 0
        self.boss = self.imagenes_caminar[self.frame_actual]
        self.boss = pygame.transform.scale(self.boss, (200, 200))
        self.x = x
        self.y = y
        self.direccion = 1  # 1 para derecha, -1 para izquierda
        self.velocidad = 5
        self.saltando = False
        self.velocidad_salto = 15
        self.gravedad = 1
        self.altura_salto = 0
        self.atacando = False
        self.frame_ataque = 0
        self.fuego = None
        self.rect = self.boss.get_rect(topleft=(self.x, self.y))
        self.cooldown_ataque = 60  # 60 frames a 10 FPS = 6 segundos
        self.ultimo_ataque = 0

    def mover(self):
        self.x += self.velocidad * self.direccion
        if self.x <= 0 or self.x >= 800:
            self.direccion *= -1
        
        if not self.saltando and random.randint(1, 100) == 1:  # 1% de probabilidad de saltar
            self.saltar()

        self.rect.x = self.x
        self.rect.y = self.y

    def saltar(self):
        if not self.saltando:
            self.saltando = True
            self.altura_salto = -self.velocidad_salto

    def actualizar(self, jugador):
        self.mover()
        
        if self.saltando:
            self.y += self.altura_salto
            self.altura_salto += self.gravedad
            if self.y >= 300:  # Asumiendo que 300 es el piso
                self.y = 300
                self.saltando = False
                self.altura_salto = 0

        self.rect.y = self.y
        
        self.atacar(jugador)
        
        if self.atacando:
            self.frame_ataque += 1
            if self.frame_ataque >= len(self.imagenes_ataque):
                self.frame_ataque = 0
                self.atacando = False
                self.boss = self.imagenes_caminar[self.frame_actual]
            else:
                self.boss = self.imagenes_ataque[self.frame_ataque]
        else:
            self.frame_actual = (self.frame_actual + 1) % len(self.imagenes_caminar)
            self.boss = self.imagenes_caminar[self.frame_actual]
        
        self.boss = pygame.transform.flip(self.boss, self.direccion == -1, False)

    def atacar(self, jugador):
        if not self.atacando and pygame.time.get_ticks() - self.ultimo_ataque > self.cooldown_ataque:
            if (self.direccion == 1 and jugador.x < self.x) or (self.direccion == -1 and jugador.x > self.x):
                self.atacando = True
                self.frame_ataque = 0
                self.fuego = Fuego(self.x, self.y, self.direccion)
                self.ultimo_ataque = pygame.time.get_ticks()

    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0

    def esta_muerto(self):
        return self.vida <= 0

    def dibujar(self, pantalla):
        pantalla.blit(self.boss, self.rect)

class Fuego:
    def __init__(self, x, y, direccion):
        self.x = x + (50 if direccion == 1 else -50)
        self.y = y + 100
        self.direccion = direccion
        self.velocidad = 10
        self.imagen = pygame.image.load("imagenes/boss2/fuego.png")
        self.rect = self.imagen.get_rect(topleft=(self.x, self.y))

    def mover(self):
        self.x += self.velocidad * self.direccion
        self.rect.x = self.x

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)