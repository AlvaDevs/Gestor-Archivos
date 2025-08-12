import unittest
import os
from gestor_archivos import crear_archivo, borrar_archivo, copiar_archivo

class TestGestorArchivos(unittest.TestCase):

    def setUp(self):
        self.archivo_prueba = "test.txt"
        self.archivo_copia = "test_copia.txt"

    def tearDown(self):
        for archivo in [self.archivo_prueba, self.archivo_copia]:
            if os.path.exists(archivo):
                os.remove(archivo)

    def test_crear_archivo(self):
        crear_archivo(self.archivo_prueba)
        self.assertTrue(os.path.exists(self.archivo_prueba))

    def test_borrar_archivo(self):
        crear_archivo(self.archivo_prueba)
        borrar_archivo(self.archivo_prueba)
        self.assertFalse(os.path.exists(self.archivo_prueba))

    def test_copiar_archivo(self):
        crear_archivo(self.archivo_prueba)
        copiar_archivo(self.archivo_prueba, self.archivo_copia)
        self.assertTrue(os.path.exists(self.archivo_copia))

if __name__ == "__main__":
    unittest.main()