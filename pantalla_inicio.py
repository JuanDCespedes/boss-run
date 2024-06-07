import pygame
from pygame.locals import *

class PantallaInicio:
    def __init__(self, screen):
        self.screen = screen
        self.imagen_fondo_original = pygame.image.load("imagenes/portada.png")  # Reemplaza con la ruta de tu imagen de portada
        self.imagen_fondo = self.escalar_imagen(self.imagen_fondo_original, self.screen.get_size())

        self.opcion_seleccionada = 0
        self.opciones = ["Jugar", "Créditos"]
        self.font = pygame.font.Font(None, 36)
        self.creditos = ["Juan Diego Cespedes", "Juan David Avila", "David Eduardo Muñoz"]
    def escalar_imagen(self, imagen, dimensiones):
        return pygame.transform.scale(imagen, dimensiones)


    def mostrar_pantalla_inicio(self):
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.opcion_seleccionada = (self.opcion_seleccionada - 1) % len(self.opciones)
                    elif event.key == K_DOWN:
                        self.opcion_seleccionada = (self.opcion_seleccionada + 1) % len(self.opciones)
                    elif event.key == K_RETURN:
                        if self.opcion_seleccionada == 0:
                            pygame.mixer.init()
                            pygame.mixer.music.load("sonido/musica/0.mp3")
                            pygame.mixer.music.set_volume(0.5)
                            pygame.mixer.music.play(-1) 
                            return  # Regresar al juego principal
                        elif self.opcion_seleccionada == 1:
                            self.mostrar_creditos()

            self.screen.blit(self.imagen_fondo, (0, 0))

            for i, opcion in enumerate(self.opciones):
                texto = self.font.render(opcion, True, (255, 255, 255))
                if i == self.opcion_seleccionada:
                    texto = self.font.render(opcion, True, (255, 0, 0))
                self.screen.blit(texto, (100, 200 + i * 50))

            pygame.display.flip()

    def mostrar_creditos(self):
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return  # Regresar a la pantalla de inicio

            self.screen.fill((0, 0, 0))

            for i, nombre in enumerate(self.creditos):
                texto = self.font.render(nombre, True, (255, 255, 255))
                self.screen.blit(texto, (100, 100 + i * 50))

            pygame.display.flip()