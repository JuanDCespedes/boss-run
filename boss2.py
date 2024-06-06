import pygame
from imagenes1 import *

class Boss:
    def __init__(self, x, y):
        self.vida = 1
        self.vida_max = 1
        self.imagenes_correr = boss2_caminar  # Asignar la lista de imagenes cargada
        self.imagenes_ataque = boss2_atacar  # Asignar la lista de imagenes cargada  
        self.imagen_actual = 0
        self.boss = self.imagenes_correr[self.imagen_actual]
        self.boss = pygame.transform.scale(self.boss, (200, 200))
        self.x = 700
        self.y = 400
        self.imagen  = boss2_imagen 
        self.direccion = "d"
        self.velocidad = 10
        self.recibiendo_dano = False

    def mover(self):
        if self.direccion == "d":
            self.x += self.velocidad
        else:
            self.x -= self.velocidad

        # Cambio de dirección al alcanzar los bordes
        if self.x >= 800 - 200:  # Asumiendo que la pantalla tiene 800 px de ancho
            self.direccion = "i"
        elif self.x <= 0:
            self.direccion = "d"

    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            self.vida = 0
            self.morir()

    def atacar(self, jugador):
        # Verificar si el jugador está en la posición correcta para recibir daño (por la espalda)
        if self.direccion == "d" and jugador.x < self.x or self.direccion == "i" and jugador.x > self.x:
            jugador.recibir_dano(3)

    def morir(self):
        self.muerto = True
        # Aquí podrías añadir animación o lógica adicional para la muerte del boss

    def dibujar(self, pantalla):
        pantalla.blit(self.boss, (self.x, self.y))
