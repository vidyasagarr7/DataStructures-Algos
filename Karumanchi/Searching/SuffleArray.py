
"""
Given an array of the form a1,a2..an,b1,b2,..bn with 2n elements in it. shuffle the array to the form a1,b1,a2,b2...

"""

def shuffle_list(input_list):
    """
    O(n^2) - algorithm
    :param input_list:
    :return:
    """
    n = len(input_list)//2
    second_pointer = n
    aux = 1

    for i in range(len(input_list)//2):
        temp = second_pointer
        while temp > aux+i:
            input_list[temp],input_list[temp-1] = input_list[temp-1],input_list[temp]
            temp -=1
        second_pointer +=1
        aux +=1

    return input_list

def _shuffle_list(input_list):
    """
    Divide and conquer based algo - O(n*log(n))
    Algo : - consider n = 2^i  - only works for this case.
    - split the aray into two halves,
    - exchange the elements around the centre - second half of the first set with first half of the second set
    - recursively repeat

    :param input_list:
    :return:
    """



if __name__=="__main__":
    test = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19]
    print(shuffle_list(test))