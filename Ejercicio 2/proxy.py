from typing import List
from compositeEstructura import Component, Documento

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