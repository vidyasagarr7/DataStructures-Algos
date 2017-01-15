"""
Implement two stacks in an array

Create a data structure twoStacks that represents two stacks. Implementation of twoStacks should use only one array,
i.e., both stacks should use the same array for storing elements. Following functions must be supported by twoStacks.

push1(int x) –> pushes x to first stack
push2(int x) –> pushes x to second stack

pop1() –> pops an element from first stack and return the popped element
pop2() –> pops an element from second stack and return the popped element

Implementation of twoStack should be space efficient.


"""

class TwoStacks:
    def __init__(self,size):
        self.size = size
        self.array = [None]*size
        self.top1 = -1
        self.top2 = size-1

    # pushing elements to first stack
    def push1(self, item):
        # check if there is space to push elements
        if self.top1 < self.top2-1   :
            self.top1 += 1
            self.array[self.top1] = item
        # over flow of stace
        else :
            print('Memory full, no space to insert')

    # pushing elements to second stack

    def push2(self,item):
        # check if there is space to push elements
        if self.top1 < self.top2 -1 :
            self.top2 -= 1
            self.array[self.top2] = item
        # over flow
        else:
            print('Memory fill. No space to insert')

    def pop1(self):
        # check if there are elements in the first stack
        if self.top1 > 0 :
            item = self.array[self.top1]
            self.array[self.top1] = None
            self.top1 -= 1
            return item

    def pop2(self):
        #check if there are elements in the second stack
        if self.top2 < self.size-1  :
            item = self.array[self.top2]
            self.array[self.top2] = None
            self.top2  -= 1
            return item

    def print_stack(self):
        for j in range(len(self.array)):
            print(self.array[j])

if __name__=='__main__':
    ts = TwoStacks(30)
    for i in range(1,10):
        ts.push1(i)
    for j in range(30,20,-1):
        ts.push2(j)

    ts.print_stack()
