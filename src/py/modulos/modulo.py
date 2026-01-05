# Estructura de código ejecutable
def ejecutar_aplicacion():
    print("\n--- La aplicación principal ha sido iniciada ---")
    print(__name__)
    # Aquí se instancia y usa el código principal.

# Este es el punto de inicio del programa
if __name__ == "__main__":
    ejecutar_aplicacion()
else:
    print("El script ha sido importado como un módulo, el código principal no se ejecuta.\n")