
from Karumanchi.Queue import Queue
from Karumanchi.Stack import Stack

def reverse_first_k(input_que,k):
    stack = Stack.Stack()
    count = 0
    while count<k:
        stack.push(input_que.dequeue())
        count +=1
    while not stack.is_empty():
        input_que.enqueue(stack.pop())
    for i in range(input_que.size-k):
        input_que.enqueue(input_que.dequeue())



if __name__=="__main__":
    que = Queue.Queue1()
    for i in range(1,10):
        que.enqueue(i*10)
    reverse_first_k(que,4)
    while not que.is_empty():
        print(que.dequeue())