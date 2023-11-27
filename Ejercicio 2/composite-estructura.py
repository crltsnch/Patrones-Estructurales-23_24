from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Union, Dict
import json
import os

class Component(ABC):
    """
    The base Component class declares common operations for both simple and
    complex objects of a composition.
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def mostrar(self) -> dict:
        pass

    def get_tamaño(self) -> int:
        pass

    def acceder(self) -> None:
        pass


class Documento(Component):
    """
    The Leaf class represents the end objects of a composition. A leaf can't
    have any children.

    Usually, it's the Leaf objects that do the actual work, whereas Composite
    objects only delegate to their sub-components.
    """
    def __init__(self, nombre: str, tipo:str, tamaño:int, sensible: bool = False):
        self.nombre = nombre
        self.tipo = tipo
        self.tamaño = tamaño
        self.sensible = sensible

    def mostrar(self) -> dict:
        return {
                "nombre": self.nombre,
                "tipo": self.tipo,
                "tamano": self.tamaño
                }
    
    def get_tamaño(self) -> int:
        return self.tamaño

    def acceder(self, usuario: str) -> None:
        print(f"Acceso a {usuario} al documemnto {self.nombre}")


class Link(Component):
    def __init__(self, target: str, tamaño: int=0):
        self.target = target
        self.tamaño = tamaño

    def mostrar(self) -> dict:
        return {
            "target": self.target,
            "tamano": self.tamaño
            }
    
    def get_tamaño(self) -> int:
        return self.tamaño

    def acceder(self, usuario: str) -> None:
        self.target.acceder(usuario)


class Carpeta(Component):
    """
    The Composite class represents the complex components that may have
    children. Usually, the Composite objects delegate the actual work to their
    children and then "sum-up" the result.
    """

    def __init__(self, nombre: str):
        self.nombre = nombre
        self._children: List[Component] = []
        self._tamaño = 0

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self
        self._tamaño += component.get_tamaño()

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None
        self._tamaño -= component.get_tamaño()

    def is_composite(self) -> bool:
        return True

    def mostrar(self) -> dict:
        return {
            "type": self.__class__.__name__,
            "nombre": self.nombre,
            "children": [child.mostrar() for child in self._children],
            "tamano": self.get_tamaño()
        }

    def get_tamaño(self) -> int:
        return sum([child.get_tamaño() for child in self._children])
    
    def acceder(self, usuario: str) -> None:
        print(f"Registro de acceso por {usuario} a la carpeta {self.nombre}")


class Proxy(Component):

    def __init__(self, documento: Documento):
        self.documento = documento
        self.accesos_registrados: List[str] = []
    
    def mostrar(self) -> str:
        return f"Proxy de Acceso y Registro: {self.documento.mostrar()}"

    def acceder(self, usuario: str) -> None:
        self.documento.acceder(usuario)
        solicitud = f"Solicitud de acceso de {usuario} al documento {self.documento.nombre}"
        self.accesos_registrados.append(solicitud)

    def mostrar_registros(self) -> None:
        print("Accesos registrados: ")
        for acceso in self.accesos_registrados:
            print(acceso)



def client_code(component: Component) -> None:
    """
    The client code works with all of the components via the base interface.
    """
    print(f"RESULT:\n{component.mostrar()}", end="\n")


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


if __name__ == "__main__":

    '''Carpeta 1'''
    ruta_carpeta = Carpeta("Imagenes")
    carpeta1 = Carpeta("Carpeta1")
    carpeta2 = Carpeta("Carpeta2")
    documento1 = Documento("Confidencial.txt", "txt", 1000, sensible=True)
    documento2 = Documento("img.jpg", "image", 900)
    link1 = Link("Link to Carpeta2", tamaño=10)

    '''Carpeta 2'''
    ruta_carpeta2 = Carpeta("Videos")
    carpeta3 = Carpeta("Videos vacaciones")
    carpeta4 = Carpeta("Videos trabajo")
    documento3 = Documento("video1.mp4", "video", 1100, sensible=True)
    documento4 = Documento("video2.mp4", "video", 1200)
    link2 = Link("Link to video1.mp4", tamaño=10)


    proxy_documento1 = Proxy(documento1)
    
    #Construir la estructura del sistema
    ruta_carpeta.add(carpeta1)
    ruta_carpeta.add(link1)
    carpeta1.add(documento1)
    carpeta1.add(carpeta2)
    carpeta2.add(documento2)


    ruta_carpeta2.add(carpeta3)
    ruta_carpeta2.add(carpeta4)
    carpeta3.add(documento3)
    carpeta3.add(link2)
    carpeta4.add(documento4)


    #Mostrar la estructura del sistema
    client_code(ruta_carpeta)
    print("\n")
    #Mostrar el tamaño de la carpeta
    print(f"Tamaño de la carpeta {ruta_carpeta.nombre}: {ruta_carpeta.get_tamaño()} bytes")
    print("\n")
    client_code(ruta_carpeta2)
    print("\n")
    #Mostrar el tamaño de la carpeta
    print(f"Tamaño de la carpeta {ruta_carpeta2.nombre}: {ruta_carpeta2.get_tamaño()} bytes")

    #Intentar acceder al documento1 a través del proxy
    proxy_documento1.acceder(usuario=input("Introduzca su nombre de usuario: "))

    #Mostrar los regristos de acceso del proxy
    proxy_documento1.mostrar_registros()

    guardar_en_json(ruta_carpeta.mostrar(), "archivo.json")
    guardar_en_json(ruta_carpeta2.mostrar(), "archivo.json")

