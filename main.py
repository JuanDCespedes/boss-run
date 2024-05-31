import pygame
import sys
from imagenes1 import lobby
from fondo import *
from jugador import *

size = width, heigth = 1022, 588
screen = pygame.display.set_mode(size)


def main():
    pygame.init()
    
    fondo = Fondo()
    fondo_rect = fondo.lobby.get_rect()
    
    pj = Jugador()
    pj_rect = pj.jugador.get_rect()
    pj_rect.topleft = (0, 380)
        
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        pj.mover()
        
        screen.blit(fondo.lobby, fondo_rect)
        screen.blit(pj.jugador, pj_rect)
        
        fondo.animar_fondo()

        pygame.display.update()
        pygame.time.delay(100)
        
if __name__ == "__main__":
    main()