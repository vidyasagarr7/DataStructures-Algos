

"""
Segregate Even and Odd numbers
Given an array A[], write a function that segregates even and odd numbers.
The functions should put all even numbers first, and then odd numbers.

Example

Input  = {12, 34, 45, 9, 8, 90, 3}
Output = {12, 34, 8, 90, 45, 9, 3}

"""

def segregate_oe(input_list):
    if not input_list :
        return
    else  :
        left = 0
        right = len(input_list)-1

        while left <= right :
            while input_list[left]%2 == 0 :
                left += 1
            while input_list[right]%2 == 1 :
                right -= 1
            #print('left : {} and right :  {}'.format(left,right))
            if left < right :
                input_list[left],input_list[right] = input_list[right],input_list[left]
                left += 1
                right -= 1
        return input_list
if __name__=='__main__':
    test = [12, 34, 45, 9, 8, 90, 3]
    print(segregate_oe(test))