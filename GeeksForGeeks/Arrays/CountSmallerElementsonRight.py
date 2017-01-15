"""
Count smaller elements on right side
Write a function to count number of smaller elements on right of each element in an array.
 Given an unsorted array arr[] of distinct integers, construct another array countSmaller[] such that countSmaller[i]
 contains count of smaller elements on right side of each element arr[i] in array.

Examples:

Input:   arr[] =  {12, 1, 2, 3, 0, 11, 4}
Output:  countSmaller[]  =  {6, 1, 1, 1, 0, 1, 0}

(Corner Cases)
Input:   arr[] =  {5, 4, 3, 2, 1}
Output:  countSmaller[]  =  {4, 3, 2, 1, 0}

Input:   arr[] =  {1, 2, 3, 4, 5}
Output:  countSmaller[]  =      {0, 0, 0, 0, 0}

"""

def count_elements(input_list):
    """
    Brute force approach - O(n^2) two loops.
    :param input_list:
    :return:
    """
    count_list = [0]*len(input_list)

    for i in range(len(input_list)):
        count = 0
        for j in range(i,len(input_list)):
            if input_list[j] < input_list[i]:
                count +=1
        count_list[i] = count
    return count_list


def _count_elements(input_list):

    # REVISIT this 

    """
    Use AVL tree / RBT - O(n*logn) time
    :param input_list:
    :return:
    """

    return 0


if __name__=='__main__':
    input_list = [5,4,3,2,1]
    print(count_elements(input_list))

    input_list = [12, 1, 2, 3, 0, 11, 4]
    print(count_elements(input_list))