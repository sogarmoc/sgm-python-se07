# Autor: Sonia Garcia
# Version: 0.0.1
# Fecha: 22/03/22

# reto 6 herencia multiple

from kata6.Animal import Animal
from kata6.Mascota import Mascota

# Clase hijo

class Perro(Animal, Mascota):

    # Atributos de clase
    raza: str

    # Atributos de instancia - contructtor de clase

    def __init__(self, newRaza, newEsp, newNom):
        Animal.__init__(self, newEsp)
        Mascota.__init__(self, newNom)
        self.raza = newRaza

    # Metodos propios - comportamientos

    def saluda(self):
        print('Hola')

    # Metodo toString
    def __str__(self):
        return f'[{self.especie}, {self.peso}, {self.nombre}, {self.raza}]'