"""

Largest subarray with equal number of 0s and 1s

Given an array containing only 0s and 1s, find the largest subarray which contain equal no of 0s and 1s.
Expected time complexity is O(n).

Examples:

Input: arr[] = {1, 0, 1, 1, 1, 0, 0}
Output: 1 to 6 (Starting and Ending indexes of output subarray)

Input: arr[] = {1, 1, 1, 1}
Output: No such subarray

Input: arr[] = {0, 0, 1, 1, 0}
Output: 0 to 3 Or 1 to 4

"""

def findmax_sarr(arr):
    # left sum array - sum of all elements to the left from the current number
    left_sum = [0]*len(arr)

    # we only have 0's or 1's
    left_sum[0] = 1 if arr[0]== 1 else -1

    for i in range(1,len(arr)):
        if arr[i] ==0 :
            left_sum[i] = left_sum[i-1]-1
        elif arr[i] == 1 :
            left_sum[i] = left_sum[i-1]+1
    htable = {}
    max_diff = -1
    start = -1
    end = -1
    for j in range(len(left_sum)):
        if left_sum[j] not in htable :
            htable[left_sum[j]] = j
        else :
            if abs(j - htable[left_sum[j]]) > max_diff :
                max_diff = j-htable[left_sum[j]]
                start = htable[left_sum[j]]
                end = j

    if start != -1 and end != -1 :
        return start,end
    else  :
        return 'there exists no substring'

if __name__=='__main__':

    arr = [1, 0, 1, 1, 1, 0, 0]
    print(findmax_sarr(arr))


