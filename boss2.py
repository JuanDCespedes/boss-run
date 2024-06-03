# boss.py

import pygame
import random

class Boss(pygame.sprite.Sprite):
    def __init__(self, width, height, player_pos):
        super().__init__()

        self.image = pygame.image.load("boss.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.width = width
        self.height = height
        self.player_pos = player_pos

        self.speed = 5
        self.direction = 1  # 1 para moverse a la derecha, -1 para moverse a la izquierda

    def update(self):
        # Movimiento horizontal
        self.rect.x += self.speed * self.direction

        # Cambiar la dirección si llega a los límites de la pantalla
        if self.rect.right >= self.width or self.rect.left <= 0:
            self.direction *= -1

        # Movimiento vertical (subiendo y bajando)
        if self.player_pos[1] < self.rect.y:
            self.rect.y -= self.speed
        elif self.player_pos[1] > self.rect.y:
            self.rect.y += self.speed

    def damage_player(self, player_rect):
        # Verificar si el jugador está detrás del boss
        if self.rect.x < player_rect.x:
            player_rect.x -= 10  # Hacer daño al jugador (moverlo hacia atrás)

