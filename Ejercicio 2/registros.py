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

def logger(func):
    def wrapper(*args, **kwargs):
        log_entry = {
            "timestamp": datetime.datetime.now().timestamp(),
            "usuario": kwargs["usuario"],
            "accion": func.__name__,
            "tipo": args[0].__class__.__name__,
            "info_extra": args[0].nombre
        }
        if args:
            log_entry["usuario"] = args[0]

        registrar(log_entry)
        return func(*args, **kwargs)
    return wrapper