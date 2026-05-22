"""rabbid.py - Clase Rabbid mejorada con sistemas de estado y comportamiento

Demuestra conceptos OOP avanzados:
- Encapsulación: Datos protegidos en la clase
- Estados: Sistema de comportamiento basado en diccionarios
- Herencia: Preparado para extensión
- Métodos privados: Lógica interna con _

Inspirado en estudios de arquitectura de proyectos similares como MikuPet,
adaptado completamente a nuestro sistema Pygame + Win32.
"""

import random


class Rabbid:
    """Clase que representa el Rabbid (Shimeji)
    
    Sistema de estados:
    - normal: Comportamiento tranquilo, azul
    - caos: Modo caótico, rojo
    """
    
    def __init__(self, x=300, y=300):
        """Inicializa un nuevo Rabbid
        
        Args:
            x: Posición horizontal inicial
            y: Posición vertical inicial
        """
        # === POSICIÓN Y FÍSICA ===
        self.x = x
        self.y = y
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.en_suelo = False
        
        # === TAMAÑO ===
        self.ancho = 50
        self.alto = 50
        
        # === ESTADO ACTUAL ===
        self._estado = "normal"  # normal, caos
        self._estados_dict = {
            "normal": {
                "color_ojos": (0, 0, 255),      # Azul
                "color_cuerpo": (100, 100, 150),
                "velocidad_movimiento": 2,
                "comportamiento": "idle"
            },
            "caos": {
                "color_ojos": (255, 0, 0),      # Rojo
                "color_cuerpo": (200, 50, 50),
                "velocidad_movimiento": 4,
                "comportamiento": "caos"
            }
        }
        
        # === COMPORTAMIENTO ===
        self.contador_movimiento = 0
        self.direccion = random.choice([-1, 1])
        self.tiempo_estado = 0
    
    # === PROPIEDADES (Properties) ===
    @property
    def estado(self):
        """Retorna el estado actual del Rabbid"""
        return self._estado
    
    @estado.setter
    def estado(self, nuevo_estado):
        """Cambia el estado del Rabbid"""
        if nuevo_estado in self._estados_dict:
            self._estado = nuevo_estado
            self.tiempo_estado = 0
        else:
            raise ValueError(f"Estado '{nuevo_estado}' no válido")
    
    # === MÉTODOS PRINCIPALES ===
    
    def actualizar(self):
        """Actualiza el comportamiento del Rabbid cada frame"""
        self.tiempo_estado += 1
        
        # Comportamiento según estado
        if self._estado == "normal":
            self._actualizar_normal()
        elif self._estado == "caos":
            self._actualizar_caos()
    
    def _actualizar_normal(self):
        """Actualiza el comportamiento en estado normal"""
        self.contador_movimiento += 1
        
        # Cambiar dirección aleatoriamente cada cierto tiempo
        if self.contador_movimiento % 120 == 0:  # Cada 120 frames (2 segundos a 60 FPS)
            self.direccion = random.choice([-1, 1])
        
        # Movimiento horizontal leve
        if self.contador_movimiento % 30 == 0:
            self.velocidad_x = self.direccion * random.uniform(0.5, 1.5)
    
    def _actualizar_caos(self):
        """Actualiza el comportamiento en estado caos"""
        # Movimiento caótico rápido
        if self.contador_movimiento % 10 == 0:
            self.velocidad_x = random.uniform(-5, 5)
            self.velocidad_y = random.uniform(-3, 3)
        
        self.contador_movimiento += 1
    
    def alternar_estado(self):
        """Alterna entre normal y caos"""
        nuevo_estado = "caos" if self._estado == "normal" else "normal"
        self.estado = nuevo_estado
    
    def dibujar(self, pantalla, pygame):
        """Dibuja el Rabbid en la pantalla
        
        Args:
            pantalla: Superficie de Pygame donde dibujar
            pygame: Módulo de Pygame
        """
        config_estado = self._estados_dict[self._estado]
        color_cuerpo = config_estado["color_cuerpo"]
        color_ojos = config_estado["color_ojos"]
        
        # Dibujar cuerpo (rectángulo redondeado simulado)
        pygame.draw.rect(pantalla, color_cuerpo, 
                        (self.x, self.y, self.ancho, self.alto))
        
        # Dibujar ojos
        distancia_ojo = 12
        tamaño_ojo = 4
        
        # Ojo izquierdo
        pygame.draw.circle(pantalla, color_ojos,
                          (int(self.x + distancia_ojo), int(self.y + 15)),
                          tamaño_ojo)
        
        # Ojo derecho
        pygame.draw.circle(pantalla, color_ojos,
                          (int(self.x + self.ancho - distancia_ojo), int(self.y + 15)),
                          tamaño_ojo)
        
        # Boca (línea)
        if self._estado == "caos":
            # Boca "asustada" en caos
            pygame.draw.line(pantalla, color_ojos,
                            (int(self.x + 15), int(self.y + 35)),
                            (int(self.x + self.ancho - 15), int(self.y + 35)), 2)
    
    def obtener_info(self):
        """Retorna información del Rabbid
        
        Returns:
            Diccionario con datos actuales del Rabbid
        """
        return {
            "x": self.x,
            "y": self.y,
            "estado": self._estado,
            "velocidad_x": self.velocidad_x,
            "velocidad_y": self.velocidad_y,
            "en_suelo": self.en_suelo,
            "color_ojos": self._estados_dict[self._estado]["color_ojos"]
        }
    
    def __str__(self):
        """Representación en texto del Rabbid"""
        return f"Rabbid(x={self.x:.0f}, y={self.y:.0f}, estado={self._estado})"
    
    def __repr__(self):
        """Representación para debugging"""
        return self.__str__()
