from Karumanchi.Queue import Queue
from Karumanchi.Stack import Stack

def reverse_queue(input_que):
    stack = Stack.Stack()
    while not input_que.is_empty():
        stack.push(input_que.dequeue())
    while not stack.is_empty():
        input_que.enqueue(stack.pop())
    return input_que

if __name__=="__main__":
    que = Queue.Queue1()
    for i in range(10):
        que.enqueue(i)
    reverse_queue(que)
    while not que.is_empty():
        print(que.dequeue())