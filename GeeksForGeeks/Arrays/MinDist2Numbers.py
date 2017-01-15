
"""
Find the minimum distance between two numbers

Given an unsorted array arr[] and two numbers x and y, find the minimum distance between x and y in arr[].
The array might also contain duplicates. You may assume that both x and y are different and present in arr[].

Examples:
Input: arr[] = {1, 2}, x = 1, y = 2
Output: Minimum distance between 1 and 2 is 1.

Input: arr[] = {3, 4, 5}, x = 3, y = 5
Output: Minimum distance between 3 and 5 is 2.

Input: arr[] = {3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3}, x = 3, y = 6
Output: Minimum distance between 3 and 6 is 4.

Input: arr[] = {2, 5, 3, 5, 4, 4, 2, 3}, x = 3, y = 2
Output: Minimum distance between 3 and 2 is 1.

X and Y - interchangable
"""

def find_min_distance(input_list,x,y):
    if len(input_list) ==0  :
        return
    else :
        i=0
        start = 0
        min_diff = len(input_list)
        while i < len(input_list) :
            if input_list[i] == x or input_array[i]==y:
                start = i
                break
            i+=1
        while i<len(input_list):
            if input_list[i] == x or input_list[i]== y :
                if input_list[i] == input_array[start] :
                    start = i
                elif input_list[i] != input_array[start] :
                    if min_diff > i-start :
                        min_diff = i-start
                    start = i
            i +=1
        return min_diff

if __name__=="__main__":
    input_array  = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
    print(find_min_distance(input_array,3,6))

    input_array = [2, 5, 3, 5, 4, 4, 2, 3]
    print(find_min_distance(input_array,3,2))

    input_array = [3, 4, 5]
    print(find_min_distance(input_array,3,5))

    input_array = [3,4,6,7,9,5,6,9,1,5,7,5,3]
    print(find_min_distance(input_array,3,5))

