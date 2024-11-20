import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 1300, 650
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Elegir Fondo")

# Colores
CELESTE = (173, 216, 230)
BLANCO = (255, 255, 255)
GRIS = (200, 200, 200)

# Función para mostrar la imagen del bosque y detectar clics
def bosque1():
    """ Carga y dibuja una imagen de bosque en la ventana de juego, escalándola a un tamaño específico y
    estableciendo su posición en la pantalla.

    Args:
        None

    Returns:
         pygame.Rect: Un rectángulo (imagen_rect) que representa la posición y tamaño de la imagen 
        en la ventana, útil para manejar colisiones.
    """
    imagen = pygame.image.load("bosque.jpg") 
    nueva_anchura = 380
    nueva_altura = 250
    imagen_pequena = pygame.transform.scale(imagen, (nueva_anchura, nueva_altura))

    # Coordenadas de la imagen (x, y)
    x = 200
    y = 70

    imagen_rect = imagen_pequena.get_rect(topleft=(x, y))  # Rectángulo de colisión
    ventana.blit(imagen_pequena, (x, y))  # Dibuja la imagen en la posición deseada

    return imagen_rect

def mar1():
    """Carga y dibuja una imagen de mar en la ventana de juego, escalándola a un tamaño específico y 
    ubicándola en una posición predefinida en la pantalla.

    Args:
        None

    Returns:
        pygame.Rect: Un rectángulo (imagen_rect) que representa la posición y tamaño de la imagen 
        en la ventana, útil para detectar colisiones.
    """
    imagen = pygame.image.load("mar.png")  
    nueva_anchura = 380
    nueva_altura = 250
    imagen_pequena = pygame.transform.scale(imagen, (nueva_anchura, nueva_altura))

    # Coordenadas de la imagen (x, y)
    x = 700
    y = 70

    imagen_rect = imagen_pequena.get_rect(topleft=(x, y))  # Rectángulo de colisión
    ventana.blit(imagen_pequena, (x, y))  # Dibuja la imagen en la posición deseada

    return imagen_rect

def montana1():
    """ Carga y dibuja una imagen de montaña en la ventana de juego, escalándola a un tamaño específico 
    y ubicándola en una posición predefinida en la pantalla.

    Args:
        None

    Returns:
        pygame.Rect: Un rectángulo (imagen_rect) que representa la posición y tamaño de la imagen 
        en la ventana, útil para gestionar colisiones.
    """
    imagen = pygame.image.load("montana.png")  
    nueva_anchura = 380
    nueva_altura = 250
    imagen_pequena = pygame.transform.scale(imagen, (nueva_anchura, nueva_altura))

    # Coordenadas de la imagen (x, y)
    x = 50
    y = 360

    imagen_rect = imagen_pequena.get_rect(topleft=(x, y))  # Rectángulo de colisión
    ventana.blit(imagen_pequena, (x, y))  # Dibuja la imagen en la posición deseada

    return imagen_rect

def espacio1():
    """Carga y dibuja una imagen de espacio en la ventana de juego, escalándola a un tamaño específico 
    y ubicándola en una posición predefinida en la pantalla.

    Args:
        None

    Returns:
        pygame.Rect: Un rectángulo (imagen_rect) que representa la posición y tamaño de la imagen 
        en la ventana, útil para detectar colisiones.
    """
    imagen = pygame.image.load("espacio.png")  
    nueva_anchura = 380
    nueva_altura = 250
    imagen_pequena = pygame.transform.scale(imagen, (nueva_anchura, nueva_altura))

    # Coordenadas de la imagen (x, y)
    x = 460
    y = 360

    imagen_rect = imagen_pequena.get_rect(topleft=(x, y))  # Rectángulo de colisión
    ventana.blit(imagen_pequena, (x, y))  # Dibuja la imagen en la posición deseada

    return imagen_rect

def ciudad1():
    """ Carga y dibuja una imagen de ciudad en la ventana de juego, escalándola a un tamaño específico 
    y ubicándola en una posición predefinida en la pantalla.

    Args:
        None

    Returns:
        pygame.Rect: Un rectángulo (imagen_rect) que representa la posición y tamaño de la imagen 
        en la ventana, útil para gestionar colisiones.
    """
    imagen = pygame.image.load("ciudad.png")  
    nueva_anchura = 380
    nueva_altura = 250
    imagen_pequena = pygame.transform.scale(imagen, (nueva_anchura, nueva_altura))

    # Coordenadas de la imagen (x, y)
    x = 870
    y = 360

    imagen_rect = imagen_pequena.get_rect(topleft=(x, y))  # Rectángulo de colisión
    ventana.blit(imagen_pequena, (x, y))  # Dibuja la imagen en la posición deseada

    return imagen_rect

# Bucle principal de la ventana de elegir fondo   
def main():
    """Ejecuta el bucle principal del juego y gestiona la lógica de interacción con las diferentes 
    escenas mediante clics del mouse.

    Args:
        None
    
    Returns:
        None.
    """
    corriendo = True
    while corriendo:
        ventana.fill(CELESTE)
        bosque_rect = bosque1()
        mar_rect = mar1()
        montana_rect = montana1()
        espacio_rect = espacio1()
        ciudad_rect = ciudad1()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # Verifica si el clic está dentro del área de la imagen
                if bosque_rect.collidepoint(evento.pos):
                    import bosque_nivel1  # Asegúrate de que el archivo 'bosque.py' exista y esté configurado
                elif mar_rect.collidepoint(evento.pos):
                    import mar_nivel1
                elif montana_rect.collidepoint(evento.pos):
                    import montana_nivel1
                elif espacio_rect.collidepoint(evento.pos):
                    import espacio_nivel1
                elif ciudad_rect.collidepoint(evento.pos):
                    import ciudad_nivel1
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()  

# Ejecutar el archivo si se abre directamente
if __name__ == "__main__":
    main()


