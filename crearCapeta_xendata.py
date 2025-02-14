import os
import re
from datetime import datetime

directorio = r"Y:\MEDIA MANAGERS\MATERIAL"
with os.scandir(directorio) as archivos:
    patron = r"^PANTALLAZO-(\d{6})-B\d-\d+(?:\.[a-zA-Z0-9]+)?(?:.*)$"
    patron2 = r".*?(\d{6}).*"


    for archivo in archivos:
        if archivo.is_file():
            coincidencia = re.match(patron2, archivo.name)
            if coincidencia:
                fecha_str = coincidencia.group(1)
                fecha = datetime.strptime(fecha_str, "%d%m%y")
                
                # Formatear la fecha para usarla como nombre de carpeta (por ejemplo: "26.01.2025")
                nombre_carpeta = fecha.strftime("%d.%m.%Y")
                ruta_carpeta = os.path.join(directorio, nombre_carpeta)
                
                if not os.path.exists(ruta_carpeta):
                    os.makedirs(ruta_carpeta)
                    print(f'Carpeta creada: {ruta_carpeta}')
                
                origen = archivo.path
                destino = os.path.join(ruta_carpeta, archivo.name)
                if os.path.exists(destino):
                    print(f'El archivo {archivo.name} ya existe en {ruta_carpeta}, se omite el movimiento.')
                else:
                    os.rename(origen, destino)
                    print(f'Archivo {archivo.name} movido a {ruta_carpeta}')
            else:
                print(f"No se encontró la fecha en la cadena para el archivo {archivo.name}.")
