from componente import Component
from registros import logger
import logging


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
    
    def modificar(self, nuevo_nombre:str) -> None:
        #cambiar el nombre del documento
        self.nombre = nuevo_nombre
        return f"Documento {self.nombre} cambiado nombre a: {nuevo_nombre}"

    @logger
    def acceder(self, usuario: str) -> None:
        #print(f"Acceso a {usuario} al documemnto {self.nombre}")
        logging.info(f"Acceso a {usuario} aaaaaaaa {self.nombre}")


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
