
"""

Print all interleavings of given two strings
Given two strings str1 and str2, write a function that prints all interleavings of the given two strings.
 You may assume that all characters in both strings are different

Example:

Input: str1 = "AB",  str2 = "CD"
Output:
    ABCD
    ACBD
    ACDB
    CABD
    CADB
    CDAB

Input: str1 = "AB",  str2 = "C"
Output:
    ABC
    ACB
    CAB

"""

def print_interleavings(list1,list2,outlist,first,second,index):

    if first==len(list1) and second == len(list2) :
        print(''.join(outlist))
    else :

        if first < len(list1) :
            outlist[index] = list1[first]
            print_interleavings(list1,list2,outlist,first+1,second,index+1)
        if second < len(list2) :
            outlist[index] = list2[second]
            print_interleavings(list1,list2,outlist,first,second+1,index+1)

if __name__=='__main__':
    one = 'ab'
    two = 'cd'
    out = ['']*(len(one)+len(two))
    print_interleavings(list(one),list(two),out,0,0,0)







