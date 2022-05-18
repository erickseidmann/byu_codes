'''Agora para tornar uma função mais reutilizavel ainda nos vamos 
usar o RETURN que retornará o valor mas não vai imprimir o valor por isso desta vez alteramos 
o nome da função para compute ao inves de print, já que a função não vai mais imprimir o resultado
como nos exemplos anteriores'''
import math

def compute_cylinder_volume(radius, height):
    """Calcula e retorna o valor de um cilindro.
        Parametros: radius- radio de um cilindro
                    height- altura de um cilindro
        retorna: o valor do volume do cilindro"""
    volume = math.pi * radius ** 2 * height

    return volume
# quando tiver duvida de como imprimir uma função olha aqui!!
volume = compute_cylinder_volume(2.5,4.1)

print(volume)