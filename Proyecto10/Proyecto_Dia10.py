import pygame
import random
import math
from pygame import mixer
#Inicializar Pygame
pygame.init()
#Crear Pantalla
pantalla = pygame.display.set_mode((800,600))
#Titulo e icono
pygame.display.set_caption("Invación Alienigena")
icono = pygame.image.load("alien.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondod.png")

#agregar musica
mixer.music.load("musicafondo.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.2)

#Jugador
img_jugador = pygame.image.load("3d-rocket.png")
posicion_x = 368
posicion_y = 510
jugador_x_cambio = 0

#variables del enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("invasor.png"))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(100,300))
    enemigo_x_cambio.append(6)
    enemigo_y_cambio.append(20)

#variables de la bala
img_bala = pygame.image.load("bullet.png")
bala_x = 0
bala_y = 510
bala_x_cambio = 0
bala_y_cambio = 4
bala_visible = False

#variable puntaje
puntaje = 0
fuente = pygame.font.Font("freesansbold.ttf",32)
texto_x = 10
texto_y = 10

#texto final
fuente_final = pygame.font.Font("freesansbold.ttf",40)

def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255,255,255))
    pantalla.blit(mi_fuente_final,(200,200))
#función mostrar puntaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255,255,255))
    pantalla.blit(texto,(x,y))

#función de movimiento de jugador
def jugador(x,y):
    pantalla.blit(img_jugador, (x,y))

#función de movimiento del enemigo
def enemigo(x,y,ene):
    pantalla.blit(img_enemigo[ene], (x,y))

#función disparar bala
def disparar(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 14,y + 10))

#función detectar colisiones
def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1,2))
    if distancia < 30:
        return True
    else:
        return False


#Loop del juego
se_ejecuta = True
while se_ejecuta:
    #RGB
    pantalla.fill((203,144,228))

    #implementar fondo
    pantalla.blit(fondo, (0,0))

    #iterar eventos del jugador
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("sonido_disparo.mp3")
                sonido_bala.play()
                if not bala_visible:
                    bala_x = posicion_x
                    disparar(bala_x, bala_y)
        #Se soltó flecha?
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
    #modificar movimiento de jugador
    posicion_x += jugador_x_cambio
    #mantener dentro de bordes
    if posicion_x <= 0:
        jugador_x_cambio = 0
    elif posicion_x >= 736:
        posicion_x = 736

    #modificar posición enemigo
    for e in range(cantidad_enemigos):
        #fin del juego
        if enemigo_y[e] > 420:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break
        enemigo_x[e] += enemigo_x_cambio[e]
    #mantener dentro de bordes enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -1
            enemigo_y[e] += enemigo_y_cambio[e]
        # colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound("muerte.mp3")
            sonido_colision.play()
            bala_y = 510
            bala_visible = False
            puntaje += 1

            enemigo_x[e] = random.randint(0,736)
            enemigo_y[e] = random.randint(50,200)
        enemigo(enemigo_x[e], enemigo_y[e],e)

    #movimiento bala
    if bala_y <= -32:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar(bala_x,bala_y)
        bala_y -= bala_y_cambio


    jugador(posicion_x,posicion_y)
    mostrar_puntaje(texto_x,texto_y)
    #actualizar
    pygame.display.update()