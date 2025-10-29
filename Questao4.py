"""
Considere um deque D que contém os números (1,2,3,4,5,6,7,8), nessa ordem. 
Suponha ainda que há uma fila Q, inicialmente vazia. 
Elabore um trecho de código que usando apenas D e Q 
(sem variáveis adicionais) e resulte em Q armazenando os elementos na ordem (1,2,3,4,5,6,7,8).
"""

def Armazena_em_Q():
    D = Qeque([1, 2, 3, 4, 5, 6, 7, 8])
    Q = Queue()

    while not D.is_empty():
        Q.enqueue(D.pop())
        
    print(f"Queue: {Q.items}")

