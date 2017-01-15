import copy

"""
Convert an array to reduced form

Given an array with n distinct elements, convert the given array to a form where all elements are in range
from 0 to n-1. The order of elements is same, i.e., 0 is placed in place of smallest element, 1 is placed for
second smallest element, … n-1 is placed for largest element.

Input:  arr[] = {10, 40, 20}
Output: arr[] = {0, 2, 1}

Input:  arr[] = {5, 10, 40, 30, 20}
Output: arr[] = {0, 1, 4, 3, 2}
Expected time complexity is O(n Log n).


"""

def binary_search(input_lst,start,end,element) :
    if not input_lst :
        return
    else :
        if start <= end :
            mid = start + (end-start)//2
            if input_lst[mid] == element :
                return mid
            elif input_lst[mid] > element :
                return binary_search(input_lst,start,mid-1,element)
            else  :
                return binary_search(input_lst,mid+1,end,element)

def binary_se(input_list,element) :
    #print('searching for element : {}'.format(element))
    start = 0
    end = len(input_list)-1

    while start <= end :
        mid = start + (end-start)//2
        #print('mid : {}'.format(mid))
        if input_list[mid] == element :
            return mid
        elif input_list[mid] > element :
            end = mid-1
        else :
            start = mid+1
    return

def _bin_search(input_list,element) :
    return binary_search(input_list,0,len(input_list)-1,element)

def reduced_form(input_list) :
    if not input_list :
        return
    else :

        temp = sorted(input_list)
        #temp.sort()

        for i in range(len(input_list)) :
            index = _bin_search(temp,input_list[i])
            input_list[i] = index

        return input_list


if __name__=='__main__':
    test = [4,8,2,7,9,5]
    test.sort()
    #print(binary_search(sorted(test),0,len(test),9))



    test = [4, 8, 2, 7, 9, 5]
    print(reduced_form(test))