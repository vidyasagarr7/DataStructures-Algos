
"""
Rearrange positive and negative numbers in O(n) time and O(1) extra space

An array contains both positive and negative numbers in random order.
Rearrange the array elements so that positive and negative numbers are placed alternatively.
Number of positive and negative numbers need not be equal. If there are more positive numbers they
appear at the end of the array. If there are more negative numbers, they too appear in the end of the array.
"""

def segregate_positive_and_negatives(input_list):

    left = 0
    for i in range(len(input_list)):
        if input_list[i] <= 0 :
            input_list[i],input_list[left] = input_list[left],input_list[i]
            left +=1
    return left



## Revisit this code. This is wrong 
def rearrange(input_list):
    if not input_list :
        return
    else :
        start = segregate_positive_and_negatives(input_list)
        current = start +1
        left = 0
        while current < len(input_list) and left < current and input_list[left] < 0 :
            input_list[left],input_list[current] = input_list[current],input_list[left]
            current += 1
            left += 2

        return input_list


if __name__=='__main__':
    test = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    #start = segregate_positive_and_negatives(test)
    #print(start)
    print(rearrange(input_list=test))
