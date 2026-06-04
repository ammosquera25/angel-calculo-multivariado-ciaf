import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider  # Herramienta nativa de sliders en Matplotlib

def actualizar_grafico(val):
    """Función que se ejecuta automáticamente cada vez que mueves el slider"""
    R_actual = slider_radio.val  # Lee el valor del slider
    
    # Recalcula el resultado analítico dinámico dado por el ejercicio
    resultado_green = 24 * np.pi * (R_actual**4) / 16
    
    # Actualiza los datos de la curva del círculo rojo
    linea_circulo.set_data(R_actual * np.cos(t), R_actual * np.sin(t))
    
    # Actualiza el título dinámicamente con los nuevos valores
    ax.set_title(f"Teorema de Green (Interactivo)\nRadio R = {R_actual:.1f} | Integral = {resultado_green:.2f}", 
                 fontsize=11, fontweight='bold')
    
    # Redibuja el lienzo de la ventana
    fig.canvas.draw_idle()

if __name__ == "__main__":
    print("=== INICIANDO RETO 3: ALTERNATIVA INTERACTIVA LOCAL ===")
    
    # Configurar el lienzo de la ventana y dejar espacio abajo para el slider
    fig, ax = plt.subplots(figsize=(7, 6))
    plt.subplots_adjust(bottom=0.2)  # Reserva el 20% inferior para los controles
    
    # 1. Dibujar el Campo Vectorial Base (Fijo de fondo)
    x = np.linspace(-4.5, 4.5, 15)
    y = np.linspace(-4.5, 4.5, 15)
    X, Y = np.meshgrid(x, y)
    U = X**2 - Y**2
    V = 3 * (X**2) * Y
    ax.quiver(X, Y, U, V, color='cornflowerblue', alpha=0.5)
    
    # 2. Dibujar el Círculo de Frontera Inicial (Para R = 2.0 por defecto)
    R_inicial = 2.0
    t = np.linspace(0, 2 * np.pi, 200)
    linea_circulo, = ax.plot(R_inicial * np.cos(t), R_inicial * np.sin(t), 
                             color='crimson', linewidth=2.5, label='Frontera C (Círculo)')
    
    # Parámetros estéticos del plano cartesiano
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-4.5, 4.5)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.2)
    ax.legend(loc='upper right')
    
    # Título dinámico inicial
    res_inicial = 24 * np.pi * (R_inicial**4) / 16
    ax.set_title(f"Teorema de Green (Interactivo)\nRadio R = {R_inicial:.1f} | Integral = {res_inicial:.2f}", 
                 fontsize=11, fontweight='bold')
    
    # 3. Crear el Slider Nativo en la parte inferior de la ventana
    # [izquierda, abajo, ancho, alto]
    ejes_slider = plt.axes([0.2, 0.05, 0.6, 0.03])
    slider_radio = Slider(
        ax=ejes_slider,
        label='Ajustar Radio (R) ',
        valmin=0.5,
        valmax=4.0,
        valinit=R_inicial,
        valstep=0.1,
        color='crimson'
    )
    
    # Enlazar el movimiento del slider con la función de actualización
    slider_radio.on_changed(actualizar_grafico)
    
    print("¡Ventana activa! Mueve el slider rojo para ver los cambios en tiempo real.")
    plt.show()  # Muestra la interfaz interactiva local