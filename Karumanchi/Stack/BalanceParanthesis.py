from Karumanchi.Stack import Stack

def check_paranthesis(input_string):
    stack = Stack.Stack()
    open_braces = '{(['
    closed_braces = '})]'
    for element in input_string:
        if element in open_braces:
            stack.push(element)
        elif element in closed_braces:
            if not stack.is_empty():
                poped_element = stack.pop()
            else :
                return 'unbalanced paranthesis'
            if closed_braces.index(element) != open_braces.index(poped_element):
                return 'Unbalanced paranthesis'
    if stack.is_empty():
        return 'balanced paranthesis'
    else :
        return 'unbalanced paranthesis'

if __name__=="__main__":
    test_input='[(])'
    test_input1= '[()]{}{[()()]()}'
    print(check_paranthesis(test_input))
    print(check_paranthesis(test_input1))