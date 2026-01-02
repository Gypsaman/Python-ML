---
title: "Stage 2 — Fundamentos del Deep Learning en la Práctica"
subtitle: "Del mapa conceptual a la implementación real"
author: "Cesar Garcia"
date: "2025"
lang: es
theme: "Madrid"
---

# Stage 2 — Overview

Stage 2 construye los **fundamentos conceptuales y mecánicos** del deep learning moderno.
El objetivo es pasar de la intuición teórica a una comprensión clara de **cómo y por qué el entrenamiento funciona en la práctica**, preparando al estudiante para implementar redes neuronales reales en PyTorch.

---

## Session 1 — Generalización y Panorama del Deep Learning

**Goal**  
Establecer el marco mental correcto sobre qué significa *aprender* en machine learning y cuál es el objetivo real del entrenamiento.

**Topics**
- Qué significa que un modelo aprenda
- Generalización vs memorización
- Sobreajuste (overfitting)
- Subajuste (underfitting)
- Importancia del rendimiento en validación
- Rol de los datos:
  - calidad vs cantidad
  - normalización y estandarización
  - balanceo de clases
- Flujo general de un proyecto de ML
- Panorama de arquitecturas:
  - redes densas
  - autoencoders
  - CNNs
  - RNNs / LSTM
  - Transformers
- Panorama de optimizadores:
  - SGD
  - Momentum
  - RMSProp
  - Adam

**Hands-On**
- Discusión guiada de casos de sobreajuste y subajuste
- Análisis conceptual de proyectos de ML reales

**Key Concept**  
> El objetivo del entrenamiento no es minimizar la pérdida en entrenamiento, sino **generalizar**.

---

## Session 2 — Tensores, Autograd y Grafos Computacionales

**Goal**  
Desmitificar el cálculo automático de gradientes y explicar cómo PyTorch implementa backpropagation.

**Topics**
- Tensores como objetos matemáticos (0D → ND)
- Diferencias entre tensores y arrays de NumPy
- Gradientes como sensibilidad local
- Por qué las derivadas manuales no escalan
- Autograd:
  - registro de operaciones
  - construcción dinámica del grafo computacional
- Regla de la cadena aplicada a grafos
- Forward pass vs backward pass
- Interpretación de `.backward()`

**Hands-On**
- Cálculo de gradientes simples con `requires_grad`
- Comparación entre gradiente manual y autograd
- Visualización conceptual de un grafo computacional

**Key Concept**  
> Backpropagation es **recorrido de un grafo**, no magia.

---

## Session 3 — Building a Neural Network from Scratch (Low-Level)

**Goal**  
Entender cada componente interno de una red neuronal sin abstracciones de alto nivel.

**Topics**
- Capas lineales como multiplicación matricial
- Bias
- Funciones de activación
- Forward pass manual
- Funciones de pérdida
- Descenso de gradiente explícito

**Hands-On**
- Implementación manual de una red de una capa
- Entrenamiento con bucle explícito

**Constraint**  
- No usar `nn.Module` ni optimizadores de PyTorch

---

## Session 4 — PyTorch `nn.Module` & Training Loop

**Goal**  
Transicionar de implementación manual a PyTorch idiomático.

**Topics**
- `nn.Module`
- Método `forward`
- Funciones de pérdida en PyTorch
- Optimizadores (`SGD`, `Adam`)
- Ciclo de entrenamiento estándar

**Hands-On**
- Reescribir el modelo de la sesión 3 usando `nn.Module`
- Comparar claridad y mantenimiento del código

**Key Concept**  
> PyTorch abstrae, pero no esconde el mecanismo.

---

## Session 5 — Classification & Decision Boundaries

**Goal**  
Conectar matemáticas, visualización y comportamiento del modelo.

**Topics**
- Clasificación binaria vs multiclase
- Sigmoid y Softmax
- Entropía cruzada
- Fronteras de decisión

**Hands-On**
- Dataset sintético en 2D
- Visualización de fronteras de decisión durante el entrenamiento

---

## Session 6 — Data Pipelines & Datasets

**Goal**  
Introducir el manejo realista de datos en proyectos de ML.

**Topics**
- `Dataset` y `DataLoader`
- Mini-batches
- Shuffling
- División entrenamiento / validación
- Normalización

**Hands-On**
- Implementación de un `Dataset` personalizado
- Entrenamiento con distintos tamaños de batch

---

## Session 7 — Optimization Deep Dive

**Goal**  
Hacer el entrenamiento predecible y diagnosticable.

**Topics**
- Learning rate
- Momentum
- RMSProp
- Adam
- Inicialización de pesos

**Hands-On**
- Comparación de optimizadores en el mismo modelo
- Visualización de curvas de pérdida

**Key Concept**  
> Muchos problemas de entrenamiento son problemas de optimización, no de arquitectura.

---

## Session 8 — Regularization & Generalization (in Code)

**Goal**  
Traducir la teoría de generalización a código real.

**Topics**
- Sobreajuste en la práctica
- Regularización L2
- Dropout
- Early stopping

**Hands-On**
- Forzar sobreajuste intencionalmente
- Aplicar técnicas de regularización
- Comparar métricas de validación

---

## Session 9 — Convolutional Neural Networks (CNNs)

**Goal**  
Introducir arquitecturas profundas reales para visión.

**Topics**
- Convoluciones
- Filtros y mapas de activación
- Pooling
- Arquitecturas CNN básicas

**Hands-On**
- Clasificación de imágenes (MNIST o CIFAR-10)
- Visualización de filtros aprendidos

---

## Session 10 — Sequence Models (RNNs → LSTMs → Attention)

**Goal**  
Introducir el aprendizaje en datos secuenciales.

**Topics**
- Limitaciones de redes feedforward
- RNNs
- LSTMs
- Introducción a atención

**Hands-On**
- Predicción de secuencias simples
- Comparación RNN vs LSTM

---

## Session 11 — Transformers & Modern Deep Learning

**Goal**  
Comprender el paradigma dominante del deep learning moderno.

**Topics**
- Self-attention
- Arquitectura Transformer
- Encoder / Decoder
- Casos de uso en NLP y visión

**Hands-On**
- Uso de un modelo Transformer preentrenado
- Inferencia y tokenización

---

## Session 12 — TensorFlow / Keras Overview & Course Wrap-Up

**Goal**  
Exponer al ecosistema completo y cerrar el curso.

**Topics**
- PyTorch vs TensorFlow
- Filosofía de Keras
- Consideraciones de despliegue
- Revisión del flujo completo de ML

**Hands-On**
- Reimplementar un modelo simple en Keras
- Comparación de APIs

**Key Concept**  
> PyTorch enseña cómo funciona ML; TensorFlow muestra cómo se despliega ML.

---

# Stage 2 Outcome

Al finalizar Stage 2, el estudiante:
- entiende **qué significa generalizar**
- comprende **cómo se calculan gradientes**
- puede implementar y entrenar redes neuronales con criterio técnico
