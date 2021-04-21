import pygame, sys
from pygame.locals import *
import paleta

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Nuestro primer juego!")

screen.fill(paleta.blanco)
rectangulo = pygame.draw.rect(screen, paleta.azul, (100, 50, 100, 50)) #primer parametro es x y el segundo y (posicion), el tecero el largo en horizontal y el cuarto el alto
linea = pygame.draw.line(screen, paleta.verde, (100, 167), (199, 104), 10)  # 100 donde empieza, 199 donde acaba, 104 inclina a la izquierda o derecha, y el ultimo el grosor
circulo = pygame.draw.circle(screen, paleta.negro, (122, 250), 20, 0)  #122 la x, 250 la y, el 20 el radio, y el 0 el relleno (widht)
elipse = pygame.draw.ellipse(screen, paleta.rojo, (275, 200, 40, 80), 10) #275 la x, 200 la y, 40 el tamaño en el eje x, y el 60 el tamaño en el eje y, el ultimo el grueso (puedes no ponerlo)

puntos = [(100, 300), (100, 100), (150, 100)] #cada una de las tuplas son los puntos de la figura (3 tuplas --> triangulo, 5 --> pentagono...)
pygame.draw.polygon(screen, paleta.rojo, puntos, 1) # el 8 es el grueso

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update() # sin esto, aunque pongas el color de blanco, se queda negro (color default)





