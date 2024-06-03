from imagenes1 import *
from fondo import *
import random

#Clase encargada del jefe 3
class Jefe3():
    #Inicialización de variables
    def __init__(self, fondos):
        self.contador_gj3 = 0
        self.contador_j3 = 0
        self.jefe3 = jefe3_entrada[self.contador_j3]
        self.xj3 = -30
        self.yj3 = 430
        self.distancia = 10
        self.fondos = fondos
        self.contador_aj3 = 0
        self.ataque_ola = False
        self.contador_x = 0
        self.ataque_llama = False

    #Función encargada de la animación de entrada del jefe 3
    def entrada_jefe3(self):
        if self.contador_gj3 == 0 and self.fondos.num_fondo == 4:    
            if self.contador_j3 == 7:
                self.yj3 = 430
                self.contador_gj3 += 1
                self.contador_j3 = 0
            elif 1 <= self.contador_j3 <= 3:
                self.xj3 += self.distancia
                self.yj3 -= self.distancia
                self.contador_j3 += 1
            elif 4 <= self.contador_j3 <= 6:
                self.xj3 += self.distancia
                self.yj3 += self.distancia
                self.contador_j3 += 1
            elif self.contador_j3 == 0:
                self.contador_j3 += 1
            self.jefe3 = jefe3_entrada[self.contador_j3]

    #Función encargada de la animación cuando el jefe esta quieto
    def estatico_jefe3(self):
        if 1 <= self.contador_gj3 <= 5:
            if self.contador_j3 == 5:
                self.contador_j3 = 0
                self.contador_gj3 += 1
            else:
                self.contador_j3 += 1
            self.jefe3 = jefe3_estatico[self.contador_j3]
    
    #Funcion encargada de la animacion de ataque del jefe
    def ataque(self):
        if self.contador_gj3 == 6 and self.contador_x == 0:
            if self.contador_j3 == 7:
                self.contador_gj3 = 1
                self.contador_j3 = 0
                self.ataque_ola = True
            else:
                self.contador_j3 += 1
            self.jefe3 = jefe3_ataque2[self.contador_j3]
        if self.contador_gj3 == 6 and self.contador_x == 1:
            if self.contador_gj3 == 6 and self.contador_x == 1 and self.contador_j3 == 0:
                self.ataque_llama = True
            if self.contador_j3 == 14:
                self.contador_gj3 = 1
                self.contador_j3 = 0
            else:
                self.contador_j3 += 1
            self.jefe3 = jefe3_ataque1[self.contador_j3]

#Clase encargada de la lluvia de fuegod el jefe 3
class Lluvia():
    #Inicializacion de variables
    def __init__(self):
        self.x = random.randint(-90, 960)
        self.y = -250
        self.contador_l = 0
        self.gota = gotadefuego[self.contador_l]
    
    #Funcion encargada de animar cada gota de fuego
    def gota_de_fuego(self):
        if self.contador_l == 11:
            self.contador_l = 0
        else:
            self.contador_l += 1
        self.gota = gotadefuego[self.contador_l]
        self.y += 25

#Clase encargada de la ola de fuego del jefe 3
class Ola():
    #Inicializacion de variables
    def __init__(self):
        self.x = 1000
        self.y = 528
        self.contador_o = 0
        self.ola = oladefuego[self.contador_o]
    
    #Funcion encargada de animar la ola de fuego
    def ola_de_fuego(self):
        if self.contador_o == 5:
            self.contador_o = 0
        else:
            self.contador_o += 1
        self.ola = oladefuego[self.contador_o]
        self.x -= 50