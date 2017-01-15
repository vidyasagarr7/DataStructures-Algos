

"""
Find subarray with given sum | Set 1 (Nonnegative Numbers)

Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given number.

Examples:

Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4

Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
Ouptut: Sum found between indexes 1 and 4

Input: arr[] = {1, 4}, sum = 0
Output: No subarray found
There may be more than one subarrays with sum as the given sum. The following solutions print first such subarray.

"""

def print_subarray(input_list,s):
    if not input_list :
        return
    else :
        _sum = input_list[0]
        start = 0
        for i in range(1,len(input_list)):
            while _sum > s and start < i-1 :
                _sum = _sum - input_list[start]
                start += 1
            if _sum ==s  :
                print('start index : {} and end index : {}'.format(start,i-1))
                return

            _sum += input_list[i]

        return 'no sum found'
if __name__=='__main__':
    test = [1, 4, 20, 3, 10, 5]
    print(print_subarray(test,33))

    test2 = [1, 4, 0, 0, 3, 10, 5]
    print(print_subarray(test2,7))

    test3 = [1, 4]
    print(print_subarray(test3,0))


