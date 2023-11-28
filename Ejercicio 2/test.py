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
    
    def test_acceso(self):
        documento_confidencial = Documento("Confidencial.txt", "txt", 1000, sensible=True)
        proxy_documento = Proxy(documento_confidencial)

        with patch('builtins.input', return_value=self.usuario_prueba):
            proxy_documento.acceder()

        # Verificar que el acceso se ha registrado en el proxy
        self.assertIn(f"Solicitud de acceso de {self.usuario_prueba} al documento {documento_confidencial.nombre}",
                      proxy_documento.accesos_registrados)
        
    
