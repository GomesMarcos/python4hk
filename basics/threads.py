import _thread, time

arquivo = open('threads.txt', 'r')
arquivo.read()
arquivo.close()

def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print("")
print(fib(7))

def test_fib(n):
    print('Fib %d = %d'%(n, fib(n)))

def run_fib():#Essa função NÃO POSSUI THREAD
    print("Executando sem threads o que demnanda mais recurso gera um 'gargalo' na execução:\n")
    test_fib(35) #Esse aqui "pesa" muito, demanda muito processamento.
    test_fib(10)
    test_fib(30)
    test_fib(8)
    print()
    print()


def run_fib_with_threads():
    print("Executando com threads o que demnanda menos recurso é finalizado primeiro:\n")
    _thread.start_new_thread(test_fib, (35,))
    _thread.start_new_thread(test_fib, (10,))
    _thread.start_new_thread(test_fib, (8,))
    _thread.start_new_thread(test_fib, (30,))
    time.sleep(5)#função para encerrar a execução após n segundos.

run_fib()
run_fib_with_threads()
