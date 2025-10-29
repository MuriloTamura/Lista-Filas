#Implemente uma fila através de duas pilhas. Não crie variáveis,
#use apenas as operações das pilhas e não use recursão.

class FilacomduasPilhas:
    
    S1 = stack()
    S2 = stack()

    def enqueue(item):
        push(S1, item)

    def dequeue():
        if S2.is_empty():
            while not isEmpty(S1):
                push(S2, pop(S1))
        return pop(S2)        

    
