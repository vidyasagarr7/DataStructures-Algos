

"""
Rearrange an array so that arr[i] becomes arr[arr[i]] with O(1) extra space
Given an array arr[] of size n where every element is in range from 0 to n-1. Rearrange the given array so that
 arr[i] becomes arr[arr[i]]. This should be done with O(1) extra space.

Examples:

Input: arr[]  = {3, 2, 0, 1}
Output: arr[] = {1, 0, 3, 2}

Input: arr[] = {4, 0, 2, 1, 3}
Output: arr[] = {3, 4, 2, 0, 1}

Input: arr[] = {0, 1, 2, 3}
Output: arr[] = {0, 1, 2, 3}
If the extra space condition is removed, the question becomes very easy. The main part of the question is to do it
without extra space.

"""

def rearrange(input_list):
    if not input_list :
        return
    else :
        n = len(input_list)
        for i in range(len(input_list)) :
            input_list[i] += (input_list[input_list[i]]%n)*n
        for i in range(len(input_list)):
            input_list[i] = input_list[i]//n
        return input_list

if __name__=='__main__':
    test = [3, 2, 0, 1]
    print(rearrange(test))

    test = [4,0,2,1,3]
    print(rearrange(test))

    test = [0,1,2,3]
    print(rearrange(test))