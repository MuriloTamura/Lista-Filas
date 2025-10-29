#Inverta os primeiros k elementos de uma fila.

def revert_first_k(queue, k):
    stack = Stack()
    for _ in range(k):
        stack.push(queue.dequeue())
    
    while not stack.is_empty():
        queue.enqueue(stack.pop())
    
    for _ in range(queue.size() - k):
        queue.enqueue(queue.dequeue())
    return queue