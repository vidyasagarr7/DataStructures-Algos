from Karumanchi.Stack import  Stack

class QueueFromStacks():
    def __init__(self):
        self.stack1=Stack.Stack()
        self.stack2=Stack.Stack()
        self.size = 0

    def enqueue(self,item):
        self.stack1.push(item)
        self.size +=1

    def dequeue(self):
        if self.stack1.size==0:
            return 'Empty Queue'
        else:
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
            temp = self.stack2.pop()
            while not self.stack2.is_empty():
                self.stack1.push(self.stack2.pop())
            self.size -= 1
            return temp


    def is_empty(self):
        return self.size ==0

    def size(self):
        return self.size


if __name__=="__main__":

    que = QueueFromStacks()
    for i in range(10):
        que.enqueue(i)
    for i in range(5):
        print(que.dequeue())
