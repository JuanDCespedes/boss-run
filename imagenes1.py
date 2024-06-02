#Archivo dedicado a agrupar las imagenes para un uso mas optimo de estas mismas
import pygame

lobby = [
    pygame.image.load("imagenes/lobby/0.png"),
    pygame.image.load("imagenes/lobby/1.png"),
    pygame.image.load("imagenes/lobby/2.png"),
    pygame.image.load("imagenes/lobby/3.png"),
    pygame.image.load("imagenes/lobby/4.png"),
    pygame.image.load("imagenes/lobby/5.png"),
    pygame.image.load("imagenes/lobby/6.png"),
    pygame.image.load("imagenes/lobby/7.png"),
    pygame.image.load("imagenes/lobby/8.png"),
    pygame.image.load("imagenes/lobby/9.png"),
    pygame.image.load("imagenes/lobby/10.png"),
    pygame.image.load("imagenes/lobby/11.png"),
    pygame.image.load("imagenes/lobby/12.png"),
    pygame.image.load("imagenes/lobby/13.png"),
    pygame.image.load("imagenes/lobby/14.png"),
    pygame.image.load("imagenes/lobby/15.png"),
    pygame.image.load("imagenes/lobby/16.png"),
    pygame.image.load("imagenes/lobby/17.png"),
    pygame.image.load("imagenes/lobby/18.png"),
    pygame.image.load("imagenes/lobby/19.png"),
    pygame.image.load("imagenes/lobby/20.png"),
    pygame.image.load("imagenes/lobby/21.png"),
    pygame.image.load("imagenes/lobby/22.png"),
    pygame.image.load("imagenes/lobby/23.png"),
    pygame.image.load("imagenes/lobby/24.png"),
    pygame.image.load("imagenes/lobby/25.png"),
    pygame.image.load("imagenes/lobby/26.png"),
    pygame.image.load("imagenes/lobby/27.png"),
    pygame.image.load("imagenes/lobby/28.png"),
    pygame.image.load("imagenes/lobby/29.png"),
    pygame.image.load("imagenes/lobby/30.png"),
    pygame.image.load("imagenes/lobby/31.png")
]

jugador_caminar = [
    pygame.image.load("imagenes/caminar/0.png"),
    pygame.image.load("imagenes/caminar/1.png"),
    pygame.image.load("imagenes/caminar/2.png"),
    pygame.image.load("imagenes/caminar/3.png"),
    pygame.image.load("imagenes/caminar/4.png"),
    pygame.image.load("imagenes/caminar/5.png"),
    pygame.image.load("imagenes/caminar/6.png"),
    pygame.image.load("imagenes/caminar/7.png")
]

jugador_pegar = [
    pygame.image.load("imagenes/pegar/0.png"),
    pygame.image.load("imagenes/pegar/1.png"),
    pygame.image.load("imagenes/pegar/2.png")
]

portal = [
    pygame.image.load("imagenes/portal/0.png"),
    pygame.image.load("imagenes/portal/1.png"),
    pygame.image.load("imagenes/portal/2.png"),
    pygame.image.load("imagenes/portal/3.png"),
    pygame.image.load("imagenes/portal/4.png"),
    pygame.image.load("imagenes/portal/5.png")
]

jugador_saltar = [
    pygame.image.load("imagenes/saltar/0.png"),
    pygame.image.load("imagenes/saltar/1.png"),
    pygame.image.load("imagenes/saltar/2.png"),
    pygame.image.load("imagenes/saltar/3.png"),
    pygame.image.load("imagenes/saltar/4.png")
]

jugador_morir = [
    pygame.image.load("imagenes/morir/0.png"),
    pygame.image.load("imagenes/morir/1.png"),
    pygame.image.load("imagenes/morir/2.png"),
    pygame.image.load("imagenes/morir/3.png"),
    pygame.image.load("imagenes/morir/4.png"),
    pygame.image.load("imagenes/morir/5.png")
]

pantalla_carga=pygame.image.load("imagenes/pantallacarga.jpg")
pantalla_carga=pygame.transform.scale(pantalla_carga, (1022, 588))

boss1_cinematica = [
    pygame.image.load("imagenes/boss1/cinematica/cine1.png"),
    pygame.image.load("imagenes/boss1/cinematica/cine2.png"),
    pygame.image.load("imagenes/boss1/cinematica/cine3.png"),
    pygame.image.load("imagenes/boss1/cinematica/cine4.png"),
    pygame.image.load("imagenes/boss1/cinematica/cine5.png"),
    pygame.image.load("imagenes/boss1/cinematica/cine6.png"),
    pygame.image.load("imagenes/boss1/cinematica/cine7.png"),
    pygame.image.load("imagenes/boss1/cinematica/cine8.png"),
    pygame.image.load("imagenes/boss1/cinematica/cine9.png"),
    pygame.image.load("imagenes/boss1/cinematica/cine10.png"),
    pygame.image.load("imagenes/boss1/cinematica/cine11.png"),
    pygame.image.load("imagenes/boss1/cinematica/cine12.png"),
    pygame.image.load("imagenes/boss1/cinematica/cine13.png")
]
for i in range(len(boss1_cinematica)):
    boss1_cinematica[i] = pygame.transform.flip(boss1_cinematica[i], True, False)
    boss1_cinematica[i] = pygame.transform.scale(boss1_cinematica[i], (200, 200))
boss1_imagen=pygame.image.load("imagenes/boss1/cinematica/cine13.png")
boss1_imagen = pygame.transform.flip(boss1_imagen, True, False)  # Voltear horizontalmente
boss1_imagen = pygame.transform.scale(boss1_imagen, (200, 200))

jefe3_entrada = [
    pygame.image.load("imagenes/boss3/entrada/0.png"),
    pygame.image.load("imagenes/boss3/entrada/1.png"),
    pygame.image.load("imagenes/boss3/entrada/2.png"),
    pygame.image.load("imagenes/boss3/entrada/3.png"),
    pygame.image.load("imagenes/boss3/entrada/4.png"),
    pygame.image.load("imagenes/boss3/entrada/5.png"),
    pygame.image.load("imagenes/boss3/entrada/6.png"),
    pygame.image.load("imagenes/boss3/entrada/7.png"),
]