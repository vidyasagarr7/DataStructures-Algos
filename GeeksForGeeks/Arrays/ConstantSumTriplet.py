"""
Find a triplet that sum to a given value

Given an array and a value, find if there is a triplet in array whose sum is equal to the given value.
If there is such a triplet present in array, then print the triplet and return true. Else return false.
For example, if the given array is {12, 3, 4, 1, 6, 9} and given sum is 24, then there is a triplet (12, 3 and 9)
present in array whose sum is 24.



Solution : - Brute force - use 3 nested loops - O(n^3)
           - Sort and iterating through the list, use two pointers for start and end - O(n^2)
"""

def find_triplet(input_list,value):

    input_list.sort()

    for i in range(len(input_list)):

        left = i+1
        right = len(input_list)-1
        while left < right :
            if input_list[i] + input_list[left] + input_list[right] > value :
                right = right -1
            elif input_list[i] + input_list[left] + input_list[right] < value :
                left = left + 1
            else :
                return input_list[i],input_list[left],input_list[right]
    return 'sum not found'





if __name__=="__main__":
    input_list = [12, 3, 4, 1, 6, 9]
    value  = 24
    print(find_triplet(input_list,value))