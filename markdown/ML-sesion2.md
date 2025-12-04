
% Sesión 2: Fundamentos de Redes Neuronales
% Curso: Fundamentos de Machine Learning con Redes Neuronales
% Sesión 2 (1 hora)

# Introducción
## Objetivos de la sesión
- Comprender qué es una neurona artificial.
- Entender el flujo de información en una red (forward propagation).
- Conocer los componentes principales: pesos, bias, capas.
- Explorar funciones de activación fundamentales.

---

# ¿Qué es una Neurona Artificial?
## Concepto
Una neurona artificial toma varias entradas, las multiplica por pesos, suma un sesgo (bias) y aplica una función de activación.

## Intuición
- Los **pesos** representan la importancia de cada entrada.
- El **bias** ajusta la salida desplazando la función.
- La **activación** introduce no linealidad.

---

# Estructura de una Red Neuronal
## Capas
- **Capa de entrada:** recibe los datos.
- **Capas ocultas:** procesan y transforman la información.
- **Capa de salida:** produce la predicción.

## Densas o Fully Connected
Cada neurona está conectada con todas las neuronas de la siguiente capa.

---

# Forward Propagation
## Flujo de Información
1. Los datos ingresan a la capa de entrada.
2. Cada capa calcula: suma ponderada + activación.
3. La última capa entrega la predicción.

## Observaciones
- No hay aprendizaje todavía, solo cálculo.
- La complejidad depende del número de capas y neuronas.

---

# Funciones de Activación
## ¿Por qué son necesarias?
Sin funciones de activación, toda la red sería equivalente a una regresión lineal.

## Tipos Comunes
### ReLU
Salida: max(0, x). Rápida y efectiva.

### Sigmoid
Mapea valores entre 0 y 1. Útil para probabilidades.

### Tanh
Valores entre -1 y 1.

### GELU
Activación suave usada en Transformers.

---

# Arquitectura y Capacidad del Modelo
## Profundidad y Anchura
- Más capas -> capacidad de aprender patrones complejos.
- Demasiadas capas -> riesgo de sobreajuste.

## Elección del modelo
Depende del tipo de datos y tarea.

---

# Actividad de Cierre
Dibujar una red neuronal simple:
- Entradas
- Pesos
- Activaciones
- Salida

---

# Notas del Presentador
- Usar diagramas para reforzar la estructura de capas.
- Explicar la intuición detrás de cada activación.
- Conectar el flujo de la red con analogías: fábrica, tuberías, filtros.
