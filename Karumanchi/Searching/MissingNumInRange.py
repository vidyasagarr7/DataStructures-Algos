import sys
"""
Find the missing number in an array containing n numbers in  range of X to Y.
"""

def find_number(input_list,x,y):
    """
    O(n) time
    :return:
    """
    n = len(input_list)
    temp = [-sys.maxsize]*(n+1)

    for i in range(len(input_list)):
        temp[input_list[i]-x] = input_list[i]

    for i in range(len(temp)):
        if temp[i] == -sys.maxsize:
            return i+x

    return -1

if __name__=="__main__":
    test = [13,11,14,15,10]
    print(find_number(test,10,15))
