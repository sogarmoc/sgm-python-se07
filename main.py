
# Autor: Sonia Garcia
# version: 0.0.1
# data: 22/03/2022


# from kata5.Usuario import Usuario
# from kata5.Alumno import Alumno

from kata6.Animal import Animal

if __name__ == '__main__':
    # usu1 = Usuario('Juan','Garcia')
    # print(usu1)
    # usu1.getNombre()
    #
    # print(f'{usu1.id}, {usu1.nombre}')
    #
    # # Instancia de la clase hija
    #
    # al1 = Alumno('Sonia', 'Garcia', 'prueba')
    # al1.getNombre()
    # print(f'{al1.id}, {al1.nombre}, {al1.email}')

    an1 = Animal('Perro')
    an2 = Animal('Gato')
    print(an1)
    # print(f'{an1.especie}, {an1.peso}, {an1.altura}')
    # dir -> para ver que metodos se pueden utilizar o tiene esa clase, atributos...
    print(dir(an1))