'''testando listas e arrays e suas principais diferenças '''
names = ['susan', 'Christopher', 'Bill', 'Justin']
presenters = names[1:3]

print(names)
print(presenters)

person = {'first': 'Christopher'}
person ['last'] = 'Harrison'
print(person)
print(person['first'])


lista = list()
for i in range(1, 7):
    par_ordenado = list()
    for j in range(1, 3):
        if j == 1:
            par_ordenado.append(int(input(f'Digite o valor do {i}º "X": ')))
        else:
            par_ordenado.append(par_ordenado[0] ** 2)
    lista.append(par_ordenado)
print(f'A lista montada é:\n{lista}')

# Segundo bloco for:
print('As componentes "x" do pares ordenados são:')
for lis in lista:
    for c in lis:
        if c == lis[0]:
            print(c, end=' ')
print()