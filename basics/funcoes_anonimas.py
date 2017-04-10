lista = list(range(1, 101))
print(lista)

def dobro(x):
    return x*2

lista_dobro = map(dobro, lista)

print(lista_dobro)

lista_dobro = map(lambda x: x * 2, lista)
print(list(lista_dobro))
