
"""

Print all possible strings that can be made by placing spaces
Given a string you need to print all possible strings that can be made by placing spaces (zero or one) in between them.

Input:  str[] = "ABC"
Output: ABC
        AB C
        A BC
        A B C


"""
def toString(List):
    s = []
    for x in List:
        if x == '\0':
            break
        s.append(x)
    return ''.join(s)

def print_string(string,out_str,i,j):
    if i == len(string) :
        out_str[j] = '\0'
        print(toString(out_str))
        return

    out_str[j] = string[i]
    print_string(string,out_str,i+1,j+1)

    out_str[j] = ' '
    out_str[j+1] = string[i]
    print_string(string,out_str,i+1,j+2)

def print_strings(string):
    n = len(string)
    out_str = [0]*2*n

    out_str[0]=string[0]
    print_string(string,out_str,1,1)

if __name__=='__main__':
    string = 'abc'
    print(print_strings(string))




