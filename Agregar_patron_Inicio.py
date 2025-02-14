#SCRIPT CREADO PARA AGREGAR PATRONES AL INICIO DE LOS ARCHIVOS
import os

patron_a_agregar = input("Ingrese el patron a agregar: ")

directorio = input("Dame la direccion donde agregar el patron")
elementos = os.scandir(directorio)

for elemento in elementos:
    if elemento.is_file() and not elemento.name.endswith(".py"):
        
        vieja_ruta = os.path.join(directorio, elemento.name)
        nuevo_nombre = patron_a_agregar + elemento.name
        nueva_ruta = os.path.join(directorio, nuevo_nombre)
        os.rename(vieja_ruta, nueva_ruta)
        print(f"Renombrado {elemento.name} a {nuevo_nombre}")        


