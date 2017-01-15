
"""
Change case
"""

def changecase(input_string):
    if not input_string :
        return
    else :
        for i in range(len(input_string)):
            if ord(input_string[i]) & (1<<5):
                input_string[i] = chr(ord(input_string[i]) & ~(1<<5))
            else :
                input_string[i] = chr(ord(input_string[i]) | (1<<5))
        return ''.join(input_string)

if __name__=='__main__':
    test = 'GeeksForGeeks'
    print(changecase(list(test)))