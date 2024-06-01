import pygame
import sys
from fondo import *
from jugador import *

size = width, heigth = 1022, 588
screen = pygame.display.set_mode(size)


def main():
    pygame.init()
    
    pj = Jugador()
    pj_rect = pj.jugador.get_rect()
    
    fondo = Fondo(pj)
    fondo_rect = fondo.imagen.get_rect()
    
    pygame.font.init()
    font = pygame.font.Font(None, 36)
        
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        pj.mover()
        pj.pegar()

        pj_rect.topleft = (pj.x, pj.y)
        screen.blit(fondo.imagen, fondo_rect)
        screen.blit(pj.jugador, pj_rect)
        
        coords_text = font.render(f"Coordenadas: ({pj.x}, {pj.y})", True, (255, 255, 255))
        screen.blit(coords_text, (10, 10))
        
        fondo.animar_fondo()
        fondo.cambiar_fondo()

        pygame.display.update()
        pygame.time.delay(100)
        
if __name__ == "__main__":
    main()