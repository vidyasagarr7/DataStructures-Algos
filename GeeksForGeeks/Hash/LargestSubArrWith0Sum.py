

"""
Find the largest subarray with 0 sum
Given an array of integers, find length of the largest subarray with sum equals to 0.

Examples:

Input: arr[] = {15, -2, 2, -8, 1, 7, 10, 23};
Output: 5
The largest subarray with 0 sum is -2, 2, -8, 1, 7

Input: arr[] = {1, 2, 3}
Output: 0
There is no subarray with 0 sum

Input: arr[] = {1, 0, 3}
Output: 1

"""

def largest_subarray(input_list):
    if not input_list :
        return
    else  :
        cur_sum = 0
        htable = {}
        max_len = 0
        for i in range(len(input_list)):
            cur_sum += input_list[i]

            if input_list[i] == 0 and max_len==0:
                max_len = 1

            if cur_sum == 0 :
                max_len = i+1

            if cur_sum in htable:
                max_len = max(max_len,i-htable[cur_sum])
            else :
                htable[cur_sum] = i

        return max_len

if __name__=='__main__':
    test = [-2, 2, -8, 1, 7, 10, 23]
    print(largest_subarray(test))

    test2 = [1, 2, 3]
    print(largest_subarray(test2))

    test3 = [1,0,3]
    print(largest_subarray(test3))