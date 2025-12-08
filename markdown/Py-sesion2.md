---
title: "Introducción a Python – Sesión 2"
author: "Cesar Garcia"
date: ""
lang: es
theme: "Madrid"
---

# Introducción a Python – Sesión 2
::: notes
Repaso general antes de avanzar a condicionales, listas y bucles.
:::

# Objetivos de la sesión
- Utilizar condicionales (`if`, `elif`, `else`).
- Trabajar con listas e indexación.
- Recorrer colecciones con bucles `for`.
- Usar bucles `while` de forma segura.
- Crear un verificador de contraseñas como mini-proyecto.


# Repaso rápido de la sesión anterior
::: notes
Refuerza los conceptos fundamentales vistos previamente.
:::

- Variables y tipos básicos.
- Uso de `input()` y `print()`.
- Operadores aritméticos y lógicos.
- Concepto de Verdad/Falsedad en Python.

---

# Condicionales: if / elif / else
::: notes
Explicar la importancia de la indentación en Python.
:::

```python
edad = int(input("Edad: "))

if edad >= 18:
    print("Eres adulto.")
elif edad >= 13:
    print("Eres adolescente.")
else:
    print("Eres niño.")
```

- Evalúa condiciones en orden.
- Solo un bloque se ejecuta.

---

# Comparaciones útiles en condicionales
::: notes
Usar ejemplos cotidianos para claridad.
:::

```python
nota = float(input("Calificación: "))

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")
```

---

# Operadores lógicos dentro de condiciones
::: notes
Explica cómo combinar múltiples condiciones.
:::

```python
edad = 20
licencia = True

if edad >= 18 and licencia:
    print("Puedes conducir.")
else:
    print("No puedes conducir.")
```

---

# Listas en Python
::: notes
Introduce listas como estructuras dinámicas.
:::

```python
numeros = [10, 20, 30, 40]
nombres = ["Ana", "Luis", "Cesar"]
mezcla = [1, "hola", True, 3.14]
```

Características:
- Ordenadas
- Mutables
- Pueden contener distintos tipos

---

# Indexación de listas
::: notes
Explica índices negativos.
:::

```python
nombres = ["Ana", "Luis", "Cesar"]

print(nombres[0])  # Ana
print(nombres[1])  # Luis
print(nombres[-1]) # Cesar
```

---

# Slicing (rebanado)
```python
nums = [0, 1, 2, 3, 4, 5]

print(nums[1:4])  # [1, 2, 3]
print(nums[:3])   # [0, 1, 2]
print(nums[3:])   # [3, 4, 5]
```

- `lista[inicio:fin]` incluye inicio, excluye fin.

---

# Operaciones comunes con listas
::: notes
Demuestra cada método en el REPL.
:::

```python
numeros = [1, 2, 3]

numeros.append(4)     # [1, 2, 3, 4]
numeros.remove(2)     # [1, 3, 4]
ultimo = numeros.pop() # [1, 3]
largo = len(numeros)  # 2
```



# Bucle for (recorriendo listas)
::: notes
Explica cómo cada elemento se asigna a la variable temporal.
:::

```python
nombres = ["Ana", "Luis", "Cesar"]

for nombre in nombres:
    print(f"Hola, {nombre}")
```

---

# Bucle for con range()
::: notes
Explica que range puede generar secuencias sin crear listas completas.
:::

```python
for i in range(5):
    print(i)
```

Resultado: 0, 1, 2, 3, 4

---

# range() con inicio y fin
```python
for i in range(1, 6):
    print(i)
```

Esto imprime del 1 al 5.

Paso personalizado:

```python
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

---

# Bucle while
::: notes
Menciona el riesgo común de olvidar actualizar la variable.
:::

```python
x = 1
while x <= 5:
    print(x)
    x += 1
```

---

# Bucles infinitos (y cómo evitarlos)
::: notes
Demuestra un ejemplo simple y cómo detenerlo con Ctrl+C.
:::

```python
x = 1
while x <= 5:
    print(x)
    # Falta x += 1 → bucle infinito
```

---

# break y continue
::: notes
Explica cuándo conviene usar estas instrucciones.
:::

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

# Mini-proyecto: Verificador de contraseñas
::: notes
Describe cómo evaluar la seguridad de una contraseña.
:::

Requisitos:
- Mínimo 8 caracteres  
- Al menos una mayúscula  
- Una minúscula  
- Un número  
- Un carácter especial (!@#$%&*)

---

# Código del verificador de contraseñas

```python
contraseña = input("Introduce una contraseña: ")

tiene_mayus = False
tiene_minus = False
tiene_num = False
tiene_esp = False

especiales = "!@#$%&*"

for c in contraseña:
    if c.isupper():
        tiene_mayus = True
    elif c.islower():
        tiene_minus = True
    elif c.isdigit():
        tiene_num = True
    elif c in especiales:
        tiene_esp = True

if len(contraseña) >= 8 and tiene_mayus and tiene_minus and tiene_num and tiene_esp:
    print("Contraseña fuerte.")
else:
    print("Contraseña débil.")
```

---

# Errores comunes
::: notes
Enfatiza la importancia de la indentación.
:::

- Confundir `=` con `==`
- Olvidar `:` en if, for y while
- Mala indentación
- Condiciones imposibles o siempre verdaderas

---

# Tarea para la próxima sesión
::: notes
La tarea prepara la transición hacia funciones.
:::

1. Programa de lista de tareas: pedir 3 tareas y mostrarlas numeradas.  
2. Imprimir los números pares del 1 al 100 (for o while).

---

# Cierre de la sesión
::: notes
Refuerza los puntos clave para consolidar aprendizaje.
:::

- Condicionales  
- Listas  
- Bucles for y while  
- Mini-proyecto práctico  
