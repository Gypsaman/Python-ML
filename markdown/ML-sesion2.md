% Sesión 2: Fundamentos de Redes Neuronales (Expandida)
% Curso: Fundamentos de Machine Learning con Redes Neuronales
% Sesión 2 (1 hora)

# Introducción
## Objetivos
- Comprender neuronas artificiales.
- Entender flujo de información (forward propagation).
- Conocer pesos, bias, activaciones.
- Visualizar qué aprende una red neuronal.
- Construir una red conceptual desde cero.

---

# ¿Qué es una Neurona Artificial?
## Concepto
Toma entradas → pondera → suma bias → aplica activación.

## Intuición
- Pesos = importancia  
- Bias = ajuste  
- Activación = no linealidad  

---

# Estructura de una Red Neuronal
## Capas
- Entrada  
- Ocultas  
- Salida  

## Conexiones densas

---

# Forward Propagation
1. Datos entran  
2. Capa oculta calcula (pesos + activación)  
3. Capa final produce predicción  

---

# ¿Qué aprende realmente una red? (segmento nuevo)
## Representaciones internas
- Capa 1: patrones simples  
- Capa 2: combinaciones más complejas  
- Última capa: decisiones  

## Ejemplos
- Imágenes: bordes → texturas → objetos  
- Datos tabulares: combinaciones de variables  

---

# Funciones de Activación
- ReLU  
- Sigmoid  
- Tanh  
- GELU  

---

# Construcción conceptual de una red (segmento nuevo)
Ejemplo:
- Entradas: edad, peso, altura  
- Capa oculta: 4 neuronas  
- Activaciones: ReLU  
- Salida: probabilidad  

### Variaciones:
- Más profundidad = más capacidad  
- Más neuronas = más detalle  
- Activaciones diferentes = comportamientos distintos  

---

# Capacidad del Modelo
- Profundidad  
- Anchura  
- Riesgo de sobreajuste  

---

# Actividad de Cierre (extendida)
Diseñar una red:
1. Elegir entradas  
2. Decidir número de capas  
3. Elegir activaciones  
4. Justificar el diseño  

