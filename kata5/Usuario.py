# Autor: Sonia Garcia
# Version: 0.0.1
# Fecha: 22/03/22

# reto 5 herencia simple

class Usuario():
    # Atributos de clase

    id: str
    nombre: str
    apellidos: str
    email: str

    # Atrubutos de instancia

    # Constructor de clase que queramos pasar si o si para la clase
    def __init__(self, newNom, newApe):
        self.id = '1234AV'
        self.nombre = newNom
        self.apellidos = newApe
        self.email = 'prueba@email.com'

        # Metodos propios - comportamiento

    def getNombre(self):
        print(f'Bienvenido {self.nombre}, {self.apellidos}')