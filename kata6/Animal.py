# Autor: Sonia Garcia
# Version: 0.0.1
# Fecha: 22/03/22

# reto 6 herencia multiple

# Definicion superclass

class Animal():
    # Atributos de clase
    especie: str
    peso: float
    altura: float

    # Atributos de instancia

    def __init__(self, newEsp):
        self.especie = newEsp
        self.peso = 15.7
        self.altura = 0.00

    # Metodos propios - comportamientos

    def comer(self):
        pass

    def cazar(self):
        pass

    def dormir(self):
        pass

    # Metodo toString (todos las variables a str)
    def __str__(self):
        return f'[{self.especie}, {self.peso}, {self.altura}]'