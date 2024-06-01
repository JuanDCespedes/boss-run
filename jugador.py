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
            self.jugador = pygame.transform.scale(self.jugador, (130, 130))
            if self.x < 960:
                self.x += 15
                self.x += self.velocidad
            self.direccion = "d"
            
        
        #Movimiento hacia la izquierda
        elif teclas[K_LEFT] and not self.muerto:
            if self.contador_j == 7:
                self.contador_j = 0
            else:
                self.contador_j += 1
            self.jugador = jugador_caminar[self.contador_j]
            self.jugador = pygame.transform.scale(self.jugador, (130, 130))
            self.jugador = pygame.transform.flip(self.jugador, True, False)
            if self.x > -75:
                self.x -= 15
                self.x -= self.velocidad
            self.direccion = "i"
            
        
        #Logica estatica del jugador
        else:
            if not self.muerto:
                if self.direccion == "d":
                    self.jugador = jugador_caminar[0]
                    self.jugador = pygame.transform.scale(self.jugador, (130, 130))
                elif self.direccion == "i":
                    self.jugador = jugador_caminar[0]
                    self.jugador = pygame.transform.scale(self.jugador, (130, 130))
                    self.jugador = pygame.transform.flip(self.jugador, True, False)
    def mejorar(self, atributo):
        if self.monedas > 0 and self.mejoras[atributo] < 3:
            self.monedas -= 1
            self.mejoras[atributo] += 1
            if atributo == "HP":
                self.vida_max += 10
                self.vida = self.vida_max
            elif atributo == "ATK":
                # No es necesario hacer nada aquí, ya que no tienes una variable de daño
                pass
            elif atributo == "VEL":
                self.velocidad += 5
    #Función dedicada a la animacion del ataque del jugador
    def pegar(self):
        teclas = pygame.key.get_pressed()
        
        #Lectura del boton de ataque
        if teclas[K_z] and not self.atacando and not self.muerto:
            self.atacando = True
            self.contador_ataque = 0

        #Logica de la animación del ataque
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
    
    #Función dedicada a la animación de salto del jugador
    def saltar(self):
        teclas = pygame.key.get_pressed()
        
        #Lectura de la tecla de salto
        if teclas[K_SPACE] and not self.saltando and not self.muerto:
            self.saltando = True
            self.contador_salto = 0
        
        #Logica de la animacion de salto
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
    
    #Función dedicada a la animacion de muerte del jugador
    def morir(self):
        if self.vida == 0:
            self.muerto = True
        
        if self.muerto:
            if self.contador_muerte < (len(jugador_morir)):
                if self.direccion == "i":
                    self.jugador = jugador_morir[self.contador_muerte]
                    self.jugador = pygame.transform.scale(self.jugador, (130, 130))
                    self.jugador = pygame.transform.flip(self.jugador, True, False)
                    self.contador_muerte += 1
                else:
                    self.jugador = jugador_morir[self.contador_muerte]
                    self.jugador = pygame.transform.scale(self.jugador, (130, 130))
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

        font = pygame.font.SysFont("Arial", 24)
        texto_vida = font.render(f"{self.vida}/20", True, (0, 0, 255))  
        screen.blit(texto_vida, (10, 35))