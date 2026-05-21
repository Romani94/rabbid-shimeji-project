# Rabbid Shimeji Project 🐰

## Descripción
Proyecto de **Programación Orientada a Objetos (POO)** que implementa un personaje Shimeji estilo Rabbid que aparece en tu pantalla.

## Conceptos OOP Demostrados

### Clase `Rabbid` (rabbid.py)
- **Encapsulación**: Los datos del Rabbid (x, y, estado, etc.) están protegidos en la clase
- **Atributos**: Propiedades que definen el estado del Rabbid
- **Métodos**: Funciones que el Rabbid puede realizar
- **Métodos Privados**: `_obtener_color_estado()` (comienzan con `_`)

### Clase `Juego` (main.py)
- **Instanciación**: Crea objetos (Rabbid, pantalla, reloj)
- **Composición**: El Juego contiene un Rabbid
- **Métodos de Inicialización**: `__init__()`
- **Métodos Mágicos**: `__str__()`

## Requisitos

### Windows
```bash
pip install -r requirements.txt
```

### Mac/Linux
```bash
pip install pygame
# (Sin transparencia, solo en Windows)
```

## Cómo Ejecutar

```bash
python main.py
```

## Características

✅ Ventana sin bordes  
✅ Transparencia (Windows)  
✅ Click interactivo en el Rabbid  
✅ Cambio de estados (normal, feliz, enojado)  
✅ Información en tiempo real  

## Estructura del Proyecto

```
rabbid-shimeji-project/
├── main.py           # Punto de entrada, loop principal
├── rabbid.py         # Clase Rabbid (OOP)
├── requirements.txt  # Dependencias
└── README.md         # Este archivo
```

## Cómo Interactuar

1. **Abre el juego**: `python main.py`
2. **Haz click en el Rabbid** para cambiar su estado
3. **Cierra la ventana** para salir

## Próximas Mejoras

- [ ] Agregar movimiento/bounce
- [ ] Animaciones con sprites
- [ ] Múltiples Rabbids
- [ ] Sonidos
- [ ] Persistencia de datos

## Créditos

- **Estudiante**: Romani94
- **Proyecto**: Escuela - Programación Orientada a Objetos
- **Tecnologías**: Python, Pygame

---

**Autor**: Romani94  
**Fecha**: 2026-05-21
