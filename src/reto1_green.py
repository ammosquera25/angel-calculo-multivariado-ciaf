import numpy as np
from scipy.integrate import trapezoid

def area_green(curva_func, t_range):
    """
    Calcula el área encerrada por una curva paramétrica usando la fórmula de Green:
    A = 0.5 * oint (-y dx + x dy)
    """
    t = t_range
    x, y = curva_func(t)
    
    # Derivadas numéricas respecto al parámetro t
    dx = np.gradient(x, t)
    dy = np.gradient(y, t)
    
    integrando = -y * dx + x * dy
    area_numerica = 0.5 * trapezoid(integrando, t)
    return area_numerica

if __name__ == "__main__":
    print("=== RETO 1: ÁREA CON GREEN ===")
    t = np.linspace(0, 2 * np.pi, 1000)
    
    # (a) Círculo r = 2
    circulo = lambda t: (2 * np.cos(t), 2 * np.sin(t))
    area_c_num = area_green(circulo, t)
    area_c_ana = 4 * np.pi
    err_c = abs(area_c_ana - area_c_num) / area_c_ana * 100
    print(f"[Círculo r=2]  Numérico: {area_c_num:.6f} | Analítico: {area_c_ana:.6f} | Error: {err_c:.4e}%")
    
    # (b) Elipse x = 3*cos(t), y = 2*sin(t)
    elipse = lambda t: (3 * np.cos(t), 2 * np.sin(t))
    area_e_num = area_green(elipse, t)
    area_e_ana = 6 * np.pi
    err_e = abs(area_e_ana - area_e_num) / area_e_ana * 100
    print(f"[Elipse 3x2]   Numérico: {area_e_num:.6f} | Analítico: {area_e_ana:.6f} | Error: {err_e:.4e}%")