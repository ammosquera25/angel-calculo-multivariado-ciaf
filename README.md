# Motor Vectorial y Visualización - Cálculo Multivariado

## 👥 Integrantes del Grupo
* **Integrante:** [ANGEL MAURICIO MOSQUERA MOSQUERA] - ID: [1.004.720.043]
* **Profesor:** Aimer A. Rivas Montoya
* **Asignatura:** Cálculo Multivariado — Proyecto Integrador Final (CIAF 2026)

---

## 📝 Descripción del Proyecto
Este proyecto consiste en un **Motor Vectorial en Python** que computa numéricamente integrales de línea y dobles asociadas a teoremas fundamentales del cálculo vectorial: el **Teorema de Green**, el análisis de **Campos Conservativos**, y el **Teorema de Stokes**. Adicionalmente, el sistema incluye módulos de visualización en 2D y 3D, pruebas unitarias automatizadas y herramientas web interactivas.

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
