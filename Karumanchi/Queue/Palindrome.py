from Karumanchi.Queue import Deque

"""
Check if the string is a palindrome using Deque
"""
def check_palindrome(input_deque):
    while input_deque.size()>1:
        if input_deque.remove_front() != input_deque.remove_rear():
            return False
    return True

if __name__=='__main__':
    deque = Deque.Deque()
    input_string = 'madam'
    input_string1 ='maam'
    input_string2='ragarrrr'
    input_string3 = 'testing'
    for char in input_string1:
        deque.add_rear(char)
    print(check_palindrome(deque))