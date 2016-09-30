from Karumanchi.Stack import Stack

def check_consecutive(input_stac):
    temp_stack = Stack.Stack()

    while not input_stac.is_empty():
        temp_stack.push(input_stac.pop())

    while not temp_stack.is_empty():
        temp = temp_stack.pop()
        if not temp_stack.is_empty():
            if abs(temp-temp_stack.pop())!=1:
                return False
        else:
            return True
    return True

if __name__=="__main__":
    temp_stack = Stack.Stack()
    temp_stack.push(4)
    temp_stack.push(5)
    temp_stack.push(-2)
    temp_stack.push(-3)
    temp_stack.push(11)
    temp_stack.push(10)
    temp_stack.push(5)
    temp_stack.push(6)
    print(check_consecutive(temp_stack))






