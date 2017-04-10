#Estrutura de Dado: Lista

lista =[]
#mostrar_lista:
print(lista.__len__()) #len mostra o tamanho da lista
print(lista, "\n") #Imprimindo os elementos da lista


lista.append(10) #.append(elemento) adiciona o elemento à estrutura

print(lista.__len__())
print(lista, "\n")

#A lista é heterogênea:
#Pode-se armazenar elementos de diferentes tipos de dados numa mesma lista.

lista.append(3.14)

print(lista.__len__())
print(lista, "\n")

lista.append('marcos')

print(lista.__len__())
print(lista, "\n")

lista.append(True)

print(lista.__len__())
print(lista, "\n")

lista2 = [1,2,3]

print(lista2.__len__())
print(lista2, "\n")


lista.extend(lista2)

print("O comando '.extends(parâmetro)' concatena a extrutura com o parâmetro passado:")
print(lista.__len__())
print(lista, "\n")

lista.pop(6)
lista.pop(5)
lista.pop(4)

print("O comando .pop(elemento), remove o elemento no índice da lista passado como parâmetro.")
print(lista.__len__())
print(lista, "\n")

lista.extend(lista2)

print("O último elemento da lista é: lista[-1] =", lista[-1], "\n")


print("Retornando elementos da lista individualmente: \n")
for i in lista:
    print(i)

print("Para remover um elemento específico da lista, use o comando .remove(elemento): \n")

print(lista)

print("lista.remove(2)")
lista.remove(2)

print(lista, "\n")


print("Retornando o índice de um elemento passando-o como parâmetro: ")
print("print(lista.index('marcos')) retorna o valor:")
print(lista.index('marcos'))

print("Contando quantas vezes um elemento aparece em uma lista: .count(elemento)")
lista = ['python', 1, 1, 1, 'python']

print("lista = ['python', 1, 1, 1, 'python']\n")
print("lista.count(1) \nlista.count('python')")
lista.count(1)
lista.count('python')
print(lista.count(1))
print(lista.count('python'))

print("Ordenando crescentemente uma lista com .sort()")

lista = [4, 1, 23, 76, 9, 90, 45]
print("lista =", lista)
print("lista.sort()")
lista.sort()
print("lista = ", lista)

print("\n\nlimpando elementos da lista: .clear()")
print("lista =", lista)
print("lista.clear()")
lista.clear()
print("lista =", lista)

print("\n\ntrocando um elemento da lista de acordo com o índice:")
lista = [10, 20, 30]
print("lista = ", lista)
print("Vamos trocar '10' por '5' usando: lista[índice] = 5")
lista[0] = 5
print("A nova lista ficou: ", lista)