---
title: "Introducción a Python – Sesión 1"
author: "Cesar Garcia"
date: ""
lang: es
theme: "Madrid"
---

# Introducción a Python – Sesión 1
::: notes
Bienvenido a la primera sesión del curso de Introducción a Python.
Presenta los objetivos, estructura y dinámica del curso.
:::

# Objetivos de la sesión
- Comprender qué es Python y por qué es tan popular.
- Ejecutar código en el intérprete y desde archivos.
- Usar variables y tipos de datos básicos.
- Leer datos del usuario con `input()`.
- Mostrar información con `print()`.
- Realizar operaciones aritméticas y lógicas.
- Crear una calculadora de propinas como mini‑proyecto.


# ¿Qué es Python?
::: notes
Explica brevemente la historia y características destacadas de Python.
Destaca su sintaxis sencilla y su amplia comunidad.
:::

- Lenguaje de programación interpretado.
- Fácil de aprender y leer.
- Multiplataforma.
- Usado en:
  - Inteligencia Artificial
  - Ciencia de Datos
  - Desarrollo Web
  - Automatización
  - Ciberseguridad
  - Scripts del sistema

---

# ¿Cómo ejecutar Python?

## Intérprete interactivo (REPL)
```bash
python3
```

## Ejecutar un archivo
```bash
python3 archivo.py
```

---

# Editores recomendados
::: notes
Recomienda VS Code para principiantes.
:::

- VS Code
- Jupyter Notebook
- Google Colab

---

# Variables en Python
::: notes
Explica que Python es dinámicamente tipado.
:::

```python
nombre = "Cesar"
edad = 59
precio = 19.99
activo = True
```

- No se declara el tipo explícitamente.
- Las variables se crean al asignarles un valor.

---

# Tipos de datos básicos
::: notes
Proporciona ejemplos prácticos durante la presentación.
:::

- `int` — enteros
- `float` — decimales
- `str` — texto
- `bool` — verdadero/falso
- `None` — valor vacío

---

# La función type()
```python
x = 10
y = 3.5
z = "hola"

print(type(x))  # int
print(type(y))  # float
print(type(z))  # str
```

---



# Entrada de datos con input()
::: notes
Asegúrate de mostrar cómo input siempre devuelve una cadena.
:::

```python
nombre = input("¿Cómo te llamas? ")
print("Hola", nombre)
```

- `input()` siempre devuelve texto (`str`).
- Para usar números, debes convertir con `int()` o `float()`.

---

# Conversión de tipos
```python
edad_texto = input("Edad: ")
edad = int(edad_texto)
print(f"El año que viene tendrás {edad + 1} años.")
```

Funciones útiles:  
- `int("10")`  
- `float("3.14")`  
- `str(10)`  

---

# Salida formateada con f-strings
::: notes
F-strings son esenciales para claridad en Python moderno.
:::

```python
nombre = "Cesar"
edad = 59
print(f"Hola, me llamo {nombre} y tengo {edad} años.")
```

---

# Operadores aritméticos
::: notes
Muestra algunos ejemplos en vivo en el intérprete.
:::

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

---

# Operadores de comparación
::: notes
Resalta que estos devuelven `True` o `False`.
:::

- `==` igual  
- `!=` diferente  
- `<` menor  
- `>` mayor  
- `<=` menor o igual  
- `>=` mayor o igual  

---

# Operadores lógicos
::: notes
Indispensables para condicionales más adelante.
:::

```python
edad = 20
tiene_licencia = True

puede = edad >= 18 and tiene_licencia
print(puede)  # True
```

---

# Mini‑proyecto: Calculadora de propinas
::: notes
Explica paso a paso el cálculo de propina, total y división.
:::

Objetivo:
- Leer el monto de la cuenta
- Leer porcentaje de propina
- Calcular total
- Opción: dividir entre varias personas

---

# Código calculadora de propinas

```python
monto = float(input("Monto de la cuenta: "))
porcentaje = float(input("Porcentaje de propina: "))
personas = int(input("Número de personas: "))

propina = monto * (porcentaje / 100)
total = monto + propina
por_persona = total / personas

print(f"Propina: {propina:.2f}")
print(f"Total a pagar: {total:.2f}")
print(f"Cada persona paga: {por_persona:.2f}")
```

---

# Errores comunes de principiantes
::: notes
Habla de estos errores mostrando ejemplos reales.
:::

- Olvidar convertir valores ingresados con `input()`
- Comillas mal cerradas en strings
- Confundir `=` (asignación) con `==` (comparación)
- Fallas en indentación

---

# Tarea para la próxima sesión
::: notes
Esta tarea prepara al alumno para condicionales en la siguiente sesión.
:::

1. Pedir nombre, edad, estatura y comida favorita.  
   Mostrar un mensaje formateado con f-strings.  
2. Convertir Fahrenheit a Celsius:
\[
C = (F - 32) 	imes rac{5}{9}
\]

---

# Cierre de la sesión
::: notes
Repetir 3–5 puntos clave para reforzar memoria.
:::

- Qué es Python
- Cómo ejecutar programas
- Variables y tipos
- Entrada y salida
- Operadores
