import pygame
from pygame.locals import *
from imagenes1 import *

#Clase dedicada a funciones del jugador
class Jugador():
    #Inicialización de variables
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
        self.vida = 20  # Vida inicial
        self.vida_max = 20  # Vida máxima inicial
        self.monedas = 1  # Inicia con 1 moneda
        self.mejoras = {
            "HP": 0,  # Mejoras de vida (máximo 3)
            "ATK": 0,  # Mejoras de ataque (máximo 3)
            "VEL": 0   # Mejoras de velocidad (máximo 3)
        }
        self.velocidad = 15
        self.largo_barra = 200
        self.ancho_barra = 20
        self.borde_barra = 2
        self.muerto = False
        self.contador_muerte = 0
        self.tamano = 130
        self.escalar_imagenes()
        self.altura_salto = 60
        self.cooldown_salto = 5  # 5 frames a 10 FPS = 0.5 segundos
        self.tiempo_cooldown = 0  # Para contar el tiempo de cooldown
        self.puede_saltar = True  # Para saber si puede saltar
        self.game_over = False
        self.daño = 1000
        self.rect = self.jugador.get_rect(topleft=(self.x, self.y))

    def escalar_imagenes(self):
        self.jugador = pygame.transform.scale(jugador_caminar[self.contador_j], (self.tamano, self.tamano))
        for i in range(len(jugador_caminar)):
            jugador_caminar[i] = pygame.transform.scale(jugador_caminar[i], (self.tamano, self.tamano))
        for i in range(len(jugador_pegar)):
            jugador_pegar[i] = pygame.transform.scale(jugador_pegar[i], (self.tamano, self.tamano))
        for i in range(len(jugador_saltar)):
            jugador_saltar[i] = pygame.transform.scale(jugador_saltar[i], (self.tamano, self.tamano))
        for i in range(len(jugador_morir)):
            jugador_morir[i] = pygame.transform.scale(jugador_morir[i], (self.tamano, self.tamano))
    def cambiar_tamano(self, nuevo_tamano, nueva_x, nueva_y, nueva_altura_salto=None):
        self.tamano = nuevo_tamano
        self.x = nueva_x
        self.y = nueva_y
        if nueva_altura_salto is not None:
            self.altura_salto = nueva_altura_salto
        self.escalar_imagenes()
    
    #Función dedicada al movimiento horizontal del jugador
    def mover(self):
        teclas = pygame.key.get_pressed()
        
        #Movimiento hacia la derecha
        if teclas[K_RIGHT] and not self.muerto:
            if self.contador_j == 7:
                self.contador_j = 0
            else:
                self.contador_j += 1
            self.jugador = jugador_caminar[self.contador_j]
            self.jugador = pygame.transform.scale(self.jugador, (self.tamano, self.tamano))
            if self.x < 960:
                self.x += 15
                self.x += self.velocidad
                self.rect.x = self.x
            self.direccion = "d"
            
        
        #Movimiento hacia la izquierda
        elif teclas[K_LEFT] and not self.muerto:
            if self.contador_j == 7:
                self.contador_j = 0
            else:
                self.contador_j += 1
            self.jugador = jugador_caminar[self.contador_j]
            self.jugador = pygame.transform.scale(self.jugador, (self.tamano, self.tamano))
            self.jugador = pygame.transform.flip(self.jugador, True, False)
            if self.x > -75:
                self.x -= 15
                self.x -= self.velocidad
                self.rect.x = self.x
            self.direccion = "i"
            
        
        #Logica estatica del jugador
        else:
            if not self.muerto:
                if self.direccion == "d":
                    self.jugador = jugador_caminar[0]
                    self.jugador = pygame.transform.scale(self.jugador, (self.tamano, self.tamano))
                elif self.direccion == "i":
                    self.jugador = jugador_caminar[0]
                    self.jugador = pygame.transform.scale(self.jugador, (self.tamano, self.tamano))
                    self.jugador = pygame.transform.flip(self.jugador, True, False)
                    
    def mejorar(self, atributo):
        if self.monedas > 0 and self.mejoras[atributo] < 3:
            self.monedas -= 1
            self.mejoras[atributo] += 1
            if atributo == "HP":
                self.vida_max += 10
                self.vida = self.vida_max
            elif atributo == "ATK":
                self.daño+=1
            elif atributo == "VEL":
                self.velocidad += 5
                
    #Función dedicada a la animacion del ataque del jugador
    def pegar(self):
        teclas = pygame.key.get_pressed()
        
        #Lectura del boton de ataque
        if teclas[K_z] and not self.atacando and not self.muerto:
            self.atacando = True
            self.contador_ataque = 0
            if self.direccion == "d":
                self.rect_ataque = pygame.Rect(self.x + self.tamano, self.y, self.tamano // 2, self.tamano)
            else:
                self.rect_ataque = pygame.Rect(self.x - self.tamano // 2, self.y, self.tamano // 2, self.tamano)
        #Logica de la animación del ataque
        if self.atacando:
            if self.contador_ataque < len(jugador_pegar):
                
                if self.direccion == "i":
                    self.jugador = jugador_pegar[self.contador_ataque]
                    self.jugador = pygame.transform.scale(self.jugador, (self.tamano, self.tamano))
                    self.jugador = pygame.transform.flip(self.jugador, True, False)
                    self.contador_ataque += 1
                else:
                    self.jugador = jugador_pegar[self.contador_ataque]
                    self.jugador = pygame.transform.scale(self.jugador, (self.tamano, self.tamano))
                    self.contador_ataque += 1
            else:
                self.atacando = False
                self.contador_j = 0
                self.rect_ataque = None
                
    def aplicar_daño(self, objetivo):
        if self.atacando and self.rect_ataque and self.rect_ataque.colliderect(objetivo.rect):
            objetivo.recibir_dano(self.daño)
            print(f"¡Golpe! El jugador hizo {self.daño} de daño.")
            return True
        return False
    
    #Función dedicada a la animación de salto del jugador
    def saltar(self):
        teclas = pygame.key.get_pressed()
        if not self.puede_saltar:
            self.tiempo_cooldown += 1
            if self.tiempo_cooldown >= self.cooldown_salto:
                self.puede_saltar = True
                self.tiempo_cooldown = 0
        #Lectura de la tecla de salto
        if teclas[K_SPACE] and not self.saltando and not self.muerto and self.puede_saltar:
            self.saltando = True
            self.contador_salto = 0
            self.puede_saltar = False  # Iniciar cooldown
            self.tiempo_cooldown = 0
        
        #Logica de la animacion de salto
        if self.saltando:
            if self.contador_salto < len(jugador_saltar):
                if self.direccion == "i":
                    self.jugador = jugador_saltar[self.contador_salto]
                    self.jugador = pygame.transform.scale(self.jugador, (self.tamano, self.tamano))
                    self.jugador = pygame.transform.flip(self.jugador, True, False)
                    if -1 < self.contador_salto < 2:
                        self.y -= self.altura_salto
                    elif 2 < self.contador_salto < 5:
                        self.y += self.altura_salto
                    self.contador_salto += 1
                else:
                    self.jugador = jugador_saltar[self.contador_salto]
                    self.jugador = pygame.transform.scale(self.jugador, (self.tamano, self.tamano))
                    if -1 < self.contador_salto < 2:
                        self.y -= self.altura_salto
                        self.rect.y = self.y
                    elif 2 < self.contador_salto < 5:
                        self.y += self.altura_salto
                        self.rect.y = self.y
                    self.contador_salto += 1
            else:
                self.saltando = False
                self.contador_salto = 0
    
    #Función dedicada a la animacion de muerte del jugador
    def morir(self):
        if self.vida == 0:
            self.muerto = True
        
        if self.muerto:
            if self.contador_muerte < (len(jugador_morir)):
                if self.direccion == "i":
                    self.jugador = jugador_morir[self.contador_muerte]
                    self.jugador = pygame.transform.scale(self.jugador, (self.tamano, self.tamano))
                    self.jugador = pygame.transform.flip(self.jugador, True, False)
                    self.contador_muerte += 1
                else:
                    self.jugador = jugador_morir[self.contador_muerte]
                    self.jugador = pygame.transform.scale(self.jugador, (self.tamano, self.tamano))
                    self.contador_muerte += 1

    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0

    def dibujar_vida(self, screen):
        vida_actual = int((self.vida / 20) * self.largo_barra)
        
        pygame.draw.rect(screen, (255, 0, 0), (10, 10, self.largo_barra, self.ancho_barra))
        pygame.draw.rect(screen, (0, 255, 0), (10, 10, vida_actual, self.ancho_barra))
        pygame.draw.rect(screen, (255, 255, 255), (10, 10, self.largo_barra, self.ancho_barra), self.borde_barra)

        font = pygame.font.SysFont("Ravie", 24)
        texto_vida = font.render(f"{self.vida}/{self.vida_max}", True, (0, 0, 255))  
        screen.blit(texto_vida, (10, 35))
