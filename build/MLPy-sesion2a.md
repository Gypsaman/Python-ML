---
title: "Tensores, Autograd y Grafos Computacionales"
subtitle: "Cómo PyTorch calcula gradientes (sin magia)"
author: "Cesar Garcia"
date: "2025"
lang: es
theme: "Madrid"
header-includes:
  - \usepackage{tikz}
  - \usetikzlibrary{arrows.meta, positioning}
---

# Introducción
## Objetivos de la sesión

- Entender **cómo** PyTorch representa cálculos matemáticos
- Ver **de dónde salen los gradientes**
- Interpretar `.backward()` como recorrido de un grafo
- Preparar la implementación manual de una red neuronal

##
> ¿Qué parte del entrenamiento de una red te resulta más “mágica” hasta ahora?

---

# ¿Qué es un Tensor?
## Más que un array

Un **tensor** es una generalización matemática:

- Escalar → tensor 0D  
- Vector → tensor 1D  
- Matriz → tensor 2D  
- Tensor ND → imágenes, secuencias, lotes  
<br/><br/>  
En PyTorch, un tensor **no solo almacena datos**, también participa en un grafo.

##
> ¿Qué tipo de tensor representaría una imagen RGB de 224×224?

---

# Tensores en PyTorch
## Propiedades relevantes para deep learning

- Tienen forma (`shape`)
- Tienen tipo (`dtype`)
- Pueden vivir en CPU o GPU
- **Pueden recordar operaciones**
<br/>  
Esta “memoria” es la base del cálculo automático de gradientes.

##
> ¿Por qué un array de NumPy no es suficiente para entrenar una red neuronal?

---

# Gradientes
## Sensibilidad local

El gradiente mide:

> **Cómo cambia una salida ante cambios pequeños en un parámetro**

En aprendizaje automático:  

> Parámetros = pesos y sesgos

> Gradientes indican **cómo ajustarlos**  

<br/>
Los gradientes son **locales**, no globales.

##
> Si un gradiente es cero, ¿qué nos dice eso sobre ese parámetro?

---

# El problema clásico
## Derivadas a mano no escalan

- Redes reales tienen millones de parámetros  
- Cada parámetro requiere una derivada parcial  
- El proceso manual es **inviable en la práctica**  
<br/>
Necesitamos un sistema automático y confiable.

##
> ¿El problema es matemático o práctico? ¿Por qué?

---

# Autograd
## Diferenciación automática en PyTorch

Autograd es el sistema que:

1. Registra operaciones matemáticas
2. Construye un **grafo computacional**
3. Aplica la **regla de la cadena**

El grafo se construye **dinámicamente**, mientras el código se ejecuta.

##
> ¿Por qué es importante que el grafo sea dinámico y no fijo?

---

# Grafo Computacional

## Formula

$$d = a \cdot b + a$$

## Intuición visual

\begin{tikzpicture}[
  node distance=2cm,
  every node/.style={draw, rectangle, rounded corners},
]
\node (a1) {$a$};
\node (b) [below=of a1] {$b$};

\node (mul) [right=of a1] {$\times$};

\node (a2) [below=of mul] {$a$};

\node (add) [right=of mul] {$+$};

\node (d) [right=of add] {$d$};

\draw[->] (a1) -- (mul);
\draw[->] (b) -- (mul);
\draw[->] (mul) -- (add);
\draw[->] (a2) -- (add);
\draw[->] (add) -- (d);
\end{tikzpicture}


Cada nodo representa **una operación real ejecutada en el código**.

##
> ¿Por qué el tensor `a` aparece dos veces en este grafo?

---

# Forward y Backward
## Dos fases del mismo proceso

- **Forward pass**: calcular valores  
- **Backward pass**: propagar gradientes  
<br/><br/>
El backward pass no “invierte” el cálculo:  

> Aplica la regla de la cadena siguiendo las dependencias del grafo

##
> ¿El backward pass necesita volver a ejecutar el forward? ¿Por qué?

---

# Qué NO es magia
## Desmitificando el entrenamiento

- PyTorch no “adivina” derivadas
- No hay reglas especiales para redes neuronales
- Todo se reduce a:
  - sumas
  - multiplicaciones
  - regla de la cadena

Las redes neuronales son **grafos grandes**, no objetos especiales.

##
> ¿Qué operación básica aparece en todas las capas de una red?

---

# ¿Por qué esto importa?
## Conexión con redes neuronales

- Cada capa = operaciones en un grafo  
- Entrenar = recorrer el grafo hacia atrás  
- Optimizadores = usar los gradientes calculados  
<br/>
Sin **autograd**, no hay deep learning moderno.

##
> ¿Qué parte de este proceso cambiaría si la red tuviera más capas?

---

# Resumen

- Tensores almacenan datos **y relaciones**
- Autograd construye grafos computacionales
- `.backward()` aplica la regla de la cadena
- Esto es la base de backpropagation

##
> ¿Qué concepto de esta sesión es imprescindible para construir una red desde cero?

---

# Próxima sesión
## Construyendo una red neuronal sin magia

Cada capa será solo:
- multiplicaciones
- sumas
- activaciones

Exactamente lo que acabamos de ver.

##
> ¿Qué parte de una red neuronal crees que será más fácil de implementar ahora?
