'''Desta vez vamos fazer uma função 
ultilizando parametros o que torna nossa 
função mais reutilizavel!'''

import math 

def print_cylinder_volume (radius, height):
    """ Calcule e imprima o volume de um cilindro.
    parametros: radius:raio de um cilindro
                height: a altura do cilindro
    rtetorno: nada"""
    volume = math.pi * radius ** 2 * height

    print(volume)
print_cylinder_volume(2.9,4.1)
