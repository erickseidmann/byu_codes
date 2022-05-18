'''Agora nos somos apresentados a dois pontos que exigem duas 
soluçoes diferentes logo teremos que ultilizar duas funçoes diferentes
'''
import math

#definir uma função principal
def main ():
    radius = float (input("Digite o raio de um cilindro: "))
    height = float (input ("Digite a altura de um cilidro: "))

    volume = compute_cylinder_volume(radius, height)

    print(f"O Volume é: {volume: .2f}")

def compute_cylinder_volume(radius, height):
    """Calcular e imprimir o volume de um cilindro"""
    volume = math.pi * radius **2 *height
    
    return volume

main()