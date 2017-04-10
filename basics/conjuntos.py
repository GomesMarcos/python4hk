print("Conjuntos não são armazenados em uma ordem específica e não possuem elementos repetidos! \n")

s = {1, 1, 1, 1}
print("s = {1, 1, 1, 1}")
print(s)

print("\nTransformando uma lista em conjunto com o comando set(estrutura):")

lista = [1, 2, 3, 4, 4, 4]
print("lista =", lista)

print("s = set(lista)")
s = set(lista)
print("s = ", s)

s1 = {1, 2, 3}
s2 = {4, 5}

print("Para unir 2 Conjuntos utiliza-se o comando .union(conjunto_a_ser_concatenado).")

print("Exemplo: s1.union(s2)")
uniao = s1.union(s2)
print("s1 passa a ser:", s1.union(s2))
print("Isso pode ser feito com uma variável auxiliar também: ")
print("uniao = s1.union(s2)")
print("print(uniao) = ", uniao)

s1 = {1, 2, 3}
s2 = {2, 3, 4}

print("\nA intersessão entre conjuntos pode ser feita de maneira parecida, utilizando o comanto .intersection(estrutura).")

print("exemplo:\ns1 = {1, 2, 3}\ns2 = {2, 3, 4}\ns1.intersection(s2) retorna: ", s1.intersection(s2))

print("A diferença entre o 1º  2º conjunto s1.difference(s2) retorna:", s1.difference(s2))
print("Ou seja: um elemento que não está contido no segundo conjunto! =D")

print("Da mesma forma, a diferença entre o 2º  1º conjunto s2.difference(s1) retorna:", s2.difference(s1))