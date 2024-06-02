import pygame
import sys
from fondo import *
from jugador import *

#Tamaño constante de la ventaja de juego
size = width, height = 1022, 588
screen = pygame.display.set_mode(size)

#Funcion de la logica de la tienda
def mostrar_dialogo_tienda(screen, pj):
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, width, height))  # Fondo gris claro
    font = pygame.font.SysFont("Times new roman", 48)  # Fuente más grande

    textos = [
        ("Bienvenido a la tienda, ¿Qué deseas mejorar?", (width // 2, 100)),
        (f"HP         {pj.mejoras['HP']}/3", (width // 2, 200)),
        (f"ATK       {pj.mejoras['ATK']}/3", (width // 2, 300)),
        (f"VEL       {pj.mejoras['VEL']}/3", (width // 2, 400)),
        (f"Monedas: {pj.monedas}", (width // 2, 500))
    ]

    for texto, pos in textos:
        text_surface = font.render(texto, True, (0, 0, 0))  # Texto negro
        text_rect = text_surface.get_rect(center=pos)
        screen.blit(text_surface, text_rect)

    pygame.display.update()  # Actualizar la pantalla después de dibujar

    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    esperando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic izquierdo
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 350 <= mouse_x <= 650:
                        if 175 <= mouse_y <= 225:
                            pj.mejorar("HP")
                        elif 275 <= mouse_y <= 325:
                            pj.mejorar("ATK")
                        elif 375 <= mouse_y <= 425:
                            pj.mejorar("VEL")

        # Volver a dibujar para actualizar las estadísticas
        pygame.draw.rect(screen, (200, 200, 200), (0, 0, width, height))
        for texto, pos in textos:
            if "HP" in texto:
                texto = f"HP         {pj.mejoras['HP']}/3"
            elif "ATK" in texto:
                texto = f"ATK       {pj.mejoras['ATK']}/3"
            elif "VEL" in texto:
                texto = f"VEL       {pj.mejoras['VEL']}/3"
            elif "Monedas" in texto:
                texto = f"Monedas: {pj.monedas}"
            
            text_surface = font.render(texto, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=pos)
            screen.blit(text_surface, text_rect)

        pygame.display.update()

#Funcion principal del juego
def main():
    pygame.init()
    
    #Generacion de instancias
    pj = Jugador()
    pj_rect = pj.jugador.get_rect()
    
    fondo = Fondo(pj)
    fondo_rect = fondo.imagen_fondo.get_rect()
    
    portal1 = Portal(fondo)
    portal1_rect = portal1.imagen_portal.get_rect()
    portal2 = Portal(fondo)
    portal2_rect = portal2.imagen_portal.get_rect()
    portal3 = Portal(fondo)
    portal3_rect = portal3.imagen_portal.get_rect()
    
    #Coordenadas (para el desarrollo solamente)
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    #Bucle principal de refrezcacion del juego
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print(f"Posición del jugador: ({pj.x}, {pj.y})")
                    print(f"Fondo: {fondo.num_fondo}")
                    if isinstance(fondo, Fondo) and fondo.num_fondo == 0 and 690 <= pj.x <= 780 and pj.y == 450:
                        print("¡Condición cumplida! Mostrando diálogo...")
                        mostrar_dialogo_tienda(screen, pj)
                        continue
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    x, y = event.pos
                    if 320 <= x <= 420 and 240 <= y <= 320:  
                        if pj.monedas > 0 and pj.hp < 3:
                            pj.monedas -= 1
                            pj.hp += 1
                    elif 320 <= x <= 420 and 320 <= y <= 400: 
                        if pj.monedas > 0 and pj.atk < 3:
                            pj.monedas -= 1
                            pj.atk += 1
                    elif 320 <= x <= 420 and 400 <= y <= 480: 
                        if pj.monedas > 0 and pj.vel < 3:
                            pj.monedas -= 1
                            pj.vel += 1
        pygame.display.update()
        clock.tick(10)  # Mantener 10 FPS
        #Llamado de las funciones necesarias
        pj.mover()
        pj.pegar()
        pj.saltar()
        pj.morir()
        pj_rect.topleft = (pj.x, pj.y)
        
        fondo.animar_fondo()
        fondo.cambiar_fondo()
        
        portal1.animar_portal()
        portal1_rect.topleft = (47, 314)
        portal2.animar_portal()
        portal2_rect.topleft = (385, 314)
        portal3.animar_portal()
        portal3_rect.topleft = (725, 314)

        #Impresion de objetos en la pantalla
        screen.blit(fondo.imagen_fondo, fondo_rect)
        if fondo.num_fondo == 1:
            screen.blit(portal1.imagen_portal, portal1_rect)
            screen.blit(portal2.imagen_portal, portal2_rect)
            screen.blit(portal3.imagen_portal, portal3_rect)
        screen.blit(pj.jugador, pj_rect)
        
        #Coordenadas
        coords_text = font.render(f"Coordenadas: ({pj.x}, {pj.y})", True, (255, 255, 255))
        screen.blit(coords_text, (250, 10))

        pj.dibujar_vida(screen)
        
        #Logica de refrezco de pantalla
        pygame.display.update()
        pygame.time.delay(100)
        
if __name__ == "__main__":
    main()