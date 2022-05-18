import math 

def print_cylinder_volume () :
    """Calcule e imprima o volume de um cilindro.
    parametros:none
    retorno: none"""
    radius = float(input("Digite o raio de um cilindro: "))
    height = float(input("Digite a altura de um cilindro: "))

    volume = math.pi * radius **2 * height

    print(f"Volume: {volume: .2f}")

print_cylinder_volume()