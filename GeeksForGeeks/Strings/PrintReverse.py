"""
Print reverse of a string using recursion

"""

def print_reverse(string,k=0):
    """
    Recursive implementation to print reverse of a string
    :param string:
    :return:
    """
    if  k > len(string)-1:
        return ''
    print_reverse(string,k+1)
    #print(string[k],end='')
    if k==0 :
        print(string[k])
    else  :
        print(string[k],end='')

def _print_reverse(string):
    return print(string[::-1])

if __name__=='__main__':
    string = 'geeksfor'
    print_reverse(string)

    #_print_reverse(string)

    #reversed(string)
    #print(string)