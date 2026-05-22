"""Main.py - Punto de entrada del juego Rabbid Chaos Companion

Configura Pygame, transparencia en Windows, y ejecuta el loop principal.

Requisitos:
- pygame
- pywin32 (solo Windows)

Características:
- Ventana transparente sin bordes
- Sistema de física (gravedad, colisiones)
- Estados del Rabbid (normal, caos)
- Interactividad con click
"""

import pygame
import sys

# Importar nuestras clases
from rabbid import Rabbid
from fisica import SistemaFisica

# Intentar importar las librerías de Windows para transparencia
try:
    import win32api
    import win32con
    import win32gui
    WINDOWS_DISPONIBLE = True
except ImportError:
    WINDOWS_DISPONIBLE = False
    print("⚠️  Advertencia: pywin32 no instalado. La transparencia no funcionará.")
    print("   En Windows, instala: pip install pywin32")


class Juego:
    """Clase que maneja el juego principal
    
    Demostración de OOP:
    - Composición: Contiene instancias de Rabbid y SistemaFisica
    - Encapsulación: Métodos privados con _
    - Métodos de inicialización y manejo
    """
    
    def __init__(self, ancho=800, alto=600):
        """Inicializa el juego
        
        Args:
            ancho: Ancho de la ventana
            alto: Alto de la ventana
        """
        pygame.init()
        
        self.ancho = ancho
        self.alto = alto
        self.hecho = False
        
        # Crear pantalla sin bordes
        self.pantalla = pygame.display.set_mode(
            (ancho, alto), 
            pygame.NOFRAME
        )
        pygame.display.set_caption("Rabbid Chaos Companion")
        
        # Configurar transparencia (solo Windows)
        if WINDOWS_DISPONIBLE:
            self._configurar_transparencia()
        
        # Color fucsia = transparente
        self.fucsia = (255, 0, 128)
        
        # Crear el Rabbid en el centro
        self.rabbid = Rabbid(ancho // 2 - 25, alto // 2 - 25)
        
        # Sistema de física
        self.fisica = SistemaFisica(ancho, alto)
        
        # Reloj para FPS
        self.reloj = pygame.time.Clock()
        self.fps = 60
        
        # Información de clicks
        self.clicks = 0
    
    def _configurar_transparencia(self):
        """Configura la transparencia en Windows
        
        Usa Win32 API para:
        1. Hacer la ventana siempre en primer plano (topmost)
        2. Hacer clic a través de la ventana (layered)
        3. Configurar el color clave para transparencia (fucsia)
        """
        try:
            hwnd = pygame.display.get_wm_info()["window"]
            win32gui.SetWindowLong(
                hwnd, 
                win32con.GWL_EXSTYLE,
                win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | 
                win32con.WS_EX_LAYERED | 
                win32con.WS_EX_TOPMOST
            )
            # El color fucsia será el que se vuelva invisible
            win32gui.SetLayeredWindowAttributes(
                hwnd, 
                win32api.RGB(255, 0, 128), 
                0, 
                win32con.LWA_COLORKEY
            )
            print("✅ Transparencia configurada exitosamente")
        except Exception as e:
            print(f"❌ Error al configurar transparencia: {e}")
    
    def procesar_eventos(self):
        """Procesa los eventos de la ventana
        
        Maneja:
        - Cierre de ventana (QUIT)
        - Clicks en el Rabbid
        """
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.hecho = True
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # Click en el Rabbid
                self._manejar_click(evento.pos)
    
    def _manejar_click(self, posicion):
        """Maneja cuando se hace click
        
        Args:
            posicion: Tupla (x, y) del click
        """
        mouse_x, mouse_y = posicion
        
        # Verificar si el click está dentro del Rabbid
        if (self.rabbid.x < mouse_x < self.rabbid.x + self.rabbid.ancho and
            self.rabbid.y < mouse_y < self.rabbid.y + self.rabbid.alto):
            # Alternar estado
            self.rabbid.alternar_estado()
            self.clicks += 1
            
            # Aplicar impulso cuando se hace click
            self.fisica.hacer_saltar(self.rabbid, potencia=12)
            
            estado = self.rabbid.estado
            print(f"🐰 Click #{self.clicks} - Rabbid ahora está: {estado}")
    
    def actualizar(self):
        """Actualiza la lógica del juego
        
        Orden:
        1. Actualizar comportamiento del Rabbid
        2. Aplicar física
        """
        self.rabbid.actualizar()
        self.fisica.aplicar_fisica(self.rabbid)
    
    def dibujar(self):
        """Dibuja todo en la pantalla
        
        Orden:
        1. Llenar fondo con fucsia (transparente)
        2. Dibujar el Rabbid
        3. Dibujar información de debug
        4. Actualizar pantalla
        """
        # Fondo transparente (fucsia)
        self.pantalla.fill(self.fucsia)
        
        # Dibujar el Rabbid
        self.rabbid.dibujar(self.pantalla, pygame)
        
        # Mostrar información de debug
        self._dibujar_info()
        
        # Actualizar pantalla
        pygame.display.flip()
    
    def _dibujar_info(self):
        """Dibuja información de debug en la pantalla"""
        fuente = pygame.font.Font(None, 20)
        info = self.rabbid.obtener_info()
        
        # Línea 1: Estado
        texto1 = fuente.render(
            f"Estado: {info['estado'].upper()} | Clicks: {self.clicks}",
            True,
            (255, 255, 255)
        )
        self.pantalla.blit(texto1, (10, 10))
        
        # Línea 2: Posición y velocidad
        texto2 = fuente.render(
            f"Pos: ({info['x']:.0f}, {info['y']:.0f}) | Vel: ({info['velocidad_x']:.1f}, {info['velocidad_y']:.1f})",
            True,
            (200, 200, 200)
        )
        self.pantalla.blit(texto2, (10, 35))
        
        # Línea 3: Instrucciones
        texto3 = fuente.render(
            "Haz click en el Rabbid para alternar estados",
            True,
            (150, 150, 150)
        )
        self.pantalla.blit(texto3, (10, self.alto - 25))
    
    def ejecutar(self):
        """Loop principal del juego"""
        print("="*50)
        print("🐰 RABBID CHAOS COMPANION - INICIANDO")
        print("="*50)
        print("Haz click en el Rabbid para cambiar su estado")
        print("Normal → Caos → Normal")
        print("Cierra la ventana para salir")
        print("="*50)
        
        while not self.hecho:
            self.procesar_eventos()
            self.actualizar()
            self.dibujar()
            self.reloj.tick(self.fps)
        
        self.cerrar()
    
    def cerrar(self):
        """Cierra el juego de forma limpia"""
        print(f"\n👋 Juego cerrado. Total de clicks: {self.clicks}")
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    juego = Juego()
    juego.ejecutar()
