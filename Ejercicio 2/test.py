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
            proxy_documento.acceder(usuario=self.usuario_prueba)

        # Verificar que el acceso se ha registrado en el proxy
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            proxy_documento.mostrar_registros()
            output = mock_stdout.getvalue()

        self.assertIn(f"Solicitud de acceso de {self.usuario_prueba} al documento {documento_confidencial.nombre}", output)
            
    def test_acceso_a_carpeta(self):
        carpeta_personal = Carpeta("Personal")
        self.ruta_carpeta.add(carpeta_personal)

        with patch('builtins.input', return_value=self.usuario_prueba):
            self.ruta_carpeta.acceder(usuario=self.usuario_prueba)

        # Verificar que el acceso se ha registrado en la carpeta
        self.assertIn(f"Registro de acceso por {self.usuario_prueba} a la carpeta {carpeta_personal.nombre}",
                      carpeta_personal.accesos_registrados)

if __name__ == '__main__':
    unittest.main()