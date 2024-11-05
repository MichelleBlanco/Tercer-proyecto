import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 1500, 800
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Elegir Fondo")

# Colores
CELESTE = (173, 216, 230)
BLANCO = (255, 255, 255)
GRIS = (200, 200, 200)

# Función para mostrar la imagen del bosque y detectar clics
def bosque1():
    imagen = pygame.image.load("bosque.jpg")  # Cambia "bosque.jpg" por tu archivo de imagen
    nueva_anchura = 380
    nueva_altura = 250
    imagen_pequeña = pygame.transform.scale(imagen, (nueva_anchura, nueva_altura))

    # Coordenadas de la imagen (x, y)
    x = 300
    y = 100

    imagen_rect = imagen_pequeña.get_rect(topleft=(x, y))  # Rectángulo de colisión
    ventana.blit(imagen_pequeña, (x, y))  # Dibuja la imagen en la posición deseada

    return imagen_rect

# Bucle principal de la ventana de elegir fondo
def main():
    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # Verifica si el clic está dentro del área de la imagen
                if bosque_rect.collidepoint(evento.pos):
                    import bosque  # Asegúrate de que el archivo 'bosque.py' exista y esté configurado

        # Dibujar fondo celeste
        ventana.fill(CELESTE)

        # Dibujar la imagen del bosque y obtener el rectángulo
        bosque_rect = bosque1()

        # Actualizar la pantalla
        pygame.display.flip()

# Ejecutar el archivo si se abre directamente
if __name__ == "__main__":
    main()


