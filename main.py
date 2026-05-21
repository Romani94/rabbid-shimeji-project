"""Main.py - Punto de entrada del juego

Configura Pygame, transparencia en Windows, y ejecuta el loop principal.

Requisitos:
- pygame
- pywin32 (solo Windows)
"""

import pygame
import sys

# Importar nuestra clase Rabbid
from rabbid import Rabbid

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
    """Clase que maneja el juego principal"""
    
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
        pygame.display.set_caption("Rabbid Shimeji")
        
        # Configurar transparencia (solo Windows)
        if WINDOWS_DISPONIBLE:
            self._configurar_transparencia()
        
        # Color fucsia = transparente
        self.fucsia = (255, 0, 128)
        
        # Crear el Rabbid
        self.rabbid = Rabbid(ancho // 2, alto // 2)
        
        # Reloj para FPS
        self.reloj = pygame.time.Clock()
        self.fps = 60
    
    def _configurar_transparencia(self):
        """Configura la transparencia en Windows"""
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
        """Procesa los eventos de la ventana"""
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
            # Cambiar estado cuando se hace click
            estados = ["normal", "feliz", "enojado"]
            indice_actual = estados.index(self.rabbid.estado)
            nuevo_estado = estados[(indice_actual + 1) % len(estados)]
            self.rabbid.cambiar_estado(nuevo_estado)
            print(f"Rabbid ahora está: {nuevo_estado}")
    
    def actualizar(self):
        """Actualiza la lógica del juego"""
        self.rabbid.actualizar()
    
    def dibujar(self):
        """Dibuja todo en la pantalla"""
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
        fuente = pygame.font.Font(None, 24)
        info = self.rabbid.obtener_info()
        texto = fuente.render(
            f"Estado: {info['estado']} | Pos: ({info['x']:.0f}, {info['y']:.0f})",
            True,
            (255, 255, 255)
        )
        self.pantalla.blit(texto, (10, 10))
    
    def ejecutar(self):
        """Loop principal del juego"""
        print("🎮 Iniciando juego...")
        print("Haz click en el Rabbid para cambiar su estado")
        print("Cierra la ventana para salir")
        
        while not self.hecho:
            self.procesar_eventos()
            self.actualizar()
            self.dibujar()
            self.reloj.tick(self.fps)
        
        self.cerrar()
    
    def cerrar(self):
        """Cierra el juego de forma limpia"""
        print("\n👋 ¡Hasta luego!")
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    juego = Juego()
    juego.ejecutar()
