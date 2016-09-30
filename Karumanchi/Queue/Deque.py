
class Deque:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items) ==0

    def add_front(self,item):
        self.items.insert(0,item)

    def add_rear(self,item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)
    def remove_rear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

if __name__=='__main__':
    deque = Deque()
    for i in range(1,5):
        deque.add_rear(i)
    for i in range(5,10):
        deque.add_front(i)
    while not deque.is_empty():
        print(deque.remove_rear())