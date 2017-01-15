"""

Maximum Length Bitonic Subarray

Given an array A[0 … n-1] containing n positive integers, a subarray A[i … j] is bitonic
 if there is a k with i <= k <= j such that A[i] <= A[i + 1] ... <= A[k] >= A[k + 1] >= .. A[j – 1] > = A[j].
 Write a function that takes an array as argument and returns the length of the maximum length bitonic subarray.

Expected time complexity of the solution is O(n)

Simple Examples
1) A[] = {12, 4, 78, 90, 45, 23}, the maximum length bitonic subarray is {4, 78, 90, 45, 23} which is of length 5.

2) A[] = {20, 4, 1, 2, 3, 4, 2, 10}, the maximum length bitonic subarray is {1, 2, 3, 4, 2} which is of length 5.

Extreme Examples
1) A[] = {10}, the single element is bitnoic, so output is 1.

2) A[] = {10, 20, 30, 40}, the complete array itself is bitonic, so output is 4.

3) A[] = {40, 30, 20, 10}, the complete array itself is bitonic, so output is 4

"""

def find_max_length(input_list):

    if len(input_list) ==1 or len(input_list)==0 :
        return len(input_list)
    else :

        # increasing sequence starting at index i
        inc_seq = [1]*len(input_list)
        i = 1
        while i < len(input_list) :
            if input_list[i] > input_list[i-1]:
                inc_seq[i] = inc_seq[i-1]+1
            else :
                inc_seq[i] = inc_seq[i-1]
            i += 1

        # decreasing sequence starting at index i
        dec_seq = [1]*len(input_list)
        j = len(input_list)-2
        while j >= 0 :
            if input_list[j] > input_list[j+1] :
                dec_seq[j] = dec_seq[j+1] + 1
            else :
                dec_seq[j] = dec_seq[j+1]

            j -=1

        # find max
        _max = 0
        for i in range(len(input_list)):
            if inc_seq[i]+dec_seq[i]-1 > _max :
                _max = inc_seq[i] + dec_seq[i] -1
        return _max


if __name__=='__main__':
    input_list = [12, 4, 78, 90, 45, 23]
    print(find_max_length(input_list))

    input_list = [20, 4, 1, 2, 3, 2,1, 10]
    print(find_max_length(input_list))

    input_list = [1]
    print(find_max_length(input_list))

    input_list = [1,2,3,4,5]
    print(find_max_length(input_list))

    input_list = [5,4,3,2,1]
    print(find_max_length(input_list))





