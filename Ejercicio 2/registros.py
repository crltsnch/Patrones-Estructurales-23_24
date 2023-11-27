import csv
import datetime

csv_archivo = "registros.csv"
csv_columnas = ["timestamp", "usuario", "accion", "tipo", "info_extra"]
csv_existe = False

def registrar(log_entry: dict) -> None:
    global csv_existe
    with open(csv_archivo, "a") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_columnas)
        if not csv_existe:
            writer.writeheader()
            csv_existe = True
        writer.writerow(log_entry)
