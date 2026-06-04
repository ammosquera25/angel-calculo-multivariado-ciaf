# Motor Vectorial y Visualización - Cálculo Multivariado

## 👥 Integrantes del Grupo
* **Integrante:** [ANGEL MAURICIO MOSQUERA MOSQUERA] - ID: [1.004.720.043]
* **Profesor:** Aimer A. Rivas Montoya
* **Asignatura:** Cálculo Multivariado — Proyecto Integrador Final (CIAF 2026)

---

## 📝 Descripción del Proyecto
Este proyecto consiste en un **Motor Vectorial en Python** que computa numéricamente integrales de línea y dobles asociadas a teoremas fundamentales del cálculo vectorial: el **Teorema de Green**, el análisis de **Campos Conservativos**, y el **Teorema de Stokes**. Adicionalmente, el sistema incluye módulos de visualización en 2D y 3D, pruebas unitarias automatizadas y herramientas web interactivas.

---

## 🧠 Análisis Técnico de los Retos y Resultados

A continuación, se presenta la sustentación física y geométrica de los resultados arrojados por el motor numérico:

### Reto 1: Teorema de Green (Integración de Frontera vs. Región)
* **El Fenómeno:** Evaluamos la integral de línea sobre una frontera cerrada circular de radio $R=2$ inmersa en el campo vectorial $\mathbf{F}(x,y) = (x^2 - y^2)\mathbf{i} + (3x^2y)\mathbf{j}$. 
* **El Resultado:** Tanto el cálculo analítico como el motor numérico arrojaron exactamente **0.0000**. 
* **Explicación Matemática:** Al aplicar el Teorema de Green, transformamos la integral de línea en una integral doble sobre la región circular del rotacional bidimensional ($\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = 6xy + 2y$). Al realizar el cambio a coordenadas polares, las componentes trigonométricas integradas en un periodo completo de $0$ a $2\pi$ resultan ser **funciones impares simétricas**, lo que provoca que las áreas positivas y negativas se cancelen mutuamente, resultando en un flujo neto nulo.

### Reto 2: Campo Gravitacional Conservativo (Trabajo e Independencia del Camino)
* **El Fenómeno:** Se calculó el trabajo neto ($W$) requerido para mover una masa dentro de un campo gravitacional uniforme cuya función de potencial es $\phi(x,y,z) = -9.8z$, desde un punto inicial $A(0,0,10)$ hasta un punto final $B(5,3,0)$.
* **El Resultado:** El trabajo neto calculado fue de **98.0000 J** con un error relativo de **0.0%**.
* **Explicación Física:** Al ser el campo gravitacional un **campo conservativo**, el trabajo es completamente independiente de la trayectoria geométrica que siga la partícula (recta, parábola o hélice). El resultado depende única y exclusivamente de la diferencia de potencial entre los puntos extremos ($W = \phi(B) - \phi(A)$). El motor numérico validó esto aproximando la integral de línea $\int \mathbf{F} \cdot d\mathbf{r}$ a través de diferenciales continuos, demostrando que la energía se conserva perfectamente en el sistema.

### Reto 3: Teorema de Stokes y Aplicación Dinámica Interactiva
* **El Fenómeno:** Se analizó el flujo del rotacional de un campo sobre una superficie abierta acotada por una frontera curva circular, evaluando el impacto del cambio del radio de la región en tiempo real.
* **El Resultado:** El sistema demostró que el valor de la integral se incrementa de forma cuártica respecto al radio ($R^4$).
* **Explicación Geométrica:** El Teorema de Stokes conecta la circulación del campo a lo largo de la frontera con el flujo del rotacional a través de la superficie. Al implementar el slider interactivo, se evidencia visualmente cómo al expandir el radio de la frontera circular, el área de la superficie abarcada crece exponencialmente, capturando una mayor cantidad de líneas del campo vectorial. Esto causa que el valor de la integral doble se recalcule de manera instantánea y ascendente en la interfaz de Streamlit, sirviendo como una herramienta pedagógica interactiva excelente.
---
## 📝 Resumen Ejecutivo del Proyecto

Este proyecto representa el desarrollo de un **Motor de Cómputo Vectorial y Plataforma de Visualización Interactiva**, diseñado para validar numéricamente los teoremas fundamentales del Cálculo Multivariado. A lo largo de la jornada de desarrollo, se lograron consolidar de manera exitosa los siguientes hitos de ingeniería de software y matemática aplicada:

1. **Precisión Matemática del Motor Numérico:** Se implementaron algoritmos de integración avanzada (utilizando cuadraturas dobles y aproximaciones trapezoidales mediante `scipy.integrate`). El motor logró resolver las integrales asociadas al **Teorema de Green**, **Campos Conservativos** y **Teorema de Stokes**, arrojando un **error relativo del 0.0000e+00%** al ser comparado directamente con los modelos analíticos resueltos a mano. Esto demuestra la estabilidad y robustez del software.

2. **Visualización y Renderizado Avanzado:** Se construyeron scripts modulares con `matplotlib` capaces de exportar de forma automatizada gráficos vectoriales en alta definición (2D y 3D) a la carpeta `/output`. Estas figuras modelan el comportamiento de campos vectoriales, curvas de frontera orientadas y superficies complejas en el espacio, garantizando la correcta interpretación geométrica de los fenómenos físicos simulados.

3. **Arquitectura y Superación de Desafíos Técnicos:** * **Migración de Código Moderno:** Se solucionaron advertencias de obsolescencia del lenguaje mediante la sustitución estratégica de comandos antiguos de integración (`np.trapz`) por las librerías estandarizadas y vigentes de la última suite de Python.
   * **Gestión de Rutas Seguras:** Se implementó el control de rutas a través de la librería estándar `pathlib`, erradicando errores sintácticos de caracteres de escape de Windows (`unicodeescape`) y logrando eludir con éxito las restricciones de bloqueo de escritura que imponen las plataformas de sincronización en la nube como OneDrive.
   * **Despliegue y Democratización:** El Reto 3 fue llevado más allá de una ejecución local, logrando su despliegue en un servidor en la nube a través de **Streamlit Community Cloud**, permitiendo a cualquier usuario evaluar el comportamiento dinámico de los campos mediante una interfaz web interactiva con controles deslizantes (*sliders*).

El software final no solo cumple con los rigores del análisis matemático, sino que adopta buenas prácticas del desarrollo profesional como la estructuración limpia de directorios, la automatización de dependencias (`requirements.txt`) y una documentación exhaustiva para el usuario final.

---

## 🚀 Aplicación Web Interactiva (Reto 3)
El Reto 3 ha sido desplegado exitosamente. Puedes probar el simulador del campo vectorial y mover el slider del radio en tiempo real haciendo clic aquí:

👉 **[Clic aquí para abrir la App en Streamlit.io](https://angel-calculo-multivariado-ciaf-yrvqoujfnb2s4dgfosdw8x.streamlit.app/)**

---

## 🛠️ Instrucciones de Instalación y Uso

### 1. Clonar el repositorio e instalar dependencias
Abre tu terminal y ejecuta:

```bash
git clone [https://github.com/ammosquera25/campos-vectoriales-ciaf.git](https://github.com/TU_USUARIO/campos-vectoriales-ciaf.git)
cd campos-vectoriales-ciaf
pip install -r requirements.txt
