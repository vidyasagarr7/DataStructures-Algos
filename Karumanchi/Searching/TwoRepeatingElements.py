import math
"""
Find two repeating elements in a given array : 1-n
"""

def find_repeating(input_list):
    """
    O(n) time
    :param input_list:
    :return:
    """

    table = {}
    for element in input_list:
        if element in table and table[element] ==1:
            print(element)
            table[element] +=1
        elif element in table:
            table[element] += 1
        elif element is not None:
            table[element] = 1


## revisit this - find two's complement - one of the numbers is more than its value  -- Change the code. 
def _find_repeating(input_list):
    """
    Use XOR
    :param input_list:
    :return:
    """
    x=0
    p = q =0
    n=len(input_list)
    for i in range(len(input_list)):
        x = x^input_list[i]

    for i in range(n+1):
        x = x^i

    right_bit = x & (~x +1)
    for i in range(len(input_list)):
        if input_list[i]& right_bit:
            p= p^input_list[i]
        else:
            q = q^input_list[i]

    for i in range(1,len(input_list)+1):
        if i&right_bit:
            p=p^i
        else:
            q = q^i

    print(p,q)




if __name__=="__main__":
    test = [1,1,2,2,3,4,5,6,7,8,9]
    print(find_repeating(test))


    test2 = [1,2,3,4,5,6,5,7,8,8,9]
    print(_find_repeating(test2))