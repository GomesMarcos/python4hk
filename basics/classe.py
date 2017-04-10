print("Criando classes no Python: palavra reservada 'class'")
print("'self' é o nome do objeto a ser invocado no método. Uma referência à instância da classe")
print("Classe: Estrutura que abstrai um conjunto de objetos com características similares.\nA mesma também define comportamento de seus Objetos.")
print("Objeto é qualquer coisa que podemos dar um nome, uma instância de uma classe")
print("Artibuto =  característica do objeto.")
print("Método = Comportamento do objeto utilizando seus atributos.")
print("\n\n\n")
class Pessoa:
    def __init__(self, nome, id): #MÉTODO CONSTRUTOR
        self.nome = nome
        self.id = id

    def getNome(self):
        return self.nome
    def getId(self):
        return self.id

p1 = Pessoa('Marcos', 1)
p2 = Pessoa('João', 2)

print(p1.getNome(), p1.getId())
print(p2.getNome(), p2.getId())