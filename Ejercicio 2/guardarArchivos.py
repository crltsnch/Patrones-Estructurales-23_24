import os
import json
from typing import Dict, Union

def guardar_en_json(data: Union[str, int, float, bool, None, Dict], filename: str) -> None:
    if os.path.exists(filename):
        # Si el archivo JSON ya existe, cargamos los datos existentes
        with open(filename, 'r') as json_file:
            existing_data = json.load(json_file)
    else:
        # Si el archivo no existe, creamos un diccionario vacío
        existing_data = {}

    # Asignamos el nuevo dato con una clave única (puedes adaptar esto según tus necesidades)
    key = f"{data['type']}_{data['nombre']}"
    existing_data[key] = data

    # Guardamos el diccionario actualizado en el archivo JSON
    with open(filename, 'w') as json_file:
        json.dump(existing_data, json_file, indent=2)