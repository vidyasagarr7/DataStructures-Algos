

"""
Find four elements a, b, c and d in an array such that a+b = c+d
Given an array of distinct integers, find if there are two pairs (a, b) and (c, d) such that a+b = c+d, and a, b, c and d are distinct elements. If there are multiple answers, then print any of them.

Example:

Input:   {3, 4, 7, 1, 2, 9, 8}
Output:  (3, 8) and (4, 7)
Explanation: 3+8 = 4+7

Input:   {3, 4, 7, 1, 12, 9};
Output:  (4, 12) and (7, 9)
Explanation: 4+12 = 7+9

Input:  {65, 30, 7, 90, 1, 9, 8};
Output:  No pairs found
Expected Time Complexity: O(n2)

"""

def find_4_elements(input_list):
    if not input_list :
        return
    else :
        htable = {}

        for i in range(len(input_list)):
            for j in range(i+1,len(input_list)):
                _sum = input_list[i] + input_list[j]
                if _sum in htable :
                    _i,_j = htable[_sum]
                    print((input_list[i],input_list[j]),(input_list[_i],input_list[_j]))
                else :
                    htable[_sum] = (i,j)
if __name__=='__main__':
    test = [3, 4, 7, 1, 2, 9, 8]
    find_4_elements(test)

    print('*******')

    test2 = [65, 30, 7, 90, 1, 9, 8]
    find_4_elements(test2)

    print('*******')

    test3 = [3, 4, 7, 1, 12, 9]
    find_4_elements(test3)

