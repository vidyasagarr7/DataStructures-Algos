"""
Find the smallest positive number missing from an unsorted array

You are given an unsorted array with both positive and negative elements.
You have to find the smallest positive number missing from the array in O(n) time using constant extra space.
 You can modify the original array.

Examples

 Input:  {2, 3, 7, 6, 8, -1, -10, 15}
 Output: 1

 Input:  { 2, 3, -7, 6, 8, 1, -10, 15 }
 Output: 4

 Input: {1, 1, 0, -1, -2}
 Output: 2

"""

def segregate_positive_and_negatives(input_list):

    left = 0
    for i in range(len(input_list)):
        if input_list[i] <= 0 :
            input_list[i],input_list[left] = input_list[left],input_list[i]
            left +=1
    return left

def find_smallest_positive(input_list):

    start = segregate_positive_and_negatives(input_list)

    return find_missing_positive(input_list[start:])


def find_missing_positive(input_list) :

    for i in range(len(input_list)):
        if abs(input_list[i] -1) < len(input_list) and input_list[abs(input_list[i]-1)]>0:
            input_list[abs(input_list[i]-1)] = - input_list[abs(input_list[i]-1)]


    for i in range(len(input_list)):
        if input_list[i] > 0:
            return i+1


if __name__=='__main__':
    input_list = [2, 3, 7, 6, 8, -1, -10, 15]
    print(find_smallest_positive(input_list))

    input_list = [2, 3, -7, 6, 8, 1, -10, 15 ]
    print(find_smallest_positive(input_list))

    input_list = [1, 1, 0, -1, -2]
    print(find_smallest_positive(input_list))




