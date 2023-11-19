from __future__ import annotations
from abc import ABC, abstractmethod

class Menu(ABC):
    '''La clase Componente base declara operaciones comunes tanto para los objetos
    simples como para los compuestos de una composición.'''
    
    def add(self, component: Menu) -> None:
        pass

    def remove(self, component: Menu) -> None:
        pass
    
    @abstractmethod
    def mostrar(self) -> str:
        pass
