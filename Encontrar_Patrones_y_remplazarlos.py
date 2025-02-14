#SCRIPT CREADO PARA ENCONTRAR PATRONES EN ARCHIVOS Y RENOMBRARLOS 
import os

patron_a_borrar = input("Ingrese el patron a borrar: ")
patron_a_agregar = input("Ingrese el patron a agregar: ")


directorio = input("Dame la rita deldirectorio: ")
elementos = os.scandir(directorio)


for elemento in elementos:
    if elemento.is_file():
        
        vieja_ruta = os.path.join(directorio, elemento.name)
        nuevo_nombre = elemento.name.replace(patron_a_borrar, patron_a_agregar)
        nueva_ruta = os.path.join(directorio, nuevo_nombre)
        os.rename(vieja_ruta, nueva_ruta)
        print(f"Renombrado {elemento.name} a {nuevo_nombre}")


#Creado por Brandon Sanchez | 2/Febrero/2025
