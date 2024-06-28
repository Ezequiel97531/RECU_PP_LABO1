#Ezequiel Nandin    

"""
El programa contará con el siguiente menú:
1) Cargar archivo: Se pedirá el nombre del archivo y se cargarán en una lista los elementosdel
mismo.
2) Imprimir lista: Se imprimirá por pantalla la tabla (en forma de columnas) con los datos de los
servicios.
3) Asignar totales: Se deberá hacer uso de una función lambda que asignará a cada servicio el
total calculado (totalServicio) de la siguiente forma: cantidad x precioUnitario.
4) Filtrar por tipo: Se deberá generar un archivo igual al original, pero donde solo aparezcan
servicios del tipo seleccionado.
5) Mostrar servicios: Se deberá mostrar por pantalla un listado de los servicios ordenados por
descripción de manera ascendente.
6) Guardar servicios: Se deberá guardar el listado del punto anterior en un archivo de tipo json.
7) Salir.


"""


import json 

def cargar_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, "r") as archivo:
            data = json.load(archivo)
            return data
    except FileNotFoundError:
        print("Archivo no encontrado")
        return None
    
def asignar_totales(datos):
    for servicio in datos:
        servicio["totalServicio"] = (lambda cantidad, precio: cantidad * precio)(int(servicio["cantidad"]), float(servicio["precioUnitario"]))
    print("El total de los servicios a sido asignado correctamente")

def filtrar_por_tipo(datos, tipo_servicio):
    servicio_filtrado = []

    for servicio in datos:
        if servicio["tipo"] == tipo_servicio:
            servicio_filtrado.append(servicio)
    return servicio_filtrado

def mostrar_servicio(datos):
    servicios_ordenados = sorted(datos, key=lambda x: x["descripcion"])
    for servicio in servicios_ordenados:
        print(f"Id: {servicio['id_servicio']}, descripcion: {servicio['descripcion']}, tipo: {servicio['tipo']}, precio unitario: {servicio['precioUnitario']}, "
              f"cantidad: {servicio['cantidad']}, Total servicio: {servicio['totalServicio']}")

def generar_csv(ruta_archivo, datos):
    if not datos:
        return False
    
    contenido_csv = "id_servicio,descripcion,tipo,precioUnitario,cantidad,totalServicio\n"

    for servicio in datos:
        contenido_csv += f"{servicio['id_servicio']},{servicio['descripcion']},{servicio['tipo']},{servicio['precioUnitario']},{servicio['cantidad']},{servicio['totalServicio']}\n"

    guardar_archivo(ruta_archivo, contenido_csv)
    return True

def guardar_archivo(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, "w+") as archivo:
            archivo.write(contenido)
        print(f"Se creo el archivo: {archivo}")
        return True
    except Exception as e:
        print(f"Error al crear el archivo: {nombre_archivo}")
        return False
    

def menu():
    datos = []
    while True:
        print("\nMenú")
        print("1) Cargar archivo.")
        print("2) Imprimir lista.")
        print("3) Asignar totales.")
        print("4) Filtrar tipo.")
        print("5) Mostrar Servicios.")
        print("6) Guardar servicios.")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ruta_archivo = input("Ingrese una ruta de archivo json: ")
            datos = cargar_archivo(ruta_archivo)
            if datos:
                print("Archivo cargado exitosamente")
        elif opcion == "2":
            if datos:
                for servicio in datos:
                    print(f"Id: {servicio['id_servicio']}, descripcion: {servicio['descripcion']}, tipo: {servicio['tipo']}, precio unitario: {servicio['precioUnitario']}, "
                          f"cantidad: {servicio['cantidad']}, Total servicio: {servicio['totalServicio']}")
            else:
                print("No hay datos cargados.")
        elif opcion == "3":
            if datos:
                asignar_totales(datos)
            else:
                print("No hay datos cargados")
        elif opcion == "4":
            if not datos:
                print("No hay lista de datos para filtrar")
            else:
                tipo = input("Ingrese el tipo de servicio por el que quiere filtrar: ")
                servicio_filtrado = filtrar_por_tipo(datos, tipo)
                if servicio_filtrado:
                    nombre_archivo = input("Ingrese el nombre del archivo CSV a guardar: ")
                    ruta_archivo = nombre_archivo + " .csv"
                    exito = generar_csv(ruta_archivo, servicio_filtrado)
                    if exito:
                        print("El archivo se genero correctamente")
                    else:
                        print("Hubo un error en la generacion del archivo CSV")
        elif opcion == "5":
            if datos:
                mostrar_servicio(datos)
            else:
                print("No hay datos cargados.")
        elif opcion == "6":
            if datos:
                nombre_archivo = input("Ingrese el nombre del archivo json a guardar: ")
                ruta_archivo = nombre_archivo + ".json"
                guardar_archivo(ruta_archivo, json.dumps(datos))
            else:
                print("No hay datos cargados.")
        elif opcion ==  "7":
            print("Saliendo del programa...")
            break
        else:
            print("Numero equivocado.Intente de nuevo")