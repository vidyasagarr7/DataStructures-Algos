from Karumanchi.Stack import Stack

def reverse_elements(input_string):
    """
    Algorithm to reverse the elements of the string using stack
    :param input_string:
    :return:
    """
    new_stack = Stack.Stack()
    for char in input_string:
        new_stack.push(char)
    while not new_stack.is_empty():
        print(new_stack.pop())


if __name__=="__main__":
    test = 'sagar'
    print(reverse_elements(test))