# nombre.py
import pygame
import sys
import time
import elegir_fondo

def un_fondo():
    if pygame.display.get_init():  # Verifica si Pygame está inicializado
        elegir_fondo.main()
        

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana y configuración del fondo
ANCHO, ALTO = 1550, 800
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ingreso de Nombre de Usuario")

# Cargar la imagen de fondo
fondo = pygame.image.load("fondo.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Colores y configuración de texto
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
fuente = pygame.font.Font(None, 40)

# Variables para la entrada de texto
nombre_usuario = ""
lista_nombres = []
cursor_visible = True  # Controla si el cursor se muestra o no
ultimo_cambio_cursor = time.time()  # Tiempo para el parpadeo del cursor

# Botón "Comenzar"
color_boton = (0, 128, 0)  # Color verde para el botón
rectangulo_boton = pygame.Rect(ANCHO - 850, ALTO - 400, 150, 50)  # Posición y tamaño

def dibujar_texto(texto, fuente, color, superficie, x, y):
    texto_obj = fuente.render(texto, True, color)
    texto_rect = texto_obj.get_rect()
    texto_rect.topleft = (x, y)
    superficie.blit(texto_obj, texto_rect)

# Bucle principal
ejecutando = True
while ejecutando:
    ventana.blit(fondo, (0, 0))  # Dibujar el fondo
    
    # Dibujar etiquetas y texto ingresado
    dibujar_texto("Ingrese su nombre de usuario:", fuente, BLANCO, ventana, 550, 150)
    
    # Dibujar campo de entrada y mostrar el texto ingresado
    rect_input = pygame.Rect(550, 200, 400, 50)  # Posición y tamaño del "campo de entrada"
    pygame.draw.rect(ventana, BLANCO, rect_input, 2)  # Rectángulo blanco como borde
    texto_mostrar = nombre_usuario + ("|" if cursor_visible else "")
    dibujar_texto(texto_mostrar, fuente, NEGRO, ventana, rect_input.x + 10, rect_input.y + 10)

    # Dibujar el botón "Comenzar"
    pygame.draw.rect(ventana, color_boton, rectangulo_boton)
    dibujar_texto("Comenzar", fuente, BLANCO, ventana, rectangulo_boton.x + 10, rectangulo_boton.y + 10)

    pygame.display.flip()

    # Control de parpadeo del cursor
    if time.time() - ultimo_cambio_cursor > 0.5:  # Parpadeo cada 0.5 segundos
        cursor_visible = not cursor_visible
        ultimo_cambio_cursor = time.time()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        # Capturar el texto ingresado
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False
            elif evento.key == pygame.K_BACKSPACE:
                nombre_usuario = nombre_usuario[:-1]
            elif evento.key == pygame.K_RETURN:
                if 3 <= len(nombre_usuario) <= 10:  # Validación del nombre
                    lista_nombres.append(nombre_usuario)
                    print(f"Nombres guardados: {lista_nombres}")
                    nombre_usuario = ""  # Reiniciar el campo de entrada
                else:
                    print("El nombre debe tener entre 3 y 10 caracteres.")
            else:
                nombre_usuario += evento.unicode

        # Detectar clic en el botón "Comenzar"
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rectangulo_boton.collidepoint(evento.pos):
                if 3 <= len(nombre_usuario) <= 10:  # Asegura que el nombre sea válido
                    lista_nombres.append(nombre_usuario)
                    print(f"Nombres de usuario guardados: {lista_nombres}")
                    nombre_usuario = ""  # Reiniciar el campo de entrada
                    un_fondo()  # Llama a un_fondo si el nombre es válido
                else:
                    print("El nombre debe tener entre 3 y 10 caracteres.")
                    
pygame.quit()



