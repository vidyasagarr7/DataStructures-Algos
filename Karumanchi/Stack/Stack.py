
class Stack1:
    """
    Stack implementation using fixed size array
    """
    def __init__(self,limit=None):
        self.stack = []
        self.limit = limit

    def is_empty(self):
        return not len(self.stack)

    def push(self,data):
        if len(self.stack) >= self.limit:
            return 'stack overflow'
        else :
             return self.stack.append(data)

    def pop(self):
        if len(self.stack) <= 0 :
            return 'empty stack'
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) <= 0:
            return 'stack is empty'
        else:
            length = len(self.stack)
            return self.stack[length-1]

    def size(self):
        return len(self.stack)


class Stack2:
    """
    Stack implementation with dynamic array size
    """
    def __init__(self,limit=20):
        self.stack = [None]*limit
        self.limit = limit

    def is_empty(self):
        return not self.stack

    def push(self,item):
        if len(self.stack)>=self.limit:
            self.limit *=2
            new_stack = list(self.stack)
            self.stack = new_stack
        self.stack.append(item)

    def pop(self):
        if len(self.stack) <= 0 :
            return 'empty stack'
        else :
            return self.stack.pop()

    def peek(self):
        if len(self.stack)==0:
            return 'empty stack'
        else :
            length = len(self.stack)
            return self.stack[length-1]

    def size(self):
        return len(self.stack)

class Node :
    def __init__(self,data=None):
        self.data= data
        self.next = None

    def set_data(self,value):
        self.data = value
    def get_data(self):
        return self.data

    def set_next(self,value):
        self.next = value
    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None


class Stack:
    """
    Linkedlist implementation of stack
    """
    def __init__(self,values=None):
        self.head = None
        self.size = 0
        if values:
            for value in values:
                self.push(value)

    def push(self,item):
        new_node = Node(item)
        if not self.head:
            self.head=new_node
        else:
            current_node = self.head
            self.head=new_node
            self.head.next = current_node
        self.size +=1

    def pop(self):
        if not self.head:
            return 'stack is empty'
        else :
            temp = self.head.data
            self.head = self.head.next
            self.size -=1
            return temp

    def peek(self):
        if not self.head:
            return 'empty stack'
        else :
            return self.head.data
    def is_empty(self):
        return self.head==None


if __name__=="__main__":
    # test code for Stack1 class
    stk = Stack1(20)
    for i in range(10):
        stk.push(i)
    for i in range(6):
        print(stk.pop())
    print(stk.peek())
    print(stk.pop())
    print(stk.peek())

    # test code for stack2 class
    stack2 = Stack2()
    for i in range(25):
        stack2.push(i)
    print(stack2.size())
    for i in range(10):
        print(stack2.pop())

    test = ['satar','vijay','ramu']
    stack = Stack(test)
    for i in range(len(test)):
        print(stack.pop())




