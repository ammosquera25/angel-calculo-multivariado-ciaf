import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Reto 3: App Interactiva - Teorema de Green")
st.write("Modifica el slider para recalcular el área y redimensionar el círculo sobre el campo en tiempo real.")

# Parámetro interactivo
R = st.slider("Ajustar Radio (R)", min_value=0.5, max_value=4.0, value=2.0, step=0.1)

# Ecuación dinámica del resultado analítico dada por el ejercicio
resultado_green = 24 * np.pi * (R**4) / 16
st.metric(label="Resultado Integral de Green (24π * R⁴ / 16)", value=f"{resultado_green:.4f}")

# Re-renderizado de la gráfica según el slider
fig, ax = plt.subplots(figsize=(6, 5))
x = np.linspace(-4.5, 4.5, 15)
y = np.linspace(-4.5, 4.5, 15)
X, Y = np.meshgrid(x, y)

# Campo vectorial del ejercicio base
U = X**2 - Y**2
V = 3 * (X**2) * Y
ax.quiver(X, Y, U, V, color='cornflowerblue', alpha=0.6)

# Frontera circular dinámica
t = np.linspace(0, 2*np.pi, 200)
ax.plot(R * np.cos(t), R * np.sin(t), color='crimson', linewidth=2.5, label=f'Círculo (R = {R})')

ax.set_xlim(-4.5, 4.5)
ax.set_ylim(-4.5, 4.5)
ax.set_aspect('equal')
ax.legend()
ax.grid(True, alpha=0.2)

st.pyplot(fig)