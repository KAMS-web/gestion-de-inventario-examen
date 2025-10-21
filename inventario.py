# Función para cargar datos con índice y acceso directo
def cargar_datos_con_indice(archivo):
    inventario = {}
    indice_id = {}
    indice_categoria = {}
    with open(archivo, 'r') as file:
        linea = 0
        while True:
            posicion = file.tell()  # Guarda la posición actual
            linea_texto = file.readline()
            if not linea_texto:
                break
            if linea_texto.strip():  # Ignora líneas vacías
                partes = linea_texto.strip().split(',')
                if len(partes) == 5:  # ID, nombre, fabricante, categoría, cantidad
                    id_parte, nombre, fabricante, categoria, cantidad = partes
                    inventario[id_parte] = {
                        "nombre": nombre,
                        "fabricante": fabricante,
                        "categoria": categoria,
                        "cantidad": int(cantidad)
                    }
                    indice_id[id_parte] = posicion
                    if categoria not in indice_categoria:
                        indice_categoria[categoria] = []
                    indice_categoria[categoria].append(id_parte)
                linea += 1
    return inventario, indice_id, indice_categoria

