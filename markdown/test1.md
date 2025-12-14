# Curso Revisado: Fundamentos de Machine Learning con Redes Neuronales

## Sesión 1: Introducción a ML

---
title: "Introducción a ML – Sesión 1"
author: "Cesar Garcia"
date: "2025"
lang: es
theme: "Madrid"
header-includes:
  - \usepackage{pdfpc}
  - \usepackage{tikz}
  - \usetikzlibrary{positioning,arrows.meta}
---

# Introducción

**Objetivos de la sesión**

- Comprender qué es el aprendizaje automático (Machine Learning).
- Diferenciar entre aprendizaje clásico y aprendizaje profundo.
- Identificar tipos de problemas: regresión, clasificación, clustering.
- Revisión de algoritmos clásicos: regresión lineal, KNN, árboles de decisión, SVM.

**Preview:** Esta sesión establece las bases. En la Sesión 2, veremos cómo las redes neuronales construyen sobre estos conceptos clásicos.

---

# ¿Qué es el Machine Learning?

## Definición
El Machine Learning permite a los sistemas aprender patrones a partir de datos sin ser programados explícitamente.

![Ciclo típico de Machine Learning: recolección de datos, preparación, entrenamiento, evaluación y despliegue](https://towardsdatascience.com/wp-content/uploads/2024/11/1_dlG-Cju5ke-DKp8DQ9hiA@2x.jpeg)

![Otro ejemplo del ciclo de Machine Learning](https://miro.medium.com/0*TnQc9I9EAkY076Od)

![Flujo de trabajo de un proyecto de Machine Learning](https://miro.medium.com/v2/resize:fit:1400/1*_0KYNHYB3DokiqfJWKvAGw.png)

---

# Por qué funciona el Machine Learning

- Identifica patrones multivariados complejos.
- Ejemplo: Detección de fraude en tarjetas (combinaciones de hora, monto, ubicación, etc.).

**Ejemplo numérico simple:** Predecir precio de casa con regresión lineal:  
precio = w₁ × área + w₂ × habitaciones + b  
(ej. área=100m², habitaciones=3 → cálculo manual en clase).

---

# Tipos de Problemas

![Tipos principales de Machine Learning: clasificación, regresión, clustering](https://www.researchgate.net/publication/354960266/figure/fig1/AS:11431281251915131@1718389091562/The-main-types-of-machine-learning-Main-approaches-include-classification-and-regression.tif)

![Clasificación de modelos de Machine Learning (incluyendo ejemplos)](https://miro.medium.com/v2/1*rsYYmrpN5ZMBNkIZAtnAxA.png)

| **Tarea**         | **Descripción**                  | **Ejemplo**                  |
|-------------------|----------------------------------|------------------------------|
| **Regresión**     | Predicción de valores numéricos  | Precio de casas             |
| **Clasificación** | Asignación de categorías         | Detectar spam en emails     |
| **Clustering**    | Agrupación sin etiquetas         | Segmentación de clientes    |

---

# Algoritmos Clásicos

<!-- Mantener el contenido original detallado sobre regresión lineal/polinomial, KNN, árboles de decisión, Random Forests y SVM, con pros/contras e hiperparámetros -->

## Comparación Rápida

| Modelo                | Mejor para...                       | Riesgo principal              |
|-----------------------|-------------------------------------|-------------------------------|
| Regresión Lineal      | Relaciones simples, interpretable   | Subajuste en no lineales      |
| KNN                   | Fronteras complejas                 | Lento en grandes datos        |
| Árboles/Random Forest | No linealidades e interacciones     | Sobreajuste (árbol único)     |
| SVM                   | Alta dimensión y no lineal (kernel) | Costoso en datasets grandes   |

**Actividad interactiva:** En grupos, elijan un problema real (ej. predecir notas de estudiantes) y discutan qué algoritmo clásico usarían y por qué.

---

## Sesión 2: Introducción a Redes Neuronales

<!-- Mantener TikZ originales para perceptrón, red completa, forward propagation y activaciones -->

**Adición: Ejemplo numérico (Todo es Álgebra Lineal)**

Supongamos:  
W = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, x = \begin{bmatrix} 0.5 \\ 1 \end{bmatrix}, b = \begin{bmatrix} 0.1 \\ 0.2 \end{bmatrix}

z = Wx + b = \begin{bmatrix} 3.1 \\ 6.2 \end{bmatrix}  
a = ReLU(z) = \begin{bmatrix} 3.1 \\ 6.2 \end{bmatrix}

![Comparación de funciones de activación (ReLU, Sigmoid, Tanh, etc.)](https://www.researchgate.net/publication/370949533/figure/fig3/AS:11431281160607100@1684811088451/Comparison-of-various-activation-functions.png)

![Gráficos detallados de activaciones comunes incluyendo GELU y Swish](https://miro.medium.com/v2/resize:fit:1400/1*6pa6uqH4B0Ia4FQ3WzsV_A.png)

**Cuándo usar cada función de activación**

- ReLU/Leaky ReLU: Capas ocultas (rápida, evita vanishing gradient).
- Sigmoid: Salida binaria (probabilidades 0-1).
- Tanh: Cuando se necesita centrado en cero.
- Softmax: Salida multiclase.
- GELU/Swish: Modelos modernos (Transformers, mejor gradiente).

**Actividad:** Experimenten en TensorFlow Playground variando activaciones y capas.

**Preview:** En la Sesión 3 veremos cómo las derivadas de estas activaciones permiten entrenar la red.

---

## Sesión 3: Funciones de Pérdida y Entrenamiento

<!-- Mantener contenido original de pérdidas y descenso de gradiente -->

## Importancia de las Derivadas (integrada)

Las derivadas calculan cómo cambiar los pesos para reducir la pérdida (backpropagation).

**Ejemplo simple de regla de la cadena:**  
∂L/∂W = (∂L/∂a) × f'(z) × x

Problema del *vanishing gradient* en Sigmoid/Tanh vs. ReLU (gradiente ≈1 en positivo).

![Ilustración del problema de vanishing gradient (Sigmoid vs ReLU)](https://miro.medium.com/1*1N0eEMXpqWK5B5QxmmPqXw.png)

![Trayectorias de descenso de gradiente: batch, SGD y mini-batch](https://statusneo.com/wp-content/uploads/2023/09/Credit-Analytics-Vidya.jpg)

![Convergencia comparativa de variantes de gradient descent](https://i0.wp.com/spotintelligence.com/wp-content/uploads/2024/05/batch-gradient-descent.jpg?fit=1200%2C675&ssl=1)

**Cuándo usar cada función de pérdida**

- MSE: Regresión estándar (penaliza errores grandes).
- MAE: Regresión robusta a outliers.
- BCE: Clasificación binaria.
- CCE: Clasificación multiclase (con Softmax).

**Actividad:** Comparen batch completo, mini-batch y SGD (estabilidad, ruido, velocidad) usando analogía de montaña.

**Preview:** En la Sesión 4 evitaremos problemas como sobreajuste.

---

## Sesión 4: Generalización y Arquitecturas Modernas

<!-- Mantener contenido original -->

## Sobreajuste y Subajuste

![Curvas de overfitting y underfitting (pérdida en entrenamiento vs validación)](https://storage.googleapis.com/kaggle-media/learn/images/tHiVFnM.png)

![Curvas de aprendizaje mostrando overfitting/underfitting](https://api.wandb.ai/files/mostafaibrahim17/images/projects/37042936/4cdebc09.png)

## Procesamiento de Datos

- **Normalización:** Escala características a [0,1].
- **Estandarización:** Media 0, desviación estándar 1 (ideal para algoritmos sensibles a escala como SVM).

## Arquitecturas Modernas (expandido)

- **CNN:** Detectan patrones locales (bordes → objetos) en imágenes. Usan mismas operaciones lineales + activaciones.

![Arquitectura de una Convolutional Neural Network (CNN)](https://cdn.analyticsvidhya.com/wp-content/uploads/2020/10/90650dnn2.webp)

- **RNN/LSTM:** Secuencias (texto, series temporales).
- **Transformers:** Atención para dependencias largas (usa GELU, muy eficiente). Base de GPT, BERT, etc.

![Diagrama de arquitectura Transformer con mecanismo de atención](https://www.mdpi.com/biology/biology-12-01033/article_deploy/html/images/biology-12-01033-g001.png)

**Actividad de cierre:** Reflexionen sobre un ejemplo real conectando todas las sesiones (datos → modelo → activaciones → entrenamiento → regularización → arquitectura).

**Conclusión del curso:** Todas las arquitecturas modernas se basan en los principios básicos vistos (pesos, forward/backward, pérdidas).