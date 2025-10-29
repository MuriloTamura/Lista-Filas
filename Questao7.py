#Implemente uma pilha usando filas.

class PilhaComFilas:
    Q1 = Queue()
    Q2 = Queue()

def push(x):
    enqueue(Q2, x)
    while not isEmpty(Q1):
        enqueue(Q2, dequeue(Q1))
    Q1, Q2[:] = Q2, Q1  

def pop():
    if isEmpty(Q1):
        return None
    return dequeue(Q1)

def peek():
    if isEmpty(Q1):
        return None
    return Q1[0]

def isEmptyStack():
    return isEmpty(Q1)