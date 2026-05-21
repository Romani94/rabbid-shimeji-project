"""Clase Rabbid - El corazón del proyecto

Demonstración de conceptos OOP:
- Encapsulación: Los datos del Rabbid están protegidos en la clase
- Atributos: x, y, estado, ojos, etc.
- Métodos: actualizar(), dibujar(), etc.
"""

class Rabbid:
    """Clase que representa el Rabbid (Shimeji)"""
    
    def __init__(self, x=300, y=300):
        """Inicializa un nuevo Rabbid
        
        Args:
            x: Posición horizontal inicial
            y: Posición vertical inicial
        """
        # Atributos de posición
        self.x = x
        self.y = y
        
        # Atributos del estado
        self.estado = "normal"  # normal, feliz, enojado, etc.
        self.ojos = "azul"      # color de los ojos
        
        # Atributos físicos
        self.en_suelo = False
        self.velocidad_x = 0
        self.velocidad_y = 0
        
        # Objeto que puede cargar
        self.objeto = None
        
        # Información de tamaño
        self.ancho = 50
        self.alto = 50
    
    def actualizar(self):
        """Actualiza el estado del Rabbid cada frame"""
        # Aquí irá la lógica de movimiento
        pass
    
    def dibujar(self, pantalla, pygame):
        """Dibuja el Rabbid en la pantalla
        
        Args:
            pantalla: Superficie de Pygame donde dibujar
            pygame: Módulo de Pygame
        """
        # Por ahora, dibuja un rectángulo simple
        # Más adelante: aquí irá la imagen del Rabbid
        color = self._obtener_color_estado()
        pygame.draw.rect(pantalla, color, 
                        (self.x, self.y, self.ancho, self.alto))
    
    def _obtener_color_estado(self):
        """Retorna el color basado en el estado actual
        
        Método privado (empieza con _) - uso interno de la clase
        """
        colores = {
            "normal": (100, 100, 150),
            "feliz": (150, 200, 100),
            "enojado": (200, 100, 100),
        }
        return colores.get(self.estado, (100, 100, 150))
    
    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado del Rabbid
        
        Args:
            nuevo_estado: El nuevo estado (feliz, enojado, etc.)
        """
        self.estado = nuevo_estado
    
    def obtener_info(self):
        """Retorna información del Rabbid
        
        Returns:
            Diccionario con datos actuales del Rabbid
        """
        return {
            "x": self.x,
            "y": self.y,
            "estado": self.estado,
            "ojos": self.ojos,
            "en_suelo": self.en_suelo,
            "objeto": self.objeto
        }
    
    def __str__(self):
        """Representación en texto del Rabbid"""
        return f"Rabbid(x={self.x}, y={self.y}, estado={self.estado})"
