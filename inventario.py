import os

# Función para cargar datos con índice y acceso directo
def cargar_datos_con_indice(archivo):
    inventario = {}
    indice_id = {}
    indice_categoria = {}
    if not os.path.exists(archivo):
        with open(archivo, 'w') as file:
            pass  # Crea el archivo vacío si no existe
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

# Función para guardar datos (sobrescribe el archivo)
def guardar_datos(datos, archivo):
    with open(archivo, 'w') as file:
        for id_parte, info in datos.items():
            file.write(f"{id_parte},{info['nombre']},{info['fabricante']},{info['categoria']},{info['cantidad']}\n")

# Función para agregar un nuevo componente y actualizar índices
def agregar_componente(datos, archivo, id_parte, nombre, fabricante, categoria, cantidad):
    datos[id_parte] = {
        "nombre": nombre,
        "fabricante": fabricante,
        "categoria": categoria,
        "cantidad": cantidad
    }
    guardar_datos(datos, archivo)
    # Recargar datos e índices para reflejar el cambio
    inventario_actualizado, indice_id_actualizado, indice_categoria_actualizado = cargar_datos_con_indice(archivo)
    return inventario_actualizado, indice_id_actualizado, indice_categoria_actualizado

# Función para buscar por ID con seek()
def buscar_por_id_con_seek(archivo, indice_id, id_parte):
    if id_parte in indice_id:
        with open(archivo, 'r') as file:
            file.seek(indice_id[id_parte])  # Acceso directo a la posición
            linea = file.readline().strip().split(',')
            if len(linea) == 5:
                return {
                    "nombre": linea[1],
                    "fabricante": linea[2],
                    "categoria": linea[3],
                    "cantidad": int(linea[4])
                }
    return "Componente no encontrado"

# Función para buscar por categoría usando el índice
def buscar_por_categoria(indice_categoria, inventario, categoria):
    if categoria in indice_categoria:
        resultados = {id: inventario[id] for id in indice_categoria[categoria]}
        return resultados if resultados else "No se encontraron componentes en esta categoría"
    return "Categoría no encontrada"

import os

# Función para cargar datos con índice y acceso directo
def cargar_datos_con_indice(archivo):
    inventario = {}
    indice_id = {}
    indice_categoria = {}
    if not os.path.exists(archivo):
        with open(archivo, 'w') as file:
            pass  # Crea el archivo vacío si no existe
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

# Función para guardar datos (sobrescribe el archivo)
def guardar_datos(datos, archivo):
    with open(archivo, 'w') as file:
        for id_parte, info in datos.items():
            file.write(f"{id_parte},{info['nombre']},{info['fabricante']},{info['categoria']},{info['cantidad']}\n")

# Función para agregar un nuevo componente y actualizar índices
def agregar_componente(datos, archivo, id_parte, nombre, fabricante, categoria, cantidad):
    datos[id_parte] = {
        "nombre": nombre,
        "fabricante": fabricante,
        "categoria": categoria,
        "cantidad": cantidad
    }
    guardar_datos(datos, archivo)
    # Recargar datos e índices para reflejar el cambio
    inventario_actualizado, indice_id_actualizado, indice_categoria_actualizado = cargar_datos_con_indice(archivo)
    return inventario_actualizado, indice_id_actualizado, indice_categoria_actualizado

# Función para buscar por ID con seek()
def buscar_por_id_con_seek(archivo, indice_id, id_parte):
    if id_parte in indice_id:
        with open(archivo, 'r') as file:
            file.seek(indice_id[id_parte])  # Acceso directo a la posición
            linea = file.readline().strip().split(',')
            if len(linea) == 5:
                return {
                    "nombre": linea[1],
                    "fabricante": linea[2],
                    "categoria": linea[3],
                    "cantidad": int(linea[4])
                }
    return "Componente no encontrado"

# Función para buscar por categoría usando el índice
def buscar_por_categoria(indice_categoria, inventario, categoria):
    if categoria in indice_categoria:
        resultados = {id: inventario[id] for id in indice_categoria[categoria]}
        return resultados if resultados else "No se encontraron componentes en esta categoría"
    return "Categoría no encontrada"

# Programa principal
def main():
    archivo = "inventario.txt"
    inventario, indice_id, indice_categoria = cargar_datos_con_indice(archivo)

    while True:
        print("\n1. Agregar componente")
        print("2. Buscar por ID")
        print("3. Buscar por categoría")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_parte = input("Ingrese ID de parte: ")
            nombre = input("Ingrese nombre: ")
            fabricante = input("Ingrese fabricante: ")
            categoria = input("Ingrese categoría: ")
            while True:
                entrada = input("Ingrese cantidad en stock (solo número): ")
                if entrada.isdigit():
                    cantidad = int(entrada)
                    break
                else:
                    print("Error: Ingrese solo un número válido.")
            inventario, indice_id, indice_categoria = agregar_componente(inventario, archivo, id_parte, nombre, fabricante, categoria, cantidad)
            print("Componente agregado exitosamente.")

        elif opcion == "2":
            id_parte = input("Ingrese ID de parte a buscar: ")
            resultado = buscar_por_id_con_seek(archivo, indice_id, id_parte)
            print(resultado)

        elif opcion == "3":
            categoria = input("Ingrese categoría a buscar: ")
            resultados = buscar_por_categoria(indice_categoria, inventario, categoria)
            print(resultados)

        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()