import pygame
import random
import math

# Inicia pygame
pygame.init()

# Crea la pantalla
pantalla = pygame.display.set_mode((1280, 720))
se_ejecuta = True

# Titulo e icono
pygame.display.set_caption("Space invaders")
icono = pygame.image.load("icon.png")
pygame.display.set_icon(icono)

# Variables Jugador
imagen_jugador = pygame.image.load("nave.png")
jugador_x = 640
jugador_y = 640
jugador_x_cambio = 0
fondo = pygame.image.load("fondo3.jpg")


# Variables enemigo
imagen_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    imagen_enemigo.append(pygame.image.load("ovni.png"))
    enemigo_x.append(random.randint(0, 1216))
    enemigo_y.append(random.randint(64, 260))
    enemigo_x_cambio.append(0.4)
    enemigo_y_cambio.append(80)


# Variables proyectil
imagen_pro = pygame.image.load("laser.png")
pro_x = 0
pro_y = 640
pro_x_cambio = 0
pro_y_cambio = 3
pro_visible = False

# Puntaje
puntaje = 0


# Funcion jugador
def jugador(x, y):
    pantalla.blit(imagen_jugador, (x, y))


# Funcion enemigo
def enemigo(x, y, ene):
    pantalla.blit(imagen_enemigo[ene], (x, y))


# Funcion disparar proyectil
def disparar_pro(x, y):
    global pro_visible
    pro_visible = True
    pantalla.blit(imagen_pro, (x + 16, y + 10))


# Funcion detectar colisiones
def hay_colisiones(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if distancia < 27:
        return True
    else:
        return False


# Respawn enemigo
def respawn_enemigo():
    enemigo_x = random.randint(0, 1216)
    enemigo_y = random.randint(64, 260)
    return enemigo_x, enemigo_y


# Ciclo del juego
while se_ejecuta:

    # Color pantalla
    pantalla.blit(fondo, (0, 0))

    # Ciclo eventos
    for evento in pygame.event.get():
        # Evento cerrar por click
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento presionar tecla
        if evento.type == pygame.KEYDOWN:

            # Evento cerrar por tecla ESC
            if evento.key == pygame.K_ESCAPE:
                se_ejecuta = False

            # Evento presionar flecha
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.7
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.7

            # Evento disparo
            if evento.key == pygame.K_x:
                if not pro_visible:
                    pro_x = jugador_x
                    disparar_pro(pro_x, pro_y)

        # Evento soltar tecla
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Modificar ubicacion jugador
    jugador_x += jugador_x_cambio

    # Mantenar dentro de bordes jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 1216:
        jugador_x = 1216

    # Modificar ubicacion enemigo
    for e in range(cantidad_enemigos):
        enemigo_x[e] += enemigo_x_cambio[e]

    # Mantenar dentro de bordes enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.5
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 1216:
            enemigo_x_cambio[e] = -0.5
            enemigo_y[e] += enemigo_y_cambio[e]

        # Colision
        colision = hay_colisiones(enemigo_x[e], enemigo_y[e], pro_x, pro_y)
        if colision:
            pro_y = 640
            pro_visible = False
            puntaje += 1
            enemigo_x[e], enemigo_y[e] = respawn_enemigo()

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Movimiento proyectil
    if pro_y <= -32:
        pro_y = 640
        pro_visible = False
    if pro_visible:
        disparar_pro(pro_x, pro_y)
        pro_y -= pro_y_cambio

    jugador(jugador_x, jugador_y)

    # Actualizar
    pygame.display.update()
