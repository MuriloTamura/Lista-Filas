#Implemente um deque através de duas pilhas. 
#Não crie variáveis, use apenas as operações das pilhas e não use recursão.

class DequeComDuasPilhas:

    S1 = []  # frente
    S2 = []  # trás

def insertFront(x):
    push(S1, x)

def insertRear(x):
    push(S2, x)

def deleteFront():
    if isEmpty(S1):
        while not isEmpty(S2):
            push(S1, pop(S2))
    return pop(S1)

def deleteRear():
    if isEmpty(S2):
        while not isEmpty(S1):
            push(S2, pop(S1))
    return pop(S2)