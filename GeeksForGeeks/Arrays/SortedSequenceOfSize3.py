
"""

Find a sorted subsequence of size 3 in linear time

Given an array of n integers, find the 3 elements such that a[i] < a[j] < a[k] and i < j < k in 0(n) time.
If there are multiple such triplets, then print any one of them.

Examples:

Input:  arr[] = {12, 11, 10, 5, 6, 2, 30}
Output: 5, 6, 30

Input:  arr[] = {1, 2, 3, 4}
Output: 1, 2, 3 OR 1, 2, 4 OR 2, 3, 4

Input:  arr[] = {4, 3, 2, 1}
Output: No such triplet

"""

def find_sorted_seq(input_list):
    if not input_list :
        return
    else :
        l_min = 0
        r_max = len(input_list)-1

        left_min = [-1]*len(input_list)
        right_max = [-1]* len(input_list)


        for i in range(1,len(input_list)):
            if input_list[i] <= input_list[l_min] :
                l_min = i
                left_min[i] = -1
            else  :
                left_min[i] = l_min

        for i in range(len(input_list)-2,-1,-1):
            if input_list[i] >= input_list[r_max] :
                r_max = i
                right_max[i] = -1
            else :
                right_max[i] = r_max

        print(left_min)
        print(right_max)
        #print(input_list)

        for i in range(len(input_list)):
            if left_min[i] >= 0 and right_max[i] >= 0 :
                print(' {}, {} and {}'.format(input_list[left_min[i]],input_list[i],input_list[right_max[i]]))
                return

if __name__=='__main__':
    test1 = [12, 11, 10, 5, 6, 2, 30]

    test2 = [1, 2, 3, 4]

    test3 = [4, 3, 2, 1]

    print(find_sorted_seq(test1))

    print(find_sorted_seq(test2))

    print(find_sorted_seq(test3))










