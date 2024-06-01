import pygame
import sys
from fondo import *
from jugador import *

#Tamaño de la ventana
size = width, heigth = 1022, 588
screen = pygame.display.set_mode(size)

#Funcion main
def main():
    pygame.init()
    
    #Instancia del jugador
    pj = Jugador()
    pj_rect = pj.jugador.get_rect()
    
    #Instancia del fondo
    fondo = Fondo(pj)
    fondo_rect = fondo.imagen_fondo.get_rect()
    
    #Instancias de los portales
    portal1 = Portal(fondo)
    portal1_rect = portal1.imagen_portal.get_rect()
    portal2 = Portal(fondo)
    portal2_rect = portal2.imagen_portal.get_rect()
    portal3 = Portal(fondo)
    portal3_rect = portal3.imagen_portal.get_rect()
    
    #Variables para el uso de coordenadas (para optimizacion de la generacion de codigo)
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    
    #Bucle principal para refrescar el juego
    while 1:
        #Logica de cierre de la ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #Llamado de todas las funciones necesarias
        pj.mover()
        pj.pegar()
        pj.saltar()
        pj_rect.topleft = (pj.x, pj.y)
        
        fondo.animar_fondo()
        fondo.cambiar_fondo()
        
        portal1.animar_portal()
        portal1_rect.topleft = (47, 314)
        portal2.animar_portal()
        portal2_rect.topleft = (385, 314)
        portal3.animar_portal()
        portal3_rect.topleft = (725, 314)

        #Impresion de los diferentes objetos sobre la pantalla
        screen.blit(fondo.imagen_fondo, fondo_rect)
        
        if fondo.num_fondo == 1:
            screen.blit(portal1.imagen_portal, portal1_rect)
            screen.blit(portal2.imagen_portal, portal2_rect)
            screen.blit(portal3.imagen_portal, portal3_rect)
        
        screen.blit(pj.jugador, pj_rect)
        
        #Impresion del sistema de coordenadas
        coords_text = font.render(f"Coordenadas: ({pj.x}, {pj.y})", True, (255, 255, 255))
        screen.blit(coords_text, (10, 10))

        #Timing de refresco de la pantalla
        pygame.display.update()
        pygame.time.delay(100)
        
if __name__ == "__main__":
    main()