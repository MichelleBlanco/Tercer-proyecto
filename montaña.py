import pygame
import json
import time
import random
import subprocess

from nombre import lista_nombres 
# Inicializar Pygame
pygame.init()

# Cargar el contenido del archivo JSON
with open('preguntas_montana.json', 'r') as file:
    preguntas_montana = json.load(file)


class NodoPregunta:
    def __init__(self, pregunta, respuesta, peso):
        self.pregunta = pregunta
        self.respuesta = respuesta
        self.peso = peso
        self.izquierda = None
        self.derecha = None

    def actualizar_peso(self, correcta):
        if correcta:
            if self.peso > 0:
                self.peso -= 1  # Restar 1 solo si el peso es mayor a 1
        else:
            self.peso += 1  # Incrementar 1 si la respuesta es incorrecta

class ArbolPreguntas:
    def __init__(self, preguntas):       #preguntas es la lista de diccionarios, 
        self.preguntas = sorted(preguntas, key=lambda x: x['peso']) #key=lambda x: x['peso']: toma del diccionario x y devielve el valor de la clave # Ordenar preguntas por peso
        self.raiz = self.construir_arbol(0, len(self.preguntas) - 1)

    
    def construir_arbol(self, inicio, fin):
        if inicio > fin:
            return None

        # El nodo raíz tiene el menor peso (en la posición inicio)
        nodo_actual = NodoPregunta(self.preguntas[inicio]['pregunta'],
                                   self.preguntas[inicio]['respuesta'],
                                   self.preguntas[inicio]['peso'])
        
        # El siguiente nodo de menor peso será el hijo izquierdo
        if inicio + 1 <= fin:
            nodo_actual.izquierda = self.construir_arbol(inicio + 1, (inicio + fin) // 2)
        
        # El siguiente nodo de mayor peso será el hijo derecho
        if (inicio + fin) // 2 + 1 <= fin:
            nodo_actual.derecha = self.construir_arbol((inicio + fin) // 2 + 1, fin)

        return nodo_actual

    def jugar(self):
        pygame.init()
        CELESTE = (173, 216, 230)
        ANCHO, ALTO = 1300, 650
        ventana = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Juego de Preguntas")
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 40)

        nodo = self.raiz
        respuesta_usuario = ""
        cursor_visible = True
        ultimo_cambio_cursor = time.time()
        preguntas_respuestas = 0
        correctas = 0
        incorrectas = 0

        def mostrar_pregunta(mensaje=None):
            ventana.fill(CELESTE)
            
            # Mostrar la pregunta
            pregunta_texto = font.render(f"Pregunta: {nodo.pregunta}", True, (255, 255, 255))
            ventana.blit(pregunta_texto, (ANCHO // 2 - pregunta_texto.get_width() // 2, 150))
            
            # Mostrar la caja de texto para la respuesta del usuario
            rect_input = pygame.Rect(ANCHO // 2 - 200, 300, 400, 50)
            pygame.draw.rect(ventana, (255, 255, 255), rect_input, 2)
            texto_mostrar = respuesta_usuario + ("|" if cursor_visible else "")
            texto_render = font.render(texto_mostrar, True, (0, 0, 0))
            ventana.blit(texto_render, (rect_input.x + 10, rect_input.y + 10))
        
            # Mostrar mensaje adicional (si hay alguno) debajo de la caja de respuesta
            if mensaje:
                # Dividir el mensaje en líneas si contiene saltos de línea
                lineas = mensaje.split('\n')
                for i, linea in enumerate(lineas):
                    color = (255, 0, 0) if "incorrecta" in mensaje else (0, 255, 0)
                    mensaje_texto = font.render(linea, True, color)
                    ventana.blit(mensaje_texto, (ANCHO // 2 - mensaje_texto.get_width() // 2, 400 + i * 40))

            pygame.display.flip()
        
        while preguntas_respuestas < 5 and nodo is not None:
            mostrar_pregunta()
        
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_BACKSPACE:
                        respuesta_usuario = respuesta_usuario[:-1]
                    elif evento.key == pygame.K_RETURN:
                        # Comprobar si la respuesta es correcta
                        correcta = respuesta_usuario.strip().lower() == nodo.respuesta.strip().lower()
                        if correcta:
                            mensaje = "Respuesta correcta!"
                            correctas += 1
                            # Actualizar el peso de la pregunta
                            nodo.actualizar_peso(correcta)
                            for pregunta in self.preguntas:
                                if pregunta['pregunta'] == nodo.pregunta:
                                    pregunta['peso'] = nodo.peso
                                    break
                            # Guardar inmediatamente en el archivo JSON
                            with open("preguntas_montana.json", "w") as file:
                                json.dump(self.preguntas, file, indent=4)  
                            #import montana_nivel1              #para activar con las preguntas
                            #montana_nivel1()
                        else:
                            mensaje = f"Respuesta incorrecta.\nLa respuesta correcta es: {nodo.respuesta}"
                            incorrectas += 1
                            # Actualizar el peso de la pregunta
                            nodo.actualizar_peso(correcta)
                            for pregunta in self.preguntas:
                                if pregunta['pregunta'] == nodo.pregunta:
                                    pregunta['peso'] = nodo.peso
                                    break
                            # Guardar inmediatamente en el archivo JSON
                            with open("preguntas_montana.json", "w") as file:
                                json.dump(self.preguntas, file, indent=4)  
                            #import montana_nivel2
                            #montana_nivel2()
        
                        # Mostrar el mensaje en la ventana por 2 segundos
                        mostrar_pregunta(mensaje)
                        pygame.time.delay(3000)  # Esperar 2 segundos
          
                        
                        # Preparar para la siguiente pregunta
                        preguntas_respuestas += 1
                        respuesta_usuario = ""
                        nodo = nodo.izquierda if correcta else nodo.derecha
                    else:
                        respuesta_usuario += evento.unicode
            
            # Parpadeo del cursor
            if time.time() - ultimo_cambio_cursor > 0.5:
                cursor_visible = not cursor_visible
                ultimo_cambio_cursor = time.time()
        
            clock.tick(30)
        ventana.fill((0, 0, 0))
        resultado_texto = font.render(f"Correctas: {correctas} - Incorrectas: {incorrectas}", True, (255, 255, 255))
        ventana.blit(resultado_texto, (ANCHO // 2 - resultado_texto.get_width() // 2, ALTO // 2))
        pygame.display.flip()
        pygame.time.delay(3000)

        with open("preguntas_monntana.json", "w") as file:
            json.dump(self.preguntas, file, indent=4)

        modos_juego = ["ciudad", "mar", "bosque", "espacio"]
        modo_seleccionado = random.choice(modos_juego)
        if modo_seleccionado == "ciudad":
            subprocess.Popen(["python", "ciudad_nivel1.py"])
        elif modo_seleccionado == "mar":
            subprocess.Popen(["python", "mar_nivel1.py"])
        elif modo_seleccionado == "bosque":
            subprocess.Popen(["python", "bosque_nivel1.py"])
        elif modo_seleccionado == "espacio":
            subprocess.Popen(["python", "espacio_nivel1.py"])

        pygame.quit()
arbol = ArbolPreguntas(preguntas_montana)
arbol.jugar()
