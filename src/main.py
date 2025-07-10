import pygame

# Inicia pygame
pygame.init()

# Crea la pantalla
pantalla = pygame.display.set_mode((1280, 720))
se_ejecuta = True

# Titulo e icono
pygame.display.set_caption("Space invaders")
icono = pygame.image.load("icon.png")
pygame.display.set_icon(icono)

# Jugador
imagen_jugador = pygame.image.load("nave.png")
jugador_x = 640
jugador_y = 656
jugador_x_cambio = 0


def jugador(x, y):
    pantalla.blit(imagen_jugador, (x, y))


# Ciclo del juego
while se_ejecuta:

    # Color pantalla
    pantalla.fill((11, 2, 57))

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
                jugador_x_cambio = -0.6
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.6

        # Evento soltar tecla
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Modificar ubicacion
    jugador_x += jugador_x_cambio

    # Mantenar dentro de bordes
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 1216:
        jugador_x = 1216

    jugador(jugador_x, jugador_y)

    # Actualizar
    pygame.display.update()
