from imagenes1 import *

#Clase encargada del jefe 3
class Jefe3():
    #Inicialización de variables
    def __init__(self):
        self.contador_gj3 = 0
        self.contador_aj3 = 0
        self.tamano = 120
        self.jefe3 = jefe3_entrada[self.contador_aj3]
        self.jefe3 = pygame.transform.scale(self.jefe3, (self.tamano, self.tamano))
        self.xj3 = -30
        self.yj3 = 450
        self.distancia = 10

    #Función encargada de la animación de entrada del jefe 3
    def entrada_jefe3(self):
        if self.contador_gj3 == 0:    
            if self.contador_aj3 == 7:
                self.jefe3 = jefe3_entrada[self.contador_aj3]
                self.yj3 = 450
                self.contador_gj3 += 1
            elif 1 <= self.contador_aj3 <= 3:
                self.jefe3 = jefe3_entrada[self.contador_aj3]
                self.xj3 += self.distancia
                self.yj3 -= self.distancia
                self.contador_aj3 += 1
            elif 4 <= self.contador_aj3 <= 6:
                self.jefe3 = jefe3_entrada[self.contador_aj3]
                self.xj3 += self.distancia
                self.yj3 += self.distancia
                self.contador_aj3 += 1
            elif self.contador_aj3 == 0:
                self.contador_aj3 += 1
            self.jefe3 = pygame.transform.scale(self.jefe3, (self.tamano, self.tamano))

    #Función encargada de la animación cuando el jefe esta quieto
    def estatico_jefe3(self):
        if self.contador_gj3 == 1:
            