import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Configuraciones generales para las imágenes
plt.rcParams['figure.figsize'] = (8, 6)

# CREAR UNA CARPETA DIRECTA EN EL DISCO C QUE NO TENGA RESTRICCIONES DE ONEDRIVE
BASE_DIR = Path("C:/imagenes_calculo")
BASE_DIR.mkdir(parents=True, exist_ok=True) # Crea la carpeta automáticamente si no existe

print(f"[ENTORNO] Las imágenes se guardarán de forma segura en: {BASE_DIR}")


# ============================================================================
# FIGURA 1: Campo vectorial + curva (Ejercicio 1)
# ============================================================================
def generar_figura_green():
    print("[INFO] Generando Figura 1: fig_green.png...")
    
    x = np.linspace(-3, 3, 20)
    y = np.linspace(-3, 3, 20)
    X, Y = np.meshgrid(x, y)
    
    U = X**2 - Y**3
    V = X**3 + Y**2
    M = np.sqrt(U**2 + V**2)
    
    fig, ax = plt.subplots()
    quiver = ax.quiver(X, Y, U, V, M, cmap='viridis', angles='xy', scale_units='xy', scale=25)
    fig.colorbar(quiver, label='Magnitud del Campo |F|')
    
    t = np.linspace(0, 2*np.pi, 200)
    ax.plot(2*np.cos(t), 2*np.sin(t), color='red', linewidth=2, label=r'Curva $C: x^2 + y^2 = 4$')
    ax.annotate('', xy=(-0.1, 2.0), xytext=(0.1, 2.0), arrowprops=dict(arrowstyle="->", color="red", lw=2))
    
    ax.set_title("Teorema de Green: Campo Vectorial y Curva C", fontsize=12, fontweight='bold')
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(loc='upper right')
    ax.set_aspect('equal')
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3.5, 3.5)
    
    # Guardado seguro con pathlib
    ruta_final = BASE_DIR / "fig_green.png"
    plt.savefig(str(ruta_final), dpi=150, bbox_inches='tight')
    plt.close()


# ============================================================================
# FIGURA 2: Curvas de nivel + gradiente (Ejercicio 2)
# ============================================================================
def generar_figura_potencial():
    print("[INFO] Generando Figura 2: fig_potencial.png...")
    
    x = np.linspace(-0.5, 1.8, 30)
    y = np.linspace(-0.5, 2.5, 30)
    X, Y = np.meshgrid(x, y)
    Z = (X**2) * Y
    
    fig, ax = plt.subplots()
    cp = ax.contourf(X, Y, Z, levels=15, cmap='coolwarm', alpha=0.6)
    fig.colorbar(cp, label=r'Potencial $\phi(x,y) = x^2y$')
    lineas = ax.contour(X, Y, Z, levels=15, colors='black', linewidths=0.5)
    ax.clabel(lineas, inline=True, fontsize=8)
    
    x_g = np.linspace(-0.2, 1.5, 12)
    y_g = np.linspace(-0.2, 2.2, 12)
    X_G, Y_G = np.meshgrid(x_g, y_g)
    ax.quiver(X_G, Y_G, 2*X_G*Y_G, X_G**2, color='teal', alpha=0.8, scale=15, label=r'Gradiente $\nabla\phi$')
    
    ax.plot(0, 0, marker='*', color='gold', markersize=12, markeredgecolor='black', linestyle='None', label='Punto A (0,0)')
    ax.plot(1, 2, marker='*', color='orange', markersize=12, markeredgecolor='black', linestyle='None', label='Punto B (1,2)')
    
    ax.set_title("Campo Conservativo: Curvas de Nivel y Gradiente", fontsize=12, fontweight='bold')
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.grid(True, linestyle='--', alpha=0.3)
    ax.legend(loc='upper left')
    
    # Guardado seguro con pathlib
    ruta_final = BASE_DIR / "fig_potencial.png"
    plt.savefig(str(ruta_final), dpi=150, bbox_inches='tight')
    plt.close()


# ============================================================================
# FIGURA 3: Superficie 3D + borde (Ejercicio 3)
# ============================================================================
def generar_figura_stokes():
    print("[INFO] Generando Figura 3: fig_stokes.png...")
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    
    r = np.linspace(0, 2, 50)
    theta = np.linspace(0, 2*np.pi, 50)
    R, THETA = np.meshgrid(r, theta)
    
    X_s = R * np.cos(THETA)
    Y_s = R * np.sin(THETA)
    Z_s = np.zeros_like(X_s)
    
    ax.plot_surface(X_s, Y_s, Z_s, color='purple', alpha=0.3)
    
    t = np.linspace(0, 2*np.pi, 100)
    ax.plot(2*np.cos(t), 2*np.sin(t), np.zeros_like(t), color='red', linewidth=2.5, label='Borde C')
    ax.quiver(0, 0, 0, 0, 0, 1.5, color='darkviolet', linewidth=2, arrow_length_ratio=0.2, label='Normal n = k')
    
    ax.view_init(elev=25, azim=45)
    ax.set_title("Teorema de Stokes: Superficie S y Vector Normal", fontsize=12, fontweight='bold')
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_zlabel("Eje Z")
    ax.set_zlim(0, 2)
    ax.legend(loc='upper right')
    
    # Guardado seguro con pathlib
    ruta_final = BASE_DIR / "fig_stokes.png"
    plt.savefig(str(ruta_final), dpi=150, bbox_inches='tight')
    plt.close()


# ============================================================================
# EXECUTION
# ============================================================================
if __name__ == "__main__":
    print("=== INICIANDO MOTOR DE VISUALIZACIÓN VECTORIAL ===")
    generar_figura_green()
    generar_figura_potencial()
    generar_figura_stokes()
    print("=== PROCESO FINALIZADO CON ÉXITO: 3 IMÁGENES GUARDADAS ===")