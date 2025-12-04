---
title: "Introducción a Python – Sesión 4"
author: "Cesar Garcia"
date: ""
lang: es
theme: "Madrid"
---

# Introducción a Python – Sesión 4
::: notes
Última sesión del curso: manejo de archivos, manejo de errores y proyecto final.
:::

# Objetivos de la sesión
- Leer y escribir archivos de texto.
- Comprender excepciones y manejo de errores.
- Usar try/except/finally.
- Construir un sistema sencillo de registro de gastos.
- Preparar al estudiante para seguir avanzando después del curso.


# Repaso rápido de la sesión anterior
::: notes
Recordar funciones, diccionarios y la agenda de contactos para conectar con archivos y errores.
:::

- Funciones y valores de retorno  
- Diccionarios y listas de diccionarios  
- Mini-proyecto: Agenda de contactos  
- Preparación para trabajar con almacenamiento persistente

---

# Introducción al manejo de archivos
::: notes
Explica por qué los archivos permiten persistencia más allá de la ejecución.
:::

Python permite:
- Crear archivos
- Leerlos
- Escribir en ellos
- Actualizarlos

Se usan funciones integradas como `open()`.

---

# Escribir archivos – modo "w"
::: notes
Aclara que "w" borra el contenido previo del archivo.
:::

```python
with open("notas.txt", "w", encoding="utf-8") as f:
    f.write("Hola mundo\n")
    f.write("Segunda línea.\n")
```

- `"w"` crea o sobrescribe el archivo.

---

# Agregar contenido – modo "a"
```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("Nueva entrada al registro\n")
```

- `"a"` agrega texto al final
- No borra lo previo

---

# Leer archivos – modo "r"
::: notes
Demuestra la diferencia entre leer todo y leer línea por línea.
:::

```python
with open("notas.txt", "r", encoding="utf-8") as f:
    contenido = f.read()

print(contenido)
```

---

# Leer archivo línea por línea
```python
with open("notas.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())
```

- `strip()` elimina saltos de línea y espacios extra.

---

# ¿Qué es una excepción?
::: notes
Aclarar que no todas las excepciones son errores del programador; a veces son condiciones esperadas.
:::

- Error que ocurre durante la ejecución.
- Detiene el programa si no se maneja.

Ejemplo:

```python
x = int("hola")  # ValueError
```

---

# try / except
::: notes
Mostrar cómo proteger partes del código que pueden fallar.
:::

```python
try:
    x = int(input("Número: "))
    print(10 / x)
except ValueError:
    print("Debes introducir un número entero.")
```

---

# Múltiples excepciones
```python
try:
    x = int(input("Número: "))
    y = 10 / x
    print(y)
except ValueError:
    print("Entrada inválida.")
except ZeroDivisionError:
    print("No se puede dividir entre cero.")
```

---

# Bloque finally
::: notes
Explica que finally se ejecuta siempre sin importar si hubo error.
:::

```python
try:
    archivo = open("test.txt")
except:
    print("Error al abrir archivo.")
finally:
    print("Fin del intento.")
```

---



# Proyecto Final: Sistema de Gastos
::: notes
Explica que este proyecto integra todo: listas, diccionarios, funciones, archivos y manejo de errores.
:::

Objetivo:
- Registrar gastos (concepto + monto)
- Guardarlos en un archivo
- Cargar gastos al iniciar
- Mostrar total acumulado

---

# Estructura de datos del sistema de gastos
```python
gasto = {
    "concepto": "Comida",
    "monto": 250.0
}

gastos = []
```

Archivo `gastos.txt`:
```
Comida,250.0
Transporte,100.0
```

---

# Función: cargar gastos desde archivo
```python
def cargar_gastos(nombre_archivo):
    gastos = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(",")
                concepto = partes[0]
                monto = float(partes[1])
                gastos.append({"concepto": concepto, "monto": monto})
    except FileNotFoundError:
        print("Archivo no encontrado. Se creará uno nuevo.")
    return gastos
```

---

# Función: guardar gastos en archivo
```python
def guardar_gastos(nombre_archivo, gastos):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        for g in gastos:
            linea = f"{g['concepto']},{g['monto']}\n"
            f.write(linea)
```

---

# Función: agregar gasto
```python
def agregar_gasto(gastos):
    concepto = input("Concepto del gasto: ")
    try:
        monto = float(input("Monto: "))
    except ValueError:
        print("Monto inválido.")
        return

    gastos.append({"concepto": concepto, "monto": monto})
    print("Gasto agregado.")
```

---

# Función: mostrar gastos y total
```python
def mostrar_gastos(gastos):
    if not gastos:
        print("No hay gastos registrados.")
        return

    total = 0
    for i, g in enumerate(gastos, start=1):
        print(f"{i}. {g['concepto']} - {g['monto']:.2f}")
        total += g["monto"]

    print(f"\nTotal gastado: {total:.2f}")
```

---

# Programa principal
```python
def main():
    archivo = "gastos.txt"
    gastos = cargar_gastos(archivo)

    while True:
        print("\n--- Menú de gastos ---")
        print("1. Agregar gasto")
        print("2. Ver gastos")
        print("3. Guardar y salir")

        opcion = input("Opción: ")

        if opcion == "1":
            agregar_gasto(gastos)
        elif opcion == "2":
            mostrar_gastos(gastos)
        elif opcion == "3":
            guardar_gastos(archivo, gastos)
            print("Gastos guardados. Adiós.")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
```

---

# Posibles mejoras del proyecto
::: notes
Motiva a extender el proyecto para aprendizaje continuo.
:::

- Agregar fechas a los gastos  
- Filtrar por categorías  
- Guardar en JSON  
- Exportar a CSV  
- Crear interfaz gráfica simple (Tkinter)

---

# Próximos pasos en Python
::: notes
Guía para continuar aprendiendo después del curso.
:::

- Programación orientada a objetos  
- Módulos y paquetes  
- Librerías externas (pip)  
- Desarrollo web (Flask, Django)  
- Ciencia de datos (Pandas, NumPy)  
- Automatización de tareas

---

# Recursos recomendados
- *Automate the Boring Stuff with Python*  
- Documentación oficial de Python  
- Plataformas de práctica:
  - LeetCode  
  - HackerRank  
  - Codewars  

---

# Cierre del curso
::: notes
Felicita al estudiante y repasa los logros del curso.
:::

- Logros:
  - Fundamentos del lenguaje  
  - Estructuras de control  
  - Funciones  
  - Diccionarios  
  - Archivos  
  - Manejo de errores  
  - Proyecto final completo  

¡Felicidades por completar las 4 sesiones!
