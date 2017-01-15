

"""
Given an array arr[], find the maximum j – i such that arr[j] > arr[i]

Examples:

  Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
  Output: 6  (j = 7, i = 1)

  Input: {9, 2, 3, 4, 5, 6, 7, 8, 18, 0}
  Output: 8 ( j = 8, i = 0)

  Input:  {1, 2, 3, 4, 5, 6}
  Output: 5  (j = 5, i = 0)

  Input:  {6, 5, 4, 3, 2, 1}
  Output: -1

"""

def find_max_diff(input_list):
    if not input_list :
        return
    else :
        l_min = [0]*len(input_list)
        r_max = [0]*len(input_list)

        l_min[0] = input_list[0]
        for i in range(1,len(input_list)):
            l_min[i] = min(l_min[i-1],input_list[i])

        r_max[len(input_list)-1] = input_list[len(input_list)-1]
        for i in range(len(input_list)-2,-1,-1):
            r_max[i] = max(input_list[i],r_max[i+1])

        max_diff = -1
        _min_idx = 0
        _max_idx = 0
        while _min_idx < len(input_list) and _max_idx < len(input_list) :
            if l_min[_min_idx] < r_max[_max_idx] :
                max_diff = max(max_diff , _max_idx - _min_idx)
                _max_idx += 1
            else :
                _min_idx += 1
        return max_diff


if __name__=='__main__':

    test1 = [34, 8, 10, 3, 2, 80, 30, 33, 1]
    print(find_max_diff(test1))

    test2 = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
    print(find_max_diff(test2))

    test3 = [1, 2, 3, 4, 5, 6]
    print(find_max_diff(test3))

    test4 = [6,5,4,3,2,1]
    print(find_max_diff(test4))









