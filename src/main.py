import pygame
import random

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
imagen_enemigo = pygame.image.load("ovni.png")
enemigo_x = random.randint(0, 1216)
enemigo_y = random.randint(64, 260)
enemigo_x_cambio = 0.6
enemigo_y_cambio = 80

# Variables proyectil
imagen_pro = pygame.image.load("laser.png")
pro_x = 0
pro_y = 640
pro_x_cambio = 0
pro_y_cambio = 1
pro_visible = False


# Funcion jugador
def jugador(x, y):
    pantalla.blit(imagen_jugador, (x, y))


# Funcion enemigo
def enemigo(x, y):
    pantalla.blit(imagen_enemigo, (x, y))


# Funcion disparar proyectil
def disparar_pro(x, y):
    global pro_visible
    pro_visible = True
    pantalla.blit(imagen_pro, (x + 16, y + 10))


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
                disparar_pro(jugador_x, pro_y)

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
    enemigo_x += enemigo_x_cambio

    # Movimiento proyectil
    if pro_visible:
        disparar_pro(jugador_x, pro_y)
        pro_y -= pro_y_cambio

    # Mantenar dentro de bordes enemigo
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.5
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 1216:
        enemigo_x_cambio = -0.5
        enemigo_y += enemigo_y_cambio

    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)

    # Actualizar
    pygame.display.update()
