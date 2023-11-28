import csv
import datetime
import os

carpeta_ejercicio2 = "Ejercicio 2"
csv_archivo = os.path.join(carpeta_ejercicio2, "registros.csv")
csv_columnas = ["timestamp", "usuario", "accion", "tipo", "info_extra"]
csv_existe = False

def verificar_columnas_existentes() -> None:
    global csv_existe
    if not csv_existe:
        if not os.path.exists(csv_archivo) or os.path.getsize(csv_archivo) == 0:
            with open(csv_archivo, "a", newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=csv_columnas, delimiter=';')
                writer.writeheader()
        csv_existe = True

def registrar(log_entry: dict) -> None:
    verificar_columnas_existentes()
    with open(csv_archivo, "a") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_columnas, delimiter=';')
        if log_entry: #Si el log_entry no está vacío
            writer.writerow(log_entry)

def crear_log_entry(func, *args, **kwargs) -> dict:
    usuario = kwargs.get("usuario", "")
    if usuario:
        log_entry = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "usuario": usuario,
            "accion": f"{func.__name__} - {args[0].nombre if args else ''}",
            "tipo": "Función",
            "info_extra": f"Información específica de la función - {args[0].nombre if args else ''}"
        }
        return log_entry
    return {}

def logger(func):
    def log_and_call(*args, **kwargs):
        log_entry = crear_log_entry(func, *args, **kwargs)
        registrar(log_entry)
        return func(*args, **kwargs)

    return log_and_call
