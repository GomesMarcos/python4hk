from threading import Thread
import time

def faz_algo(i):
    print('Executando thread %d...' % i)
    time.sleep(3)
    print('Finalizando a thread %d...'% i)

for i in range(5):
    t = Thread(target = faz_algo(i),args= (i,))
    t.start()