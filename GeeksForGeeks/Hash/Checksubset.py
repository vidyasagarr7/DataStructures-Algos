"""
Find whether an array is subset of another array | Added Method 3

Given two arrays: arr1[0..m-1] and arr2[0..n-1]. Find whether arr2[] is a subset of arr1[] or not.
Both the arrays are not in sorted order. It may be assumed that elements in both array are distinct.

Examples:
Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1}
Output: arr2[] is a subset of arr1[]

Input: arr1[] = {1, 2, 3, 4, 5, 6}, arr2[] = {1, 2, 4}
Output: arr2[] is a subset of arr1[]

Input: arr1[] = {10, 5, 2, 23, 19}, arr2[] = {19, 5, 3}
Output: arr2[] is not a subset of arr1[]

"""

def find_subset(arr1,arr2):
    # storing elements of second arr in hashtable
    hash1 = {}
    for i in arr2 :
        hash1[i] = 1

    for j in arr1 :
        if j in hash1 :
            hash1[j] -= 1

    for k in hash1 :
        if hash1[k] > 0 :
            return False
    return True

NO_CHARS = 256
def _check_subset(ar1,ar2):
    _hash = {}
    for ch in ar1 :
        _hash[ch] = 1

    for ch2 in ar2 :
        if ch2 not in _hash :
            return False
    return True

if __name__ =='__main__':
    arr1 = [1,2,3,4,5,6]
    arr2 = [1,2,10]
    print(find_subset(arr1,arr2))
    print(_check_subset(arr1,arr2))

    arr1 = [1, 2, 3, 4, 5, 6]
    arr2 = [1, 2, 5]
    print(find_subset(arr1, arr2))

    print(_check_subset(arr1,arr2))
