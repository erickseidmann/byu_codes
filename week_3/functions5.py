''' De agora em diante vamos trabalhar mais com funções
isso quer dizer que sempre que for possivel vamos ultilizar
a função em nossos codigos, um exeplo de como vamos fazer isso é 
ultilizando uma função definida pelo usuario que vamos chamar de main'''
import math

def main ():
    ''' Nessa função vamos calcular o volume de um cilindro.'''
    radiu = float(input(" Digite o Raio de um cilindro: "))
    height = float(input(" Digite a altura de um cilindro: "))

    volume = math.pi * radiu ** 2 * height

    print (f"Volume: {volume: .2f} ")

main()