# boss1.py
import pygame
from pygame.locals import *
from imagenes1 import *
import random

class Boss1:
    def __init__(self):
        self.vida = 1000  # Vida inicial del jefe
        self.vida_max = 1000
        self.x = 780  # Posición x inicial
        self.y = 400  # Posición y inicial ajustada
        self.imagen = boss1_imagen
        self.rect = self.imagen.get_rect(topleft=(self.x, self.y))
        # Variables para la cinemática
        self.cinematica_activa = False
        self.frame_actual = 0
        self.frames_por_imagen = 2  # Cambia de imagen cada 2 frames
        self.contador_frames = 0
        self.cinematica_mostrada = False
        self.caminando = False
        self.frame_caminar = 0
        self.frames_por_paso = 2  # Cambia de imagen cada 2 frames 
        self.contador_pasos = 0
        self.direccion = -1  # -1 para moverse a la izquierda (hacia el jugador)
        self.velocidad = 5  # Velocidad de movimiento
        self.mostrar_barra_vida = False  # Nueva variable para controlar la visibilidad
        self.largo_barra = 600  # Ancho de la barra de vida
        self.alto_barra = 30  # Alto de la barra de vida
        self.borde_barra = 4 
        self.atacando = False
        self.frame_ataque = 0
        self.frames_por_ataque = 0.5  # Cambia de imagen cada 2 frames
        self.contador_ataque = 0
        self.distancia_ataque = 100  # Distancia a la que el boss atacará al jugador
        self.damage = 1  # Daño que el ataque del boss hace al jugador
        self.atacando_corriendo = False
        self.frame_ataque_corriendo = 0
        self.frames_por_ataque_corriendo = 2
        self.contador_ataque_corriendo = 0
        self.distancia_ataque_corriendo = 800
        self.velocidad_ataque_corriendo = 30
        self.tiempo_quieto = 0
        self.tiempo_quieto_total = 25 
        self.cooldown_ataque_corriendo = random.randint(30, 70)  # Cooldown inicial aleatorio de 3 a 7 segundos (en milisegundos)
        self.ultimo_ataque_corriendo = pygame.time.get_ticks()
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
                    self.caminando = True
                    self.mostrar_barra_vida = True
                    print("Mostrando barra de vida del Boss1")
    def atacar_corriendo(self, jugador):
        if not self.atacando_corriendo and not self.atacando and not self.tiempo_quieto:
            if pygame.time.get_ticks() - self.ultimo_ataque_corriendo >= self.cooldown_ataque_corriendo:
                self.atacando_corriendo = True
                self.frame_ataque_corriendo = 0
                self.contador_ataque_corriendo = 0
                self.velocidad_original = self.velocidad
                self.velocidad = self.velocidad_ataque_corriendo
                self.direccion = random.choice([-1, 1])  # Elige una dirección aleatoria
                self.ultimo_ataque_corriendo = pygame.time.get_ticks()
                print("Boss1 atacando corriendo")
    
        if self.atacando_corriendo:
            self.contador_ataque_corriendo += 1
            if self.contador_ataque_corriendo >= self.frames_por_ataque_corriendo:
                self.contador_ataque_corriendo = 0
                self.frame_ataque_corriendo += 1
                if self.frame_ataque_corriendo >= len(boss1_ataque_corriendo):
                    self.frame_ataque_corriendo = 0
                    self.imagen = boss1_ataque_corriendo[self.frame_ataque_corriendo]
                    self.imagen = pygame.transform.flip(self.imagen, self.direccion == -1, False)
                    self.imagen = pygame.transform.scale(self.imagen, (60, 160))
                else:
                    self.imagen = boss1_ataque_corriendo[self.frame_ataque_corriendo]
                    self.imagen = pygame.transform.flip(self.imagen, self.direccion == -1, False)
                    self.imagen = pygame.transform.scale(self.imagen, (60, 160))
        
            self.x += self.velocidad * self.direccion
            self.rect.x = self.x
        
            if self.rect.colliderect(jugador.rect):
                jugador.recibir_dano(2)  # El ataque corriendo hace 2 de daño al jugador
        
            if (self.direccion == -1 and self.x <= 0) or (self.direccion == 1 and self.x >= 962):
                self.atacando_corriendo = False
                self.velocidad = 0
                self.tiempo_quieto = self.tiempo_quieto_total
                self.cooldown_ataque_corriendo = random.randint(3000, 7000)  # Cooldown aleatorio de 3 a 7 segundos (en milisegundos)
                print(f"Boss1 quieto después de llegar al borde de la pantalla. Próximo ataque corriendo en {self.cooldown_ataque_corriendo / 1000} segundos")
    
        if self.tiempo_quieto > 0:
            self.tiempo_quieto -= 1
            if self.tiempo_quieto == 0:
                self.velocidad = self.velocidad_original
                print("Boss1 vuelve a moverse normalmente")
    def iniciar_cinematica(self):
        if not self.cinematica_mostrada:
            self.cinematica_activa = True
            self.frame_actual = 0
            self.contador_frames = 0
            print("Iniciando cinemática")
    def caminar(self, jugador_x):
        if self.caminando:
            self.contador_pasos += 1
            if self.contador_pasos >= self.frames_por_paso:
                self.contador_pasos = 0
                self.frame_caminar = (self.frame_caminar + 1) % len(boss1_caminar)
            
            # Ajusta la dirección según la posición del jugador
            if jugador_x < self.x:
                self.direccion = -1  # Moverse a la izquierda
                self.imagen = boss1_caminar[self.frame_caminar]
            else:
                self.direccion = 1  # Moverse a la derecha
                self.imagen = pygame.transform.flip(boss1_caminar[self.frame_caminar], True, False)
            
            # Mueve al jefe
            self.x += self.velocidad * self.direccion
            self.rect.x = self.x        
    def draw(self, screen, fondo):
        if self.cinematica_activa:
            screen.blit(fondo, (0, 0))  # Dibuja el fondo primero
            screen.blit(boss1_cinematica[self.frame_actual], (self.x, self.y))  # Dibuja la cinemática en la posición correcta
        else:
            screen.blit(self.imagen, self.rect)
    
    def dibujar_vida(self, screen):
        if self.mostrar_barra_vida:
            vida_actual = int((self.vida / self.vida_max) * self.largo_barra)
        
        # Calcula las posiciones para centrar la barra en la parte superior
            pos_x = (1022 - self.largo_barra) // 2
            pos_y = 10  # 10 píxeles desde la parte superior
        
        # Dibuja el fondo de la barra (rojo)
            pygame.draw.rect(screen, (255, 0, 0), (pos_x, pos_y, self.largo_barra, self.alto_barra))
        
        # Dibuja la vida actual (verde)
            pygame.draw.rect(screen, (0, 255, 0), (pos_x, pos_y, vida_actual, self.alto_barra))
        
        # Dibuja el borde de la barra (blanco)
            pygame.draw.rect(screen, (255, 255, 255), (pos_x, pos_y, self.largo_barra, self.alto_barra), self.borde_barra)
        
        # Dibuja el texto debajo de la barra
            font = pygame.font.SysFont("Arial", 24, bold=True)
            texto_vida = font.render(f"Boss HP: {self.vida} / {self.vida_max}", True, (255, 255, 255))
            text_rect = texto_vida.get_rect(midtop=(pos_x + self.largo_barra // 2, pos_y + self.alto_barra + 10))
            screen.blit(texto_vida, text_rect)
    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0
    def atacar(self, jugador):
        if not self.atacando and not self.atacando_corriendo and not self.tiempo_quieto:
            distancia = abs(self.x - jugador.x)
            if distancia <= self.distancia_ataque:
                self.atacando = True
                self.frame_ataque = 0
                self.contador_ataque = 0
                self.velocidad_original = self.velocidad  # Guarda la velocidad original
                self.velocidad = 0  # Establece la velocidad a 0 para que el Boss1 se quede quieto
                print("Boss1 atacando")
    
        if self.atacando:
            self.contador_ataque += 1
            if self.contador_ataque >= self.frames_por_ataque:
                self.contador_ataque = 0
                self.frame_ataque += 1
                if self.frame_ataque >= len(boss1_ataque):
                    self.atacando = False
                    self.frame_ataque = 0
                    self.velocidad = self.velocidad_original  # Restablece la velocidad original
                    jugador.recibir_dano(self.damage)
                    print(f"Jugador recibió {self.damage} de daño")
                else:
                    self.imagen = boss1_ataque[self.frame_ataque]
                    self.imagen = pygame.transform.flip(self.imagen, self.direccion == 1, False)
                    self.imagen = pygame.transform.scale(self.imagen, (80, 220))