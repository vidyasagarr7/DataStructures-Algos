
"""

Check whether a given string is an interleaving of two other given strings

Given three strings A, B and C. Write a function that checks whether C is an interleaving of A and B.
C is said to be interleaving A and B, if it contains all characters of A and B and order of all characters
in individual strings is preserved. See previous post for examples.
"""

def check_interleaving(list1,list2,outlist):
    first = 0
    second = 0
    current = 0

    if len(outlist) != len(list1) + len(list2):
        return False

    while current < len(outlist) :
        if outlist[current] == list1[first] :
            first += 1
        elif outlist[current] == list2[second] :
            second += 1
        else :
            return False
        current += 1
    if first != len(list1) or second != len(list2) :
        return False
    return True



if __name__ == '__main__' :
    one = list('ab')
    two = list('cd')
    out = list('cadb')
    print(check_interleaving(one,two,out))

    out = list('cdab')
    print(check_interleaving(one,two,out))

    out = list('cbad')
    print(check_interleaving(one,two,out))
    out = list('abcduyrbvh')
    print(check_interleaving(one,two,out))
    out = list('dskajfdjsafk')
    print(check_interleaving(one,two,out))