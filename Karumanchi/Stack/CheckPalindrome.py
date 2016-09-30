from Karumanchi.Stack import  Stack

def _check_palindrome(input_string):
    """
    Algorithm to check if an input string is a palindrome
    :param input_string:
    :return:
    """
    length = len(input_string)
    stack = Stack.Stack()
    mid=0
    if length%2==0:
        mid = length//2
    else:
        mid = length//2+1
    for i in range(mid):
        stack.push(input_string[i])
    if length%2 ==1:
        stack.pop()
    for i in range(mid):
        if stack.pop() != input_string[mid+i]:
            return 'not palindrome'
        else :
            return 'palindrome'

def check_palindrome(input_str):
    stk = Stack.Stack()
    palindrome = False
    for char in input_str:
        stk.push(char)
    for char in input_str:
        if char == stk.pop():
            palindrome = True
        else :
            palindrome = False
    return palindrome

if __name__=="__main__":
    test = 'madam'
    test1 = 'maam'
    test2 = 'massam'
    test3 = 'masma'
    input = 'ababaababXbabaababa'
    print(_check_palindrome(test))
    print(_check_palindrome(test1))
    print(_check_palindrome(test2))
    print(_check_palindrome(test3))
    print(_check_palindrome(input))

