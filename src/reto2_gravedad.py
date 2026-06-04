import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# 1. DEFINICIÓN DE LA RUTA (Asegurando formato raw string)
BASE_DIR = Path(".")

# Fuerza la creación de la carpeta y de todas las carpetas superiores si no existen
BASE_DIR = Path(".")

if __name__ == "__main__":
    print("=== RETO 2: CAMPO GRAVITACIONAL CONSERVATIVO ===")
    
    phi = lambda x, y, z: -9.8 * z
    A = (0, 0, 10)
    B = (5, 3, 0)
    
    # Trabajo analítico independiente del camino
    W_potencial = phi(*B) - phi(*A)
    print(f"Trabajo neto calculado (phi(B) - phi(A)): {W_potencial:.2f} J")
    
    # Discretización para los caminos
    t = np.linspace(0, 1, 100)
    
    # Camino 1: Línea recta
    x_recta = A[0] + (B[0] - A[0]) * t
    y_recta = A[1] + (B[1] - A[1]) * t
    z_recta = A[2] + (B[2] - A[2]) * t
    
    # Camino 2: Parábola en 3D
    x_para = A[0] + (B[0] - A[0]) * t
    y_para = A[1] + (B[1] - A[1]) * t
    z_para = 10 - 10 * (t**2)
    
    # Renderizado Gráfico 3D
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    
    ax.plot(x_recta, y_recta, z_recta, color='dodgerblue', linewidth=2.5, label='Camino 1: Recta')
    ax.plot(x_para, y_para, z_para, color='deeppink', linewidth=2.5, linestyle='--', label='Camino 2: Parábola')
    ax.scatter(*A, color='red', s=60, label='Inicio A (0,0,10)')
    ax.scatter(*B, color='green', s=60, label='Fin B (5,3,0)')
    
    ax.set_title("Independencia del Camino en Campo Conservativo", fontsize=11, fontweight='bold')
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_zlabel("Eje Z")
    ax.legend()
    
    # Guardado directo en la carpeta actual
    ruta_archivo = BASE_DIR / "fig_reto_gravedad.png"
    plt.savefig(str(ruta_archivo), dpi=150, bbox_inches='tight')
    plt.close()
    
    print(f"¡Éxito! Gráfica 3D guardada como: {ruta_archivo.resolve()}")