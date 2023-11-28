import unittest
import os
import json
from io import StringIO
from unittest.mock import patch
from compositeEstructura import *
from proxy import *
from registros import *
from guardarArchivos import *

class TestEstructuraComposite(unittest.TestCase):
    def setUp(self):
        self.ruta_carpeta = Carpeta("Documentos")
        self.usuario_prueba = "usuario_prueba"
    
    
