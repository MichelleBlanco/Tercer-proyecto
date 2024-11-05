# menu.py
import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 1500, 800
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Trivia Challenge")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (200, 0, 0)
VERDE = (0, 200, 0)
AZUL = (0, 0, 200)

# Cargar imagen de fondo
fondo = pygame.image.load("fondo.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Fuentes
fuente = pygame.font.Font(None, 40)

# Definir botones
def dibujar_boton(texto, x, y, ancho, alto, color_normal, color_hover, accion=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Cambiar color si el mouse está sobre el botón
    if x + ancho > mouse[0] > x and y + alto > mouse[1] > y:
        pygame.draw.rect(ventana, color_hover, (x, y, ancho, alto))
        if click[0] == 1 and accion is not None:
            accion()
    else:
        pygame.draw.rect(ventana, color_normal, (x, y, ancho, alto))

    # Renderizar texto
    texto_superficie = fuente.render(texto, True, BLANCO)
    texto_rect = texto_superficie.get_rect()
    texto_rect.center = ((x + (ancho // 2)), (y + (alto // 2)))
    ventana.blit(texto_superficie, texto_rect)

# Acciones de los botones
def jugar():
    import nombre

def cargar_juego():
    print("Cargar juego")
    # Aquí puedes agregar la lógica para cargar el juego guardado

def salir():
    pygame.quit()
    sys.exit()

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Dibujar fondo
    ventana.blit(fondo, (0, 0))

    # Dibujar botones
    dibujar_boton("Jugar", 610, 200, 200, 50, VERDE, (0, 255, 0), jugar)
    dibujar_boton("Cargar Juego", 610, 300, 200, 50, VERDE, (0, 0, 255), cargar_juego)
    dibujar_boton("Salir", 610, 400, 200, 50, VERDE, (255, 0, 0), salir)

    # Actualizar la pantalla
    pygame.display.update()

# Finalizar Pygame
pygame.quit()
