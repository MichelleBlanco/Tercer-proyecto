import pygame
import threading
import time
import random
import subprocess

# Inicializar Pygame y el módulo de sonido
pygame.init()
pygame.mixer.init()

# Cargar y reproducir la música de fondo
pygame.mixer.music.load("espacio.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

# Configuración de la pantalla
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

ANCHO, ALTO = 1300, 650
ventana = pygame.display.set_mode((ANCHO, ALTO))


# Fondo
fondo = pygame.image.load("espacio.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))


# Cargar la imagen del ícono
icon = pygame.image.load("conejo.ico")
pygame.display.set_icon(icon)
pygame.display.set_caption("Scape The Quest")

# Cargar la imagen del jugador
image_jugador = pygame.image.load("astronauta.png")
image_jugador = pygame.transform.scale(image_jugador, (45, 45))
image_jugador_rect = image_jugador.get_rect()
image_jugador_rect.topleft = (screen_width // 2, screen_height // 2)

# Cargar la imagen de los obstáculos
image = pygame.image.load('cohete.png')
image = pygame.transform.scale(image, (90, 30))

# Crear los rectángulos de los tres obstáculos y posicionarlos
def crear_obstaculos():
    """Crea una lista de rectángulos que representan los obstáculos en la pantalla del juego.
    La función genera una lista de obstáculos y los posiciona verticalmente 
    en el eje y, con una separación decreciente entre ellos, simulando bloques 
    alineados. La posición de cada obstáculo se calcula a partir de una posición base 
    en la pantalla.

    Args:
        None

    Returns:
        lista: Una lista de objetos Rect que representan los obstáculos en la pantalla.
    """
    obstaculos = []
    for i in range(5):
        image_rect = image.get_rect()
        image_rect.y = screen_height // 3 - (150 - (i * 90))  # Posicionar cada tronco
        obstaculos.append(image_rect)
    return obstaculos

obstaculos = crear_obstaculos()

# Crear la "Meta" en la parte superior de la pantalla
meta_rect = pygame.Rect((ANCHO // 2 - 50, 10), (100, 40))

# Variables de movimiento
move_speed_1 = 2
move_speed_2 = 5  # Velocidad diferente para el segundo tronco
move_speed_3 = 4  # Velocidad diferente para el tercer tronco
move_speed_4 = 7
move_speed_5 = 6

moving_right_1 = True  # Dirección inicial para el primer tronco
moving_right_2 = False  # Dirección inicial para el segundo tronco
moving_right_3 = True   # Dirección inicial para el tercer tronco
moving_right_4 = False
moving_right_5 = True
pause = False

# Función para mover los troncos
def move_obstacles():
    """Mueve los rectángulos que representan los obstáculos en la pantalla de izquierda a derecha
    o viceversa, de acuerdo con la dirección actual de cada obstáculo.
    La función utiliza varias variables globales para manejar la posición y el estado de movimiento 
    de cada obstáculo. Cada obstáculo se mueve a una velocidad definida y rebota al alcanzar 
    los bordes de la pantalla, cambiando su dirección de movimiento.    
    La función se ejecuta en un bucle infinito, actualizando la posición de cada obstáculo 
    mientras `pause` sea False. Cada obstáculo cambia de dirección al alcanzar el borde izquierdo 
    o derecho de la pantalla.

    Args:
        None
    
    Returns: None.
    """
    global moving_right_1, moving_right_2, moving_right_3, moving_right_4, moving_right_5, obstaculos, pause
    while True:
        if not pause:
            # Mover el primer tronco
            if moving_right_1:
                obstaculos[0].x += move_speed_1
                if obstaculos[0].right >= screen_width:
                    moving_right_1 = False
            else:
                obstaculos[0].x -= move_speed_1
                if obstaculos[0].left <= 0:
                    moving_right_1 = True

            # Mover el segundo tronco en dirección opuesta al primero
            if moving_right_2:
                obstaculos[1].x += move_speed_2  # Mover hacia la derecha
                if obstaculos[1].right >= screen_width:
                    moving_right_2 = False
            else:
                obstaculos[1].x -= move_speed_2  # Mover hacia la izquierda
                if obstaculos[1].left <= 0:
                    moving_right_2 = True

            # Mover el tercer tronco en la misma dirección que el primero
            if moving_right_3:
                obstaculos[2].x += move_speed_3
                if obstaculos[2].right >= screen_width:
                    moving_right_3 = False
            else:
                obstaculos[2].x -= move_speed_3
                if obstaculos[2].left <= 0:
                    moving_right_3 = True
            
            if moving_right_4:
                obstaculos[3].x += move_speed_4
                if obstaculos[3].right >= screen_width:
                    moving_right_4 = False
            else:
                obstaculos[3].x -= move_speed_4
                if obstaculos[3].left <= 0:
                    moving_right_4 = True

            if moving_right_5:
                obstaculos[4].x += move_speed_5
                if obstaculos[4].right >= screen_width:
                    moving_right_5 = False
            else:
                obstaculos[4].x -= move_speed_5
                if obstaculos[4].left <= 0:
                    moving_right_5 = True

            # Tiempo de pausa variable
            time.sleep(random.uniform(0.01, 0.03))  # Pausa aleatoria entre 10ms y 30ms

# Crear y comenzar el hilo para mover los obstáculos
move_thread = threading.Thread(target=move_obstacles)
move_thread.daemon = True
move_thread.start()

# Función para reiniciar el juego
def reiniciar_juego():
    """ Reinicia el estado del juego, colocando al jugador en su posición inicial, 
    restableciendo los obstáculos y configurando la dirección de movimiento inicial de cada obstáculo.

    Args:
        None

    Returns: None.
    """
    global image_jugador_rect, obstaculos, moving_right_1, moving_right_2, moving_right_3, moving_right_4, moving_right_5
    image_jugador_rect.topleft = (screen_width // 2, screen_height // 2)  # Reiniciar posición del jugador
    obstaculos = crear_obstaculos()  # Reiniciar obstáculos
    moving_right_1 = True
    moving_right_2 = False
    moving_right_3 = True
    moving_right_4 = False
    moving_right_5 = True

# Bucle principal de Pygame
running = True
perdiendo = False
ganaste = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if perdiendo and event.key == pygame.K_RETURN:  # Reiniciar al presionar Enter si perdió
                reiniciar_juego()
                perdiendo = False
                ganaste = False

    keys = pygame.key.get_pressed()

     # Mover el jugador
    if not perdiendo and not ganaste:  # Solo mover si no ha perdido ni ha ganado
        if keys[pygame.K_LEFT]:
            image_jugador_rect.x -= move_speed_1
        if keys[pygame.K_RIGHT]:
            image_jugador_rect.x += move_speed_1
        if keys[pygame.K_UP]:
            image_jugador_rect.y -= move_speed_1
        if keys[pygame.K_DOWN]:
            image_jugador_rect.y += move_speed_1

    # Evitar que el jugador salga de la pantalla
    image_jugador_rect.clamp_ip(ventana.get_rect())

    # Verificar colisiones
    if any(obstacle.colliderect(image_jugador_rect) for obstacle in obstaculos):
        perdiendo = True

    # Verificar si el jugador alcanzó la meta
    if meta_rect.colliderect(image_jugador_rect):
        ganaste = True

    ventana.blit(fondo, (0, 0))

    # Dibujar la meta
    pygame.draw.rect(ventana, (255, 255, 0), meta_rect)
    font_meta = pygame.font.Font(None, 30)
    text_meta = font_meta.render("Meta", True, (0, 0, 0))
    ventana.blit(text_meta, (meta_rect.x + 15, meta_rect.y + 5))

    if ganaste:
       running = False
       subprocess.Popen(["python", "espacio.py"])
       subprocess.Popen(["python", "espacio_nivel2.py"])

    elif perdiendo:
        running = False
        subprocess.Popen(["python", "menu.py"]) 
    else:
        # Dibujar los obstáculos y el jugador si no ha ganado ni perdido
        for obstaculo in obstaculos:
            ventana.blit(image, obstaculo)
        ventana.blit(image_jugador, image_jugador_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
