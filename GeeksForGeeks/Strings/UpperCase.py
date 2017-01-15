

"""
Lower case to upper case – An interesting fact
Problem: Given a string containing only lowercase letters, generate a string with the same letters, but in uppercase.

Input : GeeksForGeeks
Output : GEEKSFORGEEKS
"""

def uppercase(input_string):
    if not input_string :
        return
    else :
        for i in range(len(input_string)) :
            if ord(input_string[i]) <= ord('z') and ord(input_string[i]) >= ord('a') :
                input_string[i] = chr(ord(input_string[i])-ord('a')+ord('A'))
        return ''.join(input_string)

def upper_case(input_string):
    return input_string.upper()

def _uppercase(input_string):
    if not input_string :
        return
    else :
        for i in range(len(input_string)) :
            if ord(input_string[i]) & (1<<5) :
                input_string[i] = chr( ord(input_string[i]) & ~(1<<5))
        return ''.join(input_string)





if __name__=='__main__':
    lower = 'Sagar'
    print(uppercase(list(lower)))

    print(_uppercase(list(lower)))

    print(upper_case(lower))

