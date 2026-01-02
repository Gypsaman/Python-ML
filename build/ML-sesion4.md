---
title: Generalización, Sobreajuste y Conceptos Modernos en Redes Neuronales"
author: "Cesar Garcia"
date: "2025"
lang: es
theme: "Madrid"
header-includes:
  - \usepackage{tikz}
  - \usetikzlibrary{arrows.meta}
---

# Introducción
## Objetivos de la sesión
- Comprender qué es generalización y por qué es importante.
- Diferenciar entre sobreajuste y subajuste.
- Conocer técnicas de regularización.
- Explorar la importancia de los datos y su preparación.
- Introducir arquitecturas modernas (CNN, RNN, Transformers).
- Integrar todos los conceptos en un flujo completo de ML.

---

# Generalización
## Concepto
Generalizar significa que el modelo aprende patrones reales del problema y no simplemente memoriza los datos.

## Analogía
- Estudiante que memoriza → falla en el examen.
- Estudiante que comprende → aplica el conocimiento en nuevos casos.

---

# Sobreajuste y Subajuste
## Sobreajuste (Overfitting)
Ocurre cuando el modelo aprende demasiado bien los datos de entrenamiento, incluso el ruido.

### Señales
- Pérdida baja en entrenamiento.
- Pérdida alta en validación.

## Subajuste (Underfitting)
El modelo no tiene suficiente capacidad para aprender el patrón.

### Señales
- Pérdida alta en entrenamiento y validación.

---

# Técnicas para Evitar Sobreajuste
## Regularización L2
Añade una penalización a pesos grandes para evitar complejidad excesiva.

## Dropout
Desactiva aleatoriamente neuronas durante entrenamiento para evitar dependencia excesiva.

## Early Stopping
Detiene el entrenamiento cuando la pérdida de validación deja de mejorar.

## Aumentación de Datos
Transformaciones en imágenes, texto o audio para generar variaciones artificiales.

---

# Importancia de los Datos
## Calidad sobre cantidad
Mejores datos → mejores modelos.

## Procesamiento de datos
### Normalización
Escalar valores a un rango común.

### Estandarización
Ajustar datos a media 0 y desviación estándar 1.

### Balanceo
Evitar clases desbalanceadas para mejorar precisión del modelo.

---

# Batch Processing y Optimizadores Modernos
## Revisión de batch y mini-batch
Permiten un entrenamiento más eficiente y estable.

## Optimizadores avanzados
### Momentum
Acumula velocidad para acelerar el descenso.

### Adam
Adaptativo, eficiente y el más usado en la práctica moderna.

---

# Optimizadores Basados en Gradiente

## Momentum

El optimizador **Momentum** mejora el descenso de gradiente clásico acumulando una *velocidad* que incorpora información de gradientes pasados.

## Intuición
- Similar a empujar una bola cuesta abajo.
- Aumenta la velocidad en direcciones consistentes.
- Reduce oscilaciones en regiones con pendientes pronunciadas.

---

## Formulación
Sea $L(\theta)$ la función de pérdida:

- Velocidad:
  $$
  v_t = \beta v_{t-1} + \eta \nabla L(\theta)
  $$

- Actualización de parámetros:
  $$
  \theta = \theta - v_t
  $$

Donde: 

- $\beta$ es el coeficiente de momentum (típicamente 0.9)  
- $\eta$ es la tasa de aprendizaje  

---

## Ventajas
- Convergencia más rápida que SGD estándar.
- Menor sensibilidad al ruido.
- Mejor comportamiento en valles estrechos.

---

---

# RMSProp (Root Mean Square Propagation)

**RMSProp** es un optimizador adaptativo diseñado para resolver los problemas de tasas de aprendizaje inestables en descenso de gradiente estándar.

## Intuición
- Ajusta automáticamente la tasa de aprendizaje **por parámetro**.
- Reduce el paso en direcciones con gradientes grandes.
- Aumenta el paso en direcciones con gradientes pequeños.
- Evita oscilaciones y pasos demasiado agresivos.

## Idea clave
En lugar de usar una tasa de aprendizaje fija, RMSProp divide el gradiente por una media móvil de su magnitud.

---

## Formulación
Sea $g_t = \nabla L(\theta)$:

- Media móvil del gradiente al cuadrado:
  $$
  v_t = \beta v_{t-1} + (1 - \beta) g_t^2
  $$

- Actualización de parámetros:
  $$
  \theta = \theta - \frac{\eta}{\sqrt{v_t} + \epsilon} g_t
  $$

Donde:
- $\beta$ controla la memoria (típicamente 0.9)
- $\eta$ es la tasa de aprendizaje
- $\epsilon$ evita divisiones por cero

---

## Ventajas
- Entrenamiento más estable que SGD.
- Buen desempeño en problemas no estacionarios.
- Menor sensibilidad a la elección de $\eta$.

## Uso práctico
RMSProp es común en:
- Redes recurrentes (RNN, LSTM)
- Problemas con gradientes ruidosos
- Entrenamientos donde SGD es inestable


---

# Adam (Adaptive Moment Estimation)

**Adam** combina las ideas de **Momentum** y **RMSProp**, ajustando automáticamente la tasa de aprendizaje para cada parámetro.

## Intuición
- Mantiene memoria del **promedio del gradiente** (primer momento).
- Mantiene memoria de la **varianza del gradiente** (segundo momento).
- Ajusta el tamaño del paso de manera adaptativa.

---

## Componentes
- Primer momento (media):
  $$
  m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t
  $$

- Segundo momento (varianza):
  $$
  v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2
  $$

- Corrección de sesgo y actualización de parámetros:
  $$
  \theta = \theta - \frac{\eta}{\sqrt{\hat{v}_t} + \epsilon} \hat{m}_t
  $$

### Valores típicos
- $\beta_1 = 0.9$
- $\beta_2 = 0.999$
- $\epsilon = 10^{-8}$

---

### Ventajas
- Muy estable numéricamente.
- Funciona bien con datos ruidosos.
- Requiere poco ajuste manual.

### Uso práctico
Es el **optimizador por defecto** en la mayoría de frameworks modernos como **PyTorch** y **TensorFlow**.


---

# Flujo Completo de un Proyecto de Machine Learning
1. Recolección de datos  
2. Limpieza y procesamiento  
3. División en entrenamiento/validación  
4. Selección de modelo  
5. Entrenamiento (épocas, batch, optimización)  
6. Evaluación  
7. Regularización y ajuste final  
8. Implementación  


