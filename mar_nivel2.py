import pygame
import threading
import time
import random
import subprocess

# Inicializar Pygame y el módulo de sonido
pygame.init()
pygame.mixer.init()

# Cargar y reproducir la música de fondo
pygame.mixer.music.load("mar1.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1.0)

# Configuración de la pantalla
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

ANCHO, ALTO = 1300, 650
ventana = pygame.display.set_mode((ANCHO, ALTO))

# Fondo
fondo = pygame.image.load("mar.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Cargar la imagen del jugador
image_jugador = pygame.image.load("pulpo.png")
image_jugador = pygame.transform.scale(image_jugador, (40, 40))
image_jugador_rect = image_jugador.get_rect()
image_jugador_rect.topleft = (screen_width // 2, screen_height // 2)

# Cargar la imagen de los obstáculos
image = pygame.image.load('tiburon.png')
image = pygame.transform.scale(image, (90, 40))

# Crear los rectángulos de los obstáculos y posicionarlos
def crear_obstaculos():
    """Crea una lista de rectángulos que representan obstáculos en dos columnas y los posiciona
    en una pantalla dividida en zonas izquierda y derecha, con un espaciamiento vertical y
    horizontal predeterminado.

    Args:
        None

    Returns:
        lista: Lista de rectángulos pygame.Rect que representan los obstáculos en pantalla.
    """
    obstaculos = []
    columna_espaciado = 150  # Espacio horizontal entre las dos columnas de obstáculos

    # Primera columna de obstáculos (lado izquierdo de la pantalla)
    for i in range(5):
        image_rect = image.get_rect()
        image_rect.x = ANCHO // 4 - columna_espaciado  # Posición en el lado izquierdo
        image_rect.y = (ALTO // 5) * i + 80  # Espaciado vertical en la columna
        obstaculos.append(image_rect)

    # Segunda columna de obstáculos (lado derecho de la pantalla)
    for i in range(5):
        image_rect = image.get_rect()
        image_rect.x = 3 * ANCHO // 3 - columna_espaciado  # Posición en el lado derecho
        image_rect.y = (ALTO // 6) * i + 40  # Espaciado vertical en la columna
        obstaculos.append(image_rect)

    return obstaculos

obstaculos = crear_obstaculos()

# Crear la "Meta" en la parte superior de la pantalla
meta_rect = pygame.Rect((ANCHO // 2 - 50, 10), (100, 40))

# Variables de movimiento para los 10 obstáculos
move_speeds = [2, 5, 4, 7, 6, 3, 2, 5, 4, 6]  # Velocidades para cada obstáculo
moving_right = [True, False, True, False, True, True, False, True, False, True]  # Direcciones iniciales

pause = False

# Función para mover los troncos
def move_obstacles():
    """Mueve los obstáculos (troncos) horizontalmente en la pantalla, alternando sus direcciones al
    llegar a los bordes. Cada obstáculo se mueve independientemente con una velocidad asignada.

    Args:
        None
    
    Returns: None.
    """
    global obstaculos, pause
    while True:
        if not pause:
            for i in range(10):
                if moving_right[i]:
                    obstaculos[i].x += move_speeds[i]
                    if obstaculos[i].right >= screen_width:
                        moving_right[i] = False
                else:
                    obstaculos[i].x -= move_speeds[i]
                    if obstaculos[i].left <= 0:
                        moving_right[i] = True
            # Tiempo de pausa variable
            time.sleep(random.uniform(0.01, 0.01))  # Pausa aleatoria entre 10ms y 30ms

# Crear y comenzar el hilo para mover los obstáculos
move_thread = threading.Thread(target=move_obstacles)
move_thread.daemon = True
move_thread.start()

# Función para reiniciar el juego
def reiniciar_juego():
    """Reinicia el estado del juego, incluyendo la posición del jugador y los obstáculos en la pantalla.

    Args:
        None

    Returns: None.
    """
    global image_jugador_rect, obstaculos, moving_right
    image_jugador_rect.topleft = (screen_width // 2, screen_height // 2)  # Reiniciar posición del jugador
    obstaculos = crear_obstaculos()  # Reiniciar obstáculos
    moving_right = [True, False, True, False, True, True, False, True, False, True]

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
            image_jugador_rect.x -= move_speeds[0]
        if keys[pygame.K_RIGHT]:
            image_jugador_rect.x += move_speeds[0]
        if keys[pygame.K_UP]:
            image_jugador_rect.y -= move_speeds[0]
        if keys[pygame.K_DOWN]:
            image_jugador_rect.y += move_speeds[0]

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
        subprocess.Popen(["python", "mar_nivel1.py"])
        #subprocess.Popen(["python", "mar.py"])      #para ponerlo con las preguntas quitar el de abajo y quitar el comentario de este
        
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
