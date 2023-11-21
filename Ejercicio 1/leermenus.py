import csv

def leer_pizzas_desde_csv(archivo_csv):
    menus = []
    with open(menus.csv, 'r', newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            menus.append(row)
    return menus
