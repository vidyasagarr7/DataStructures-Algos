"""
    Given a number k, find a from Array1 and b from Array2 such that a+b=k
"""

def find_numbers(array1,array2,k):
    """
    O(n^2) algorithm for finding if there exists two numbers
    :param array1:
    :param array2:
    :param k:
    :return:
    """
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] + array2[j] ==k:
                return True
    return False

"""
###############   Look for implementations   ##############
"""

def _binary_search(input_list,start,end,key):
    if key not in input_list:
        return False
    if start==end:
        if input_list[start]==key:
            return True
        else :
            return False

    mid = (start+end)//2
    if key<input_list[mid]:
        return _binary_search(input_list, start, mid-1, key)
    elif key>input_list[mid]:
        return _binary_search(input_list, mid+1, end, key)
    else:
        return True

    return False

def binary_search(input_list,key):
    return _binary_search(input_list,0,len(input_list),key)


def find_num(array1,array2,k):
    """
    O(n*ln(n)) algorithm for finding if there exists two numbers from two diff arrays
    :param arra1:
    :param array2:
    :param k:
    :return:
    """
    array1.sort()

    for i in range(len(array2)):
        temp = k - array2[i]
        binary_search(array1,temp)
    return False



if __name__=="__main__":
    test_input1 = [3,5,8,1,5,9,2,5,0,6]
    test_input2 = [12,11,14,15,17,18]
    print(find_numbers(test_input1,test_input2,21))
    print(find_num(test_input1,test_input2,21))
