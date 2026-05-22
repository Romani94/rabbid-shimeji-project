"""Módulo de Física - Sistema de gravedad y colisiones

Implementa un sistema de física simplificado para el Rabbid:
- Gravedad
- Colisiones con bordes
- Rebotes
"""

class SistemaFisica:
    """Gestiona la física del Rabbid"""
    
    def __init__(self, ancho_pantalla=800, alto_pantalla=600):
        """Inicializa el sistema de física
        
        Args:
            ancho_pantalla: Ancho de la pantalla
            alto_pantalla: Alto de la pantalla
        """
        self.ancho = ancho_pantalla
        self.alto = alto_pantalla
        
        # Constantes de física
        self.gravedad = 0.5
        self.friccion = 0.99
        self.elasticidad = 0.7
        self.velocidad_maxima = 15
        
        # Margen para el suelo (donde está la barra de tareas)
        self.margen_suelo = 30
    
    def aplicar_fisica(self, rabbid):
        """Aplica física al Rabbid
        
        Args:
            rabbid: Objeto Rabbid a actualizar
        """
        # Aplicar gravedad
        rabbid.velocidad_y += self.gravedad
        
        # Aplicar fricción del aire
        rabbid.velocidad_x *= self.friccion
        rabbid.velocidad_y *= self.friccion
        
        # Limitar velocidad máxima
        if abs(rabbid.velocidad_y) > self.velocidad_maxima:
            rabbid.velocidad_y = self.velocidad_maxima if rabbid.velocidad_y > 0 else -self.velocidad_maxima
        
        # Actualizar posición
        rabbid.x += rabbid.velocidad_x
        rabbid.y += rabbid.velocidad_y
        
        # Detectar colisiones con bordes
        self._detectar_colisiones(rabbid)
    
    def _detectar_colisiones(self, rabbid):
        """Detecta y maneja colisiones con los bordes
        
        Args:
            rabbid: Objeto Rabbid
        """
        # Colisión con piso (tratamos como si existiera barra de tareas)
        if rabbid.y + rabbid.alto >= self.alto - self.margen_suelo:
            rabbid.y = self.alto - self.margen_suelo - rabbid.alto
            rabbid.velocidad_y *= -self.elasticidad
            rabbid.en_suelo = True
        else:
            rabbid.en_suelo = False
        
        # Colisión con techo
        if rabbid.y <= 0:
            rabbid.y = 0
            rabbid.velocidad_y *= -self.elasticidad
        
        # Colisión con pared derecha
        if rabbid.x + rabbid.ancho >= self.ancho:
            rabbid.x = self.ancho - rabbid.ancho
            rabbid.velocidad_x *= -self.elasticidad
        
        # Colisión con pared izquierda
        if rabbid.x <= 0:
            rabbid.x = 0
            rabbid.velocidad_x *= -self.elasticidad
    
    def aplicar_impulso(self, rabbid, fuerza_x, fuerza_y):
        """Aplica un impulso al Rabbid
        
        Args:
            rabbid: Objeto Rabbid
            fuerza_x: Fuerza horizontal
            fuerza_y: Fuerza vertical
        """
        rabbid.velocidad_x += fuerza_x
        rabbid.velocidad_y += fuerza_y
    
    def hacer_saltar(self, rabbid, potencia=10):
        """Hace que el Rabbid salte
        
        Args:
            rabbid: Objeto Rabbid
            potencia: Fuerza del salto
        """
        if rabbid.en_suelo:
            rabbid.velocidad_y = -potencia
