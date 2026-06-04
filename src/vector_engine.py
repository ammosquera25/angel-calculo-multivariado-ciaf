import numpy as np
from scipy import integrate
from scipy.integrate import trapezoid

# Integrantes: [Nombres]    Grupo: [Número]    CIAF 2026

# ============================================================================
# EJERCICIO 1: Teorema de Green - Ejercicio 1
# ============================================================================
def green_circulo(R=2.0):
    """
    Calcula la integral de Green de (x^2 - y^2)dx + (x^3 + y^2)dy sobre un círculo de radio R.
    Utiliza el método numérico de integración doble en coordenadas polares.

    Parámetros:
    -----------
    R : float
        Radio del círculo (debe ser mayor o igual a cero).

    Retorna:
    --------
    float
        Resultado de la integral doble (numérico).
    """
    if R < 0:
        raise ValueError("El radio no puede ser negativo.")

    # Integral doble en polares: 3*r^2 * r dr dtheta
    def integrando(r, theta):
        return 3 * r**2 * r  # 3*r^2 (de la función) * r (del jacobiano)

    # integrate.dblquad toma (funcion, lim_inf_x, lim_sup_x, lim_inf_y, lim_sup_y)
    # Para theta (0 a 2pi) y r (0 a R)
    resultado, _ = integrate.dblquad(
        integrando,
        0, 2 * np.pi,      # Límites de theta
        lambda x: 0, lambda x: R  # Límites de r (funciones en dblquad)
    )

    analitico = 24 * np.pi  # Valor analítico para R=2
    # Si R no es 2, recalculamos el analítico proporcional a R^4 para la tabla general
    analitico_dinamico = (3/2) * np.pi * (R**4)

    print(f"[GREEN] Analítico (R={R}): {analitico_dinamico:.6f}")
    print(f"[GREEN] Numérico:          {resultado:.6f}")
    print(f"[GREEN] Error:             {abs(resultado - analitico_dinamico):.2e}")
    
    return resultado


# ============================================================================
# EJERCICIO 2: Campo conservativo - Ejercicio 2
# ============================================================================
def campo_conservativo(A=(0, 0, 0), B=(1, 2, 1)):
    """
    Para F = (2*x*y*z - 2, x^2*z, x^2*y).
    Verifica la conservatividad en un punto de prueba y calcula W = phi(B) - phi(A).

    Parámetros:
    -----------
    A : tuple
        Punto inicial (x, y, z).
    B : tuple
        Punto final (x, y, z).

    Retorna:
    --------
    float
        Trabajo realizado por el campo (phi(B) - phi(A)).
    """
    def phi(x, y, z):
        return (x**2) * y * z - 2 * x  # Función potencial matemática

    # Verificar curl F = 0 en un punto de prueba (1,1,1)
    x0, y0, z0 = 1.0, 1.0, 1.0
    curl_i = x0**2 - x0**2               
    curl_j = 2*x0*y0 - 2*x0*y0           
    curl_k = 2*x0*z0 - 2*x0*z0           
    
    es_conservative = (curl_i == 0 and curl_j == 0 and curl_k == 0)

    # Calculamos el valor real en base a los parámetros de la función
    W = phi(B[0], B[1], B[2]) - phi(A[0], A[1], A[2])
    
    # IMPORTANTE: Cambiamos el analítico estático por el valor matemáticamente correcto (0.0)
    analitico = 0.0 

    print(f"\n[CONSERV] curl(F) = ({curl_i}, {curl_j}, {curl_k})")
    print(f"[CONSERV] Es conservativo: {es_conservative}")
    print(f"[CONSERV] phi(x,y,z) = x^2*y*z - 2*x")
    print(f"[CONSERV] W = phi(B) - phi(A) = {W:.4f} J")
    print(f"[CONSERV] Analítico: {analitico:.4f} J")
    
    return W  # <-- ASEGÚRATE DE QUE ESTA LÍNEA NO ESTÉ IDENTADA DENTRO DE "phi"


# ============================================================================
# EJERCICIO 3: Teorema de Stokes - Ejercicio 3
# ============================================================================
def stokes_circulo(R=2.0, n=800):
    """
    Para F=(z, x, y) y S: círculo x^2 + y^2 = R^2, z=0.
    Calcula por Stokes (área del disco) y por verificación directa de la integral de línea.

    Parámetros:
    -----------
    R : float
        Radio del círculo (debe ser mayor o igual a cero).
    n : int
        Número de puntos para la discretización de la curva.

    Retorna:
    --------
    float
        Resultado aproximado por el teorema de Stokes.
    """
    if R < 0:
        raise ValueError("El radio no puede ser negativo.")

    # Stokes: (curl F) . n = (1,1,1) . (0,0,1) = 1 sobre el disco
    stokes = np.pi * R**2 * 1

    # Verificación directa de la integral de línea
    t = np.linspace(0, 2 * np.pi, n)
    x = R * np.cos(t)
    y = R * np.sin(t)
    z = np.zeros(n)

    dx = np.gradient(x, t)
    dy = np.gradient(y, t)
    dz = np.zeros(n)

    # F = (z, x, y) sobre la curva
    Fx, Fy, Fz = z, x, y
    
    # Integración numérica usando la regla del trapecio
    linea = trapezoid(Fx * dx + Fy * dy + Fz * dz, t)
    analitico = 4 * np.pi if R == 2.0 else np.pi * R**2

    print(f"\n[STOKES] curl(F) = (1,1,1); n = k = (0,0,1)")
    print(f"[STOKES] (curl F).n = 1 -> integral = área disco")
    print(f"[STOKES] Stokes (área=1): {stokes:.6f}")
    print(f"[STOKES] Línea directa:   {linea:.6f}")
    print(f"[STOKES] Analítico 4*pi:  {analitico:.6f}")
    
    return stokes


# ============================================================================
# REQUERIMIENTO COMPLEMENTARIO: Tabla de Resultados (Actualizada)
# ============================================================================
def tabla_resultados():
    """
    Imprime una tabla comparativa en consola mostrando los valores analíticos,
    numéricos y el error relativo porcentual de los 3 ejercicios.
    """
    print("\n" + "="*60)
    print(f"{'EJERCICIO':<20}{'ANALÍTICO':<12}{'NUMÉRICO':<12}{'ERROR REL (%)':<12}")
    print("="*60)
    
    # Ejercicio 1 (Green)
    an1 = 24 * np.pi
    num1 = green_circulo(R=2.0)
    err1 = abs(an1 - num1) / an1 * 100
    
    # Ejercicio 2 (Conservativo) -> Cambiado a 0.0 que es el valor real
    an2 = 0.0
    num2 = campo_conservativo(A=(0,0,0), B=(1,2,1))
    err2 = abs(an2 - num2) * 100 # Evitamos división por cero ya que analítico es 0
    
    # Ejercicio 3 (Stokes)
    an3 = 4 * np.pi
    num3 = stokes_circulo(R=2.0)
    err3 = abs(an3 - num3) / an3 * 100
    
    print("\n" + "="*60)
    print(f"{'1. Green':<20}{an1:<12.4f}{num1:<12.4f}{err1:<12.4e}%")
    print(f"{'2. Conservativo':<20}{an2:<12.4f}{num2:<12.4f}{err2:<12.4e}%")
    print(f"{'3. Stokes':<20}{an3:<12.4f}{num3:<12.4f}{err3:<12.4e}%")
    print("="*60)


# ============================================================================
# MAIN & PRUEBAS UNITARIAS (Corregido)
# ============================================================================
if __name__ == "__main__":
    # 1. Demostración de manejo de errores (try/except)
    print("--- Probando Manejo de Errores con Radio Negativo ---")
    try:
        green_circulo(R=-5.0)
    except ValueError as e:
        print(f"Éxito capturando error esperado: {e}")

    # 2. Ejecutar y generar la tabla comparativa solicitada
    print("\n--- Generando Tabla Comparativa Principal ---")
    tabla_resultados()

    # 3. Pruebas Unitarias Obligatorias (Validación mediante Asserts)
    print("\n--- Ejecutando Pruebas Unitarias ---")
    
    # Prueba 1: Green
    assert abs(green_circulo(2.0) - 24 * np.pi) < 0.01, "Error en la prueba unitaria de Green"
    
    # Prueba 2: Campo Conservativo -> ¡AQUÍ YA ESTÁ COMPARANDO CONTRA 0.0!
    assert abs(campo_conservativo((0,0,0), (1,2,1)) - 0.0) < 0.01, "Error en la prueba unitaria del Campo Conservativo"
    
    # Prueba 3: Stokes
    assert abs(stokes_circulo(2.0) - 4 * np.pi) < 0.01, "Error en la prueba unitaria de Stokes"
    
    print("\n¡Perfecto! Todas las pruebas unitarias (asserts) pasaron exitosamente.")