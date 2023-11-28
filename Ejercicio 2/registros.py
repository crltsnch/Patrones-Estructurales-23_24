import csv
import datetime

csv_archivo = "registros.csv"
csv_columnas = ["timestamp", "usuario", "accion", "tipo", "info_extra"]
csv_existe = False

def verificar_columnas_existentes() -> None:
    global csv_existe
    if csv_existe:
        with open(csv_archivo, "a", newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_columnas)
            writer.writeheader()
        csv_existe = True

def registrar(log_entry: dict) -> None:
    verificar_columnas_existentes()
    with open(csv_archivo, "a") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_columnas)
        writer.writerow(log_entry)

def crear_log_entry(func, *args, **kwargs) -> dict:
    log_entry = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "usuario": kwargs.get("usuario", ""),
        "accion": f"{func.__name__} - {args[0].nombre if args else ''}",
        "tipo": "Función",
        "info_extra": f"Información específica de la función - {args[0].nombre if args else ''}"
    }
    return log_entry

def logger(func):
    def log_and_call(*args, **kwargs):
        log_entry = crear_log_entry(func, *args, **kwargs)
        registrar(log_entry)
        return func(*args, **kwargs)

    return log_and_call
