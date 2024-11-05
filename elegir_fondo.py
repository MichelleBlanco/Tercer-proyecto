import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 1550, 850
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Elegir Fondo")

# Colores
CELESTE = (173, 216, 230)
BLANCO = (255, 255, 255)
GRIS = (200, 200, 200)

# Función para mostrar la imagen del bosque y detectar clics
def bosque1():
    imagen = pygame.image.load("bosque.jpg") 
    nueva_anchura = 380
    nueva_altura = 250
    imagen_pequeña = pygame.transform.scale(imagen, (nueva_anchura, nueva_altura))

    # Coordenadas de la imagen (x, y)
    x = 300
    y = 100

    imagen_rect = imagen_pequeña.get_rect(topleft=(x, y))  # Rectángulo de colisión
    ventana.blit(imagen_pequeña, (x, y))  # Dibuja la imagen en la posición deseada

    return imagen_rect

def mar1():
    imagen = pygame.image.load("mar.png")  
    nueva_anchura = 380
    nueva_altura = 250
    imagen_pequeña = pygame.transform.scale(imagen, (nueva_anchura, nueva_altura))

    # Coordenadas de la imagen (x, y)
    x = 800
    y = 100

    imagen_rect = imagen_pequeña.get_rect(topleft=(x, y))  # Rectángulo de colisión
    ventana.blit(imagen_pequeña, (x, y))  # Dibuja la imagen en la posición deseada

    return imagen_rect

def montaña1():
    imagen = pygame.image.load("montaña.png")  
    nueva_anchura = 380
    nueva_altura = 250
    imagen_pequeña = pygame.transform.scale(imagen, (nueva_anchura, nueva_altura))

    # Coordenadas de la imagen (x, y)
    x = 100
    y = 500

    imagen_rect = imagen_pequeña.get_rect(topleft=(x, y))  # Rectángulo de colisión
    ventana.blit(imagen_pequeña, (x, y))  # Dibuja la imagen en la posición deseada

    return imagen_rect

def espacio1():
    imagen = pygame.image.load("espacio.png")  
    nueva_anchura = 380
    nueva_altura = 250
    imagen_pequeña = pygame.transform.scale(imagen, (nueva_anchura, nueva_altura))

    # Coordenadas de la imagen (x, y)
    x = 550
    y = 500

    imagen_rect = imagen_pequeña.get_rect(topleft=(x, y))  # Rectángulo de colisión
    ventana.blit(imagen_pequeña, (x, y))  # Dibuja la imagen en la posición deseada

    return imagen_rect

def ciudad1():
    imagen = pygame.image.load("ciudad.png")  
    nueva_anchura = 380
    nueva_altura = 250
    imagen_pequeña = pygame.transform.scale(imagen, (nueva_anchura, nueva_altura))

    # Coordenadas de la imagen (x, y)
    x = 1000
    y = 500

    imagen_rect = imagen_pequeña.get_rect(topleft=(x, y))  # Rectángulo de colisión
    ventana.blit(imagen_pequeña, (x, y))  # Dibuja la imagen en la posición deseada

    return imagen_rect

# Bucle principal de la ventana de elegir fondo
def main():
    corriendo = True
    while corriendo:
        ventana.fill(CELESTE)
        bosque_rect = bosque1()
        mar_rect = mar1()
        montaña_rect = montaña1()
        espacio_rect = espacio1()
        ciudad_rect = ciudad1()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # Verifica si el clic está dentro del área de la imagen
                if bosque_rect.collidepoint(evento.pos):
                    import bosque  # Asegúrate de que el archivo 'bosque.py' exista y esté configurado
                elif mar_rect.collidepoint(evento.pos):
                    import mar
                elif montaña_rect.collidepoint(evento.pos):
                    import montaña
                elif espacio_rect.collidepoint(evento.pos):
                    import espacio
                elif ciudad_rect.collidepoint(evento.pos):
                    import ciudad
        pygame.display.flip()
        

# Ejecutar el archivo si se abre directamente
if __name__ == "__main__":
    main()



