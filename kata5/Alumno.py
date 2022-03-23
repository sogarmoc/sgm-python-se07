# Autor: Sonia Garcia
# Version: 0.0.1
# Fecha: 22/03/22

# reto 5 herencia simple

from kata5.Usuario import Usuario

class Alumno(Usuario):
    # Atributos de clase
    asignatura: str

    # Atributos de instancia

    def __init__(self,  newNom, newApe, newAsig):
        super().__init__(newNom, newApe)
        self.asignatura = newAsig


        # Metodos propios - comportamientos
        # Si tenemos un mismo metodo que se llame igual va a utilizar el de la propia clase antes que el de la clase padre


    def getNombre(self):
        print(f'Bienvenido {self.nombre} {self.apellido} - {self.asignatura}')