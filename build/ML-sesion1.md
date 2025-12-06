---
title: "Introducción a Python – Sesión 1"
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
## Objetivos de la sesión
- Comprender qué es el aprendizaje automático (Machine Learning).
- Diferenciar entre aprendizaje clásico y aprendizaje profundo.
- Identificar tipos de problemas: regresión, clasificación, clustering.
- Conectar conceptos con aplicaciones del mundo real.
- Entender por qué el ML funciona y qué patrones aprende.
- Construir intuiciones visuales clave.

---

# ¿Qué es el Machine Learning?
## Definición
El Machine Learning permite a los sistemas aprender patrones a partir de datos sin ser programados explícitamente.

## Ciclo de ML
1. Recolección de datos  
2. Modelo  
3. Entrenamiento  
4. Predicción  
5. Evaluación  

---

# Por qué funciona el Machine Learning (segmento nuevo)
## Patrones visibles vs patrones ocultos
- Algunos patrones pueden verse gráficamente.
- Otros requieren cálculos complejos imposibles de ver.
- ML descubre relaciones no triviales.

## Ejemplo intuitivo
Predicción de precio de casas:
- Entradas: tamaño, ubicación, edad, habitaciones.
- ML aprende combinaciones no obvias.

---

# Categorías del Aprendizaje Supervisado
## Algoritmos Clásicos
- Regresión lineal/polinomial  
- Clasificación  
- kNN  
- Árboles de decisión  
- Random Forests  
- SVM (conceptual)

## Deep Learning (Redes Neuronales)
- Inspiradas en el cerebro
- Aprenden representaciones profundas
- Ideales para grandes volúmenes de datos

---

# Tipos de Problemas
## Regresión
Predicción de valores numéricos.

## Clasificación
Asignación de categorías.

## Clustering
Agrupación sin etiquetas.

---

# Analogías visuales del ML (segmento nuevo)
- ML como fábrica  
- ML como mapa  
- ML como filtro de ruido  

---

# Aplicaciones del Mundo Real
- Recomendadores  
- Autos autónomos  
- Diagnóstico médico  
- Modelos de lenguaje  

---

# Actividad de Cierre (extendida)
Clasificar ejemplos reales:
- ¿Regresión, clasificación o clustering?
- ¿Clásicos o redes neuronales?
- ¿Qué datos se necesitan?

---

## Diagrama: Ciclo básico de Machine Learning

```{=latex}
\begin{tikzpicture}[
  node distance=1.8cm,
  every node/.style={rectangle, draw, rounded corners, minimum width=2.4cm, minimum height=0.9cm},
  >=Stealth
]
\node (datos)    {Datos};
\node (modelo)   [right=of datos] {Modelo};
\node (entrena)  [right=of modelo] {Entrenamiento};
\node (predic)   [right=of entrena] {Predicción};
\node (evalua)   [right=of predic] {Evaluación};

\draw[->] (datos) -- (modelo);
\draw[->] (modelo) -- (entrena);
\draw[->] (entrena) -- (predic);
\draw[->] (predic) -- (evalua);

\end{tikzpicture}
```

---

## Diagrama: Red neuronal simple (intuición)

```{=latex}
\begin{tikzpicture}[
  >=Stealth,
  node distance=1.2cm and 1.6cm,
  input/.style={circle, draw, minimum size=0.6cm},
  hidden/.style={circle, draw, minimum size=0.6cm},
  output/.style={circle, draw, minimum size=0.6cm}
]

% Capa de entrada
\node[input] (x1) at (0,1.5) {$x_1$};
\node[input] (x2) at (0,0.5) {$x_2$};
\node[input] (x3) at (0,-0.5) {$x_3$};

% Capa oculta
\node[hidden] (h1) at (2,2) {};
\node[hidden] (h2) at (2,1) {};
\node[hidden] (h3) at (2,0) {};
\node[hidden] (h4) at (2,-1) {};

% Capa de salida
\node[output] (y) at (4,0.5) {$\hat y$};

% Conexiones entrada -> oculta
\foreach \i in {x1,x2,x3}{
  \foreach \h in {h1,h2,h3,h4}{
    \draw[->] (\i) -- (\h);
  }
}

% Conexiones oculta -> salida
\foreach \h in {h1,h2,h3,h4}{
  \draw[->] (\h) -- (y);
}

\end{tikzpicture}
```

---

## Diagrama: Descenso de gradiente (idea)

```{=latex}
\begin{tikzpicture}[
  >=Stealth,
  scale=0.9,
  every node/.style={font=\small}
]
% Eje horizontal
\draw[->] (-0.2,0) -- (6.2,0) node[right] {Parámetros (pesos)};
% Eje vertical
\draw[->] (0,-0.2) -- (0,4.2) node[above] {Pérdida};

% Curva suave (pérdida)
\draw[thick, domain=0.5:5.5, smooth, variable=\x] plot (\x,{0.15*(\x-3)^2 + 1});

% Puntos de iteraciones
\fill (1.2, 2.5) circle (1.5pt) node[above left] {Inicio};
\fill (2.1, 1.8) circle (1.5pt);
\fill (2.6, 1.4) circle (1.5pt);
\fill (3.0, 1.35) circle (1.5pt) node[below right] {Cerca del mínimo};

% Flechas de pasos
\draw[->] (1.2,2.5) -- (2.1,1.8);
\draw[->] (2.1,1.8) -- (2.6,1.4);
\draw[->] (2.6,1.4) -- (3.0,1.35);

\end{tikzpicture}
```

---

## Diagrama: Sobreajuste vs buena generalización

```{=latex}
\begin{tikzpicture}[
  >=Stealth,
  scale=0.9,
  every node/.style={font=\small}
]
% Ejes
\draw[->] (0,0) -- (6,0) node[right] {Épocas};
\draw[->] (0,0) -- (0,4) node[above] {Pérdida};

% Curva entrenamiento (baja continuamente)
\draw[thick] (0.5,3.5) .. controls (2,2) and (3,1.2) .. (5.5,0.7) node[right] {Entrenamiento};

% Curva validación (mínimo y luego sube)
\draw[thick,dashed] (0.5,3.2) .. controls (2,2.1) and (3,1.4) .. (4,1.1)
                     .. controls (4.6,1.25) and (5.2,1.6) .. (5.5,2.0)
                     node[right] {Validación};

% Punto de parada temprana
\fill (4,1.1) circle (1.5pt) node[below right] {Early stopping};

\end{tikzpicture}
```

---
