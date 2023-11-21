import csv

def leer_pizzas_desde_csv(archivo_csv):
    menus = []
    with open(menus.csv, 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            menus.append(row)
    return menus

def reconstruir_menu(datos):
    menu = f"ID: {datos['id']}\n"
    menu += f"Nombre: {datos['nombre']}\n"
    menu += f"Entrante: {datos['entrante']}\n"
    menu += f"Pizza: {datos['pizza']}\n"
    menu += f"Bebida: {datos['bebida']}\n"
    menu += f"Postre: {datos['postre']}\n"
    return menu