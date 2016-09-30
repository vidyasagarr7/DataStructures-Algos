
class Queue:
    """
    Circular fized size array implementation of a Queue
    """
    def __init__(self,limit=10):
        self.queue =[]
        self.limit = limit
        self.rear = None
        self.front = None
        self.size= 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self,item):
        if self.size >= self.limit:
            return 'Queue overflow'
        else:
            self.queue.append(item)
            if self.rear == None and self.front==None:
                self.rear = self.front = 0
            else :
                self.rear = self.size
            self.size +=1

    def dequeue(self):
        if self.size <=0 :
            return 'Empty Queue'
        else :
            self.size -=1
            if self.size ==0 :
                self.front = self.rear = None
            else :
                self.rear -= 1
            return self.queue.pop(0)

    def queue_rear(self):
        if self.size ==0:
            return 'Empty Queue'
        else:
            return self.queue[self.size-1]

    def queue_front(self):
        if self.size ==0 :
            return 'Empty Queue'
        else:
            return self.queue[0]

    def size(self):
        return self.size


class Node:
    """
    Linkedlist node for implemeting a queue
    """
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Queue1:
    """
    Linkedlist implementation of a Queue.
    """
    def __init__(self):
        self.head=None
        self.tail = None
        self.size = 0

    def enqueue(self,item):
        new_node = Node(item)
        if self.size ==0:
            self.head = self.tail = new_node
        else :
            temp = self.tail
            temp.next = new_node
            self.tail = new_node
        self.size +=1

    def dequeue(self):
        if self.size <=0:
            return 'empty queue'
        else:
            temp = self.head
            self.head = temp.next
            self.size -=1
            return temp.data

    def is_empty(self):
        return self.size ==0

    def queue_rear(self):
        if self.size == 0:
            return 'Empty Queue'
        else :
            return self.tail.data

    def queue_front(self):
        if self.size ==0:
            return 'Empty Queue'
        else:
            return self.head.data

    def size(self):
        return self.size


if __name__=="__main__":

    que = Queue()
    for i in range(10):
        que.enqueue(i)
    for i in range(5):
        print(que.dequeue())

    print(que.queue_front())
    print(que.queue_rear())


    que1 = Queue1()
    for i in range(10):
        que1.enqueue(i)
    for i in range(5):
        print(que1.dequeue())

    print(que1.queue_front())
    print(que1.queue_rear())

