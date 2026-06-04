import pytest
import numpy as np
import scipy.integrate as integrate

# Definimos las funciones del motor matemático que vamos a probar
def calcular_green_numerico(R):
    """Calcula la integral doble del Teorema de Green para un radio dado"""
    # Integrando en polares: (6r^2 * cos(t) * sin(t) + 2r * sin(t)) * r
    integrando = lambda r, t: (6 * (r**2) * np.cos(t) * np.sin(t) + 2 * r * np.sin(t)) * r
    val_num, _ = integrate.dblquad(integrando, 0, 2 * np.pi, lambda r: 0, lambda r: R)
    return val_num

def calcular_trabajo_gravitacional(zA, zB):
    """Calcula el trabajo neto en un campo conservativo uniforme"""
    # F_z = -9.8, Trabajo = F_z * delta_z = -9.8 * (zB - zA)
    return -9.8 * (zB - zA)


# =====================================================================
# PRUEBAS UNITARIAS AUTOMATIZADAS (Se ejecutan con Pytest)
# =====================================================================

def test_teorema_green_simetria():
    """Prueba que la integral de Green en un periodo completo de 0 a 2pi dé 0 por simetría"""
    resultado = calcular_green_numerico(R=2.0)
    # Al ser numérico, puede dar un número extremadamente cercano a 0 (ej: 1e-16)
    # pytest.approx nos ayuda a tolerar esos mini decimales de precisión de la PC
    assert resultado == pytest.approx(0.0, abs=1e-9)

def test_campo_conservativo_trabajo():
    """Prueba que el trabajo de A(z=10) a B(z=0) sea exactamente 98.0 J"""
    resultado = calcular_trabajo_gravitacional(zA=10, zB=0)
    assert resultado == 98.0

def test_campo_conservativo_camino_cerrado():
    """Prueba física: En un campo conservativo, el trabajo en un camino cerrado (volver al inicio) debe ser 0"""
    resultado = calcular_trabajo_gravitacional(zA=10, zB=10)
    assert resultado == 0.0