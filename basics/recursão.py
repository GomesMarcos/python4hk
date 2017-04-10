print("Função que chama a si mesma.")

def pot(base, expoente):
    if expoente == 0:
        return 1
    return base*pot(base, expoente-1)

print(pot(0,6))
print(pot(1,500))
print(pot(2, 10))
print(pot(4, 2))

def fibonacci(tamanho):
    vet = []
    anterior, proximo = 1,1

    for i in range(tamanho):

        vet.append(anterior)

        anterior, proximo = proximo, anterior + proximo

    return vet
print()
print(fibonacci(10))