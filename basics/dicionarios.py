print("\nDicionários são estruturas (Hash) cujos elementos são compostos pelo par 'Chave-Valor'.")
print("Para se acessar o valor, tem de se perguntar a chave e vice-versa.")
print("Dicionários são declarados entre chaves: '{}'.")

dicionario = {'Marcos':28, 'João':30, 'Maria':20}
print(dicionario, "\n")

print("Descubrindo o valor do Hash: .__len()__ ou len(estrutura)")
len(dicionario)
print("O tamanho do Hash dicionário{} é: ", dicionario.__len__())

print("\nPar saber o valor da chave 'Marcos', usa-se estrutura['chave].\n")
print("Exemplo: dicionario['Marcos'] retorna o valor:",dicionario['Marcos'], "\n")

print("Para associar um novo valor a uma chave usa-se estrutura['chave'] = novo_valor.")
dicionario['Marcos'] = 29
print("Exmeplo: dicionario['Marcos'] = 29 retorna o valor:", dicionario['Marcos'])

print("\nMostrando todas as chaves e valores: ")
for chave in dicionario:
    print(chave, dicionario[chave])
    #print(dicionario[chave])