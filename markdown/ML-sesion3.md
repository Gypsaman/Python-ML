
% Sesión 3: Entrenamiento, Funciones de Pérdida y Descenso de Gradiente
% Curso: Fundamentos de Machine Learning con Redes Neuronales
% Sesión 3 (1 hora)

# Introducción
## Objetivos de la sesión
- Comprender qué significa entrenar una red neuronal.
- Entender el rol de las funciones de pérdida.
- Explicar el concepto de descenso de gradiente de forma intuitiva.
- Introducir épocas, iteraciones y procesamiento por lotes (batches).

---

# ¿Qué significa entrenar una red?
## Intuición general
Entrenar una red neuronal significa **ajustar los pesos** para mejorar las predicciones.

## Proceso
1. La red hace una predicción con pesos iniciales aleatorios.
2. Se compara la predicción con el valor real.
3. Se calcula un error (pérdida).
4. Se ajustan los pesos para reducir ese error.

---

# Funciones de Pérdida
## ¿Qué es una función de pérdida?
Es una medida del error entre la predicción y el valor real.  
El objetivo del entrenamiento es **minimizar esta pérdida**.

## Ejemplos
### MSE – Mean Squared Error
- Usado para regresión.
- Penaliza fuertemente errores grandes.

### Cross-Entropy
- Usado para clasificación.
- Mide qué tan bien se ajustan las probabilidades predichas a las verdaderas.

---

# Descenso de Gradiente (Gradient Descent)
## Intuición
- Imagina una montaña donde el objetivo es llegar al punto más bajo.
- El gradiente indica en qué dirección sube más rápido la montaña.
- Para minimizar el error, tomamos pasos hacia la dirección opuesta.

## Idea central
Actualizar los pesos con pequeños pasos que reduzcan la pérdida.

---

# Variantes del Descenso de Gradiente
## Batch Gradient Descent
Usa **todos los datos** en cada actualización.

## Stochastic Gradient Descent (SGD)
Usa **un solo dato** por actualización.

## Mini-Batch Gradient Descent
Usa pequeños grupos de datos:  
- Más estable que SGD  
- Más rápido que batch completo  
- El método más utilizado

---

# Learning Rate
## Concepto
El learning rate define el tamaño del paso durante el descenso de gradiente.

## Comportamiento
- Muy grande → el modelo salta el mínimo.
- Muy pequeño → entrenamiento lento.

---

# Épocas, Iteraciones y Batches
## Definiciones
### Época
Una pasada completa por todos los datos.

### Batch
Un subconjunto de los datos.

### Iteración
Una actualización de pesos por cada batch.

## Importancia
- Controlan la estabilidad y velocidad del aprendizaje.
- Permiten generalizar mejor sin sobreajustar.

---

# Procesamiento por Lotes (Batch Processing)
## Beneficios
- Estabiliza el cálculo del gradiente.
- Reduce ruido en la actualización.
- Optimiza el uso del hardware (GPU/CPU).

---

# Actividad de Cierre
Comparar tres escenarios:
1. Batch completo  
2. Mini-batch  
3. SGD  

Explicar cuál sería más estable, más ruidoso y más rápido.

---

# Notas del Presentador
- Usar la analogía de la montaña para descenso de gradiente.
- Explicar por qué el batch afecta la estabilidad.
- Evitar matemáticas y enfocarse en intuición visual.
- Conectar esta sesión con la siguiente sobre generalización.
