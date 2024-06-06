import pygame
import sys
from fondo import *
from jugador import *
from boss1 import *
from boss2 import *
from boss3 import *

# Tamaño constante de la ventana de juego
size = width, height = 1022, 588
screen = pygame.display.set_mode(size)
BLACK = (0, 0, 0)

# Función de la lógica de la tienda
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

# Función principal del juego
def main():
    pygame.init()
    
    boss2 = None

    # Generación de instancias
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
    
    jefe3 = Jefe3(fondo)
    jefe3_rect = jefe3.jefe3.get_rect()
    
    lluvias = [Lluvia() for _ in range(5)]
    ola = Ola()
    
    # Coordenadas (para el desarrollo solamente)
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    boss1 = None
    primera_entrada_jefe1 = True
    boss1_muerto = False
    boss1_monedas_dadas = False
    boss3_muerto = False
    boss3_monedas_dadas = False
    
    tiempo_para_nueva_gota = pygame.USEREVENT + 1
    pygame.time.set_timer(tiempo_para_nueva_gota, 1500)
    
    # Bucle principal de refrescación del juego
    while True:
        # Sigue con vida?
        if pj.vida == 0:
            pj.game_over = True
        
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
            elif event.type == tiempo_para_nueva_gota:
                lluvias.append(Lluvia())
        
        clock.tick(10)  # Mantener 10 FPS
        
        # Llamado de las funciones necesarias
        # Funciones de movimiento de pj
        pj.mover()
        pj.pegar()
        pj.saltar()
        pj.morir()
        pj_rect.topleft = (pj.x, pj.y)
        
        # Funciones de refrescar pantalla
        fondo.animar_fondo()
        fondo.cambiar_fondo(boss1_muerto, boss3_muerto)
        fondo.pantalla_muerte()
        if boss1_muerto and fondo.num_fondo == 2:
            fondo.num_fondo = 0
            boss1 = None
            pj.x = 450
            pj.y = 450
            pj.altura_salto = 60
            print("Jugador vuelve al lobby")
        
        # Funciones del jefe 1
        if fondo.num_fondo == 2 and not fondo.transicion and not pj.game_over:
            if boss1 is None:
                boss1 = Boss1()
                print("Boss1 creado")

            if primera_entrada_jefe1:
                boss1.iniciar_cinematica()
                primera_entrada_jefe1 = False
                print("Primera entrada, iniciando cinemática")
            boss1.actualizar_cinematica()
            if boss1.cinematica_activa:
                screen.blit(fondo.imagen_fondo, fondo_rect)
                boss1.draw(screen, fondo.imagen_fondo)
                pygame.display.update()
                continue
            else:
                screen.blit(fondo.imagen_fondo, fondo_rect)
                screen.blit(pj.jugador, pj_rect)
                boss1.draw(screen, fondo.imagen_fondo)
                if not boss1.atacando_corriendo:
                    boss1.caminar(pj.x)
                boss1.atacar(pj)
                boss1.atacar_corriendo(pj)
                pj.aplicar_daño(boss1)
                boss1.dibujar_vida(screen)
                if boss1.vida <= 0:
                    boss1.morir()

                if boss1.esta_muerto() and not boss1_muerto:
                    boss1_muerto = True
                    
                if boss1_muerto and not boss1_monedas_dadas:
                    pj.vida = pj.vida_max
                    pj.monedas += 1
                    boss1_monedas_dadas = True
                    print("Jugador recupera vida y gana 1 moneda")
                    
        else:
            boss1 = None
            primera_entrada_jefe1 = True

        #Inicializar boss2 como None
        boss2 = None


        #Funciones del jefe 2 
        if fondo.num_fondo == 3 and not pj.game_over:

            if boss2 is None: 
                boss2 = Boss(400, 300)
                print("Boss2 creado")

            if boss2 is not None:
                boss2.dibujar(screen)
                boss2.mover()
                boss2.atacar(pj)
        
        else: 
            # si no estamos en la habitación del Boss2, asignar None al boss2 
            boss2 = None

        # Funciones de los portales
        portal1.animar_portal()
        portal1_rect.topleft = (47, 314)
        portal2.animar_portal()
        portal2_rect.topleft = (385, 314)
        portal3.animar_portal()
        portal3_rect.topleft = (725, 314)
        
        # Impresión de objetos en la pantalla
        screen.blit(fondo.imagen_fondo, fondo_rect)

        # Impresión de pantalla de muerte
        fade_surface = pygame.Surface((1022, 588))
        fade_surface.fill(BLACK)
        fade_surface.set_alpha(fondo.opacidad)
        screen.blit(fade_surface, (0, 0))
        
        if fondo.opacidad == 255:
            font1 = pygame.font.SysFont("Arial", 74)
            gameover_text = font1.render(f"GAME OVER", True, (135, 0, 0))
            screen.blit(gameover_text, (325, 230))
        
        if boss1 is not None and not boss1.cinematica_activa:
            boss1.draw(screen, fondo.imagen_fondo)
        if not (fondo.transicion and fondo.portal_usado):
            if fondo.num_fondo == 1 and not pj.game_over:
                if not boss1_muerto:
                    screen.blit(portal1.imagen_portal, portal1_rect)
                screen.blit(portal2.imagen_portal, portal2_rect)
                if not boss3_muerto:
                    screen.blit(portal3.imagen_portal, portal3_rect)
            screen.blit(pj.jugador, pj_rect)
        
        if fondo.num_fondo == 4 and not fondo.transicion and not pj.game_over:
            if jefe3.vida != 0:
                for lluvia in lluvias:
                    lluvia.gota_de_fuego()
                    lluvia_rect = lluvia.gota.get_rect(topleft=(lluvia.x, lluvia.y))
                    screen.blit(lluvia.gota, lluvia_rect)
                    if lluvia.y > height:
                        lluvias.remove(lluvia)
                    if pj_rect.colliderect(lluvia_rect):
                        pj.recibir_dano(1)
                        lluvias.remove(lluvia)
                jefe3_rect.topleft = (jefe3.xj3, jefe3.yj3)
                screen.blit(jefe3.jefe3, jefe3_rect)
                jefe3.entrada_jefe3()
                jefe3.estatico_jefe3()
                jefe3.ataque()
                if jefe3.contador_gj3 == 6 and jefe3.contador_j3 == 6:
                    ola = Ola()
                if jefe3.ataque_ola:
                    ola.ola_de_fuego()
                    ola_rect = ola.ola.get_rect(topleft=(ola.x, ola.y))
                    screen.blit(ola.ola, ola_rect)
                    if ola.x == -100:
                        jefe3.ataque_ola = False
                        del ola
                        jefe3.contador_x = 1
                    if pj_rect.colliderect(ola_rect):
                        pj.recibir_dano(1)
                        del ola
                        jefe3.ataque_ola = False
                        jefe3.contador_x = 1
                if jefe3.ataque_llama:
                    if jefe3.contador_gj3 == 6 and jefe3.contador_j3 == 14:
                        jefe3.contador_x = 0
                        jefe3.ataque_llama = False
                        jefe3.contador_j3 = 0
                        jefe3.contador_gj3 = 1
                if jefe3.ataque_llama:
                    if pj_rect.colliderect(jefe3_rect.inflate(170, 0)):
                        pj.recibir_dano(1)
                jefe3.dibujar_vida(screen)
                jefe3.rect = jefe3.jefe3.get_rect(topleft=(jefe3.xj3, jefe3.yj3))
                pj.aplicar_daño(jefe3)
            
            elif jefe3.vida <= 0:
                if jefe3.contador_mj3 == 3:
                    jefe3.yj3 = 525
                jefe3.morir()
                jefe3_rect.topleft = (jefe3.xj3, jefe3.yj3)
                screen.blit(jefe3.jefe3, jefe3_rect)
            
            if jefe3.esta_muerto() and not boss3_muerto:
                boss3_muerto = True
            if boss3_muerto and not boss3_monedas_dadas:
                pj.vida = pj.vida_max
                pj.monedas += 1
                boss3_monedas_dadas = True
                print("Jugador recupera vida y gana 1 moneda")
        
                fondo.num_fondo = 0
                jefe3 = None
                pj.x = 450
                pj.y = 450
                print("Jugador vuelve al lobby")
        
        # Coordenadas
        coords_text = font.render(f"Coordenadas: ({pj.x}, {pj.y})", True, (255, 255, 255))
        screen.blit(coords_text, (250, 10))

        pj.dibujar_vida(screen)
        
        # Lógica de ESC
        teclas = pygame.key.get_pressed()
        if teclas[K_ESCAPE]:
            if pj.game_over:
                fondo.num_fondo = 0
                pj.vida = pj.vida_max
                pj.game_over = False
                fondo.opacidad = 0
                pj.muerto = False
                pj.contador_muerte = 0
                pj.altura_salto = 60
            if fondo.num_fondo == 4 and jefe3.vida == 0:
                pj.vida = pj.vida_max
                fondo.num_fondo = 0
        
        pygame.display.update()
        pygame.time.delay(100)
        
if __name__ == "__main__":
    main()
