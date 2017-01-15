

"""
Find the maximum repeating number in O(n) time and O(1) extra space

Given an array of size n, the array contains numbers in range from 0 to k-1 where k is a positive integer and k <= n.
Find the maximum repeating number in this array. For example, let k be 10 the given array be
 arr[] = {1, 2, 2, 2, 0, 2, 0, 2, 3, 8, 0, 9, 2, 3}, the maximum repeating number would be 2.
 Expected time complexity is O(n) and extra space allowed is O(1). Modifications to array are allowed.

"""

def max_repeating(input_list,k):
    if not input_list :
        return
    else :

        for i in range(len(input_list)) :
            input_list[input_list[i]%k] += k

        _max = input_list[0]
        max_idx = 0
        for i in range(len(input_list)) :
            if input_list[i] > _max :
                _max = input_list[i]
                max_idx = i
        return max_idx

if __name__=='__main__':
    test = [1, 2, 2, 2, 0, 2, 0, 2, 3, 8, 0, 9, 2, 3]
    print(max_repeating(test,10))