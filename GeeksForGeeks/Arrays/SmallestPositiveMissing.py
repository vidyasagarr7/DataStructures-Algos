
"""
Find the smallest positive number missing from an unsorted array

You are given an unsorted array with both positive and negative elements.
You have to find the smallest positive number missing from the array in O(n) time using
constant extra space. You can modify the original array.
"""

def segregate(input_list):
    if not input_list :
        return
    else :
        start = 0
        end  = len(input_list)-1
        while start < end :
            if input_list[end] < 0 :
                input_list[end],input_list[start] = input_list[start],input_list[end]
                start += 1
            else :
                end -= 1
        return start

def smallest_pos(input_list):
    if not input_list :
        return
    else :
        start = segregate(input_list=input_list)
        """

        for i in range(start,len(input_list)) :
            if abs(input_list[i]) < len(input_list) and input_list[abs(input_list[i])-1] > 0 :
                input_list[abs(input_list[i])-1] = - input_list[abs(input_list[i])-1]

        for i in range(start,len(input_list)):
            if input_list[i] > 0 :
                return i-start+1
        """
        return find_first_missing(input_list[start:])


def find_first_missing(input_list):
    if not input_list :
        return
    else :
        for i in range(len(input_list)):
            if abs(input_list[i]) < len(input_list) and input_list[abs(input_list[i])-1] > 0 :
                input_list[abs(input_list[i])-1] = - input_list[abs(input_list[i])-1]
        for i in range(len(input_list)):
            if input_list[i] > 0 :
                return i+1


def find_missing(input_list,start):
    if not input_list:
        return
    else :
        for i in range(start,len(input_list)):
            if abs(input_list[i]) < len(input_list) and input_list[abs(input_list[i])-1] > 0 :
                #print(input_list[abs(input_list[i])-1])
                input_list[abs(input_list[i])-1] = - input_list[abs(input_list[i])-1]
        print(input_list)
        for i in range(start,len(input_list)) :
            if input_list[i] > 0 :
                return i-start+1

if __name__=='__main__':

    test = [1,-2,2,3,6,-5,2,-9,10,-3,8,4,9,-4,-5,-6,4]
    #print(segregate(input_list=test))
    print(smallest_pos(test))

    test1 = [2, 3, 7, 6, 8, -1, -10, 15]
    print(smallest_pos(test1))

    test2 = [ 2, 3, -7, 6, 8, 1, -10, 15 ]
    print(smallest_pos(test2))

    test3 = [1, 1, 0, -1, -2]
    print(smallest_pos(test3))
    #testing = [2,4,6,7,8,3,6,9,4,6,1,0]
    #print(find_first_missing(testing))

    #test2 = [-1,-3,-5,2,4,6,7,8,3,6,9,4,6,1,0]
    #print(find_missing(test2,3))