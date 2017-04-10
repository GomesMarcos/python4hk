#from scapy.all import *

arquivo = open('teoria.txt', 'w')
arquivo.write("Funções de Baixo Níxel:\n    sr() = Enviar e receber pacotes na camada 3(rede);\n    sr1() = Enviar pacotes na camada de rede e receber apenas a primeira resposta;\n    srp() = Enviar e receber pacotes na camada de enlaxe;\n    srp1() = Enviar pacotes na camada de enlaxe e receber apenas a primeira resposta;\n    srloop() Enviar pacotes na camada 3 em um loop e imprimir as saídas;\n    srploop() = Enviar pacotes na camada 2 em um loop e imprimir as saídas;\n    sniff() = Captura pacotes;\n    send() = Enviar pacotes na camada 3;\n    sendp() = Enviar pacotes na camada 2;\n    ls() = Lista as camadas suportadas pelo Scapy;\n    ls(x) = Mostra as características de uma determinada camada x;\n    lsc() = Mostra todas as funções presentes no Scapy;\n    lsc(x) = Mostra os parâmetros da função x;\n    conf() = Mostra todos os parâmetros iniciais predefinidos.\n\n")
arquivo.write("Funções de Alto Nível: \n")
arquivo.close()

arquivo = open('teoria.txt', 'r')
arquivo.read()
arquivo.close()
