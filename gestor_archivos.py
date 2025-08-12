# gestor_archivos.py
# Autor: Álvaro Álvarez
# Descripción: Script sencillo para crear, borrar y copiar archivos desde la terminal

import os
import shutil

def crear_archivo(nombre):
    """Crea un archivo vacío con el nombre especificado."""
    try:
        with open(nombre, 'w') as archivo:
            archivo.write("")  # Archivo vacío
        print(f"✅ Archivo '{nombre}' creado exitosamente.")
    except Exception as e:
        print(f"❌ Error al crear el archivo: {e}")

def borrar_archivo(nombre):
    """Elimina el archivo especificado si existe."""
    if os.path.exists(nombre):
        os.remove(nombre)
        print(f"🗑️ Archivo '{nombre}' eliminado.")
    else:
        print(f"⚠️ El archivo '{nombre}' no existe.")

def copiar_archivo(origen, destino):
    """Copia el archivo de origen al destino."""
    if os.path.exists(origen):
        shutil.copy(origen, destino)
        print(f"📄 Archivo copiado de '{origen}' a '{destino}'.")
    else:
        print(f"⚠️ El archivo origen '{origen}' no existe.")

def mostrar_menu():
    print("\n--- Gestor de Archivos ---")
    print("1. Crear archivo")
    print("2. Borrar archivo")
    print("3. Copiar archivo")
    print("4. Salir")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            nombre = input("Nombre del archivo a crear: ")
            crear_archivo(nombre)
        elif opcion == "2":
            nombre = input("Nombre del archivo a borrar: ")
            borrar_archivo(nombre)
        elif opcion == "3":
            origen = input("Archivo origen: ")
            destino = input("Archivo destino: ")
            copiar_archivo(origen, destino)
        elif opcion == "4":
            print("👋 Saliendo del programa.")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")