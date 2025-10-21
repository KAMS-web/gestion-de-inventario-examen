import json

#funcion para cargar los datos desde un archivo
def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as f:
            datos = json.load(f)
        return datos
    except FileNotFoundError:
        return []
    
    