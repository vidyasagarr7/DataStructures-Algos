

"""
An in-place algorithm for String Transformation

Given a string, move all even positioned elements to end of string.
While moving elements, keep the relative order of all even positioned and
odd positioned elements same. For example, if the given string is “a1b2c3d4e5f6g7h8i9j1k2l3m4”,
convert it to “abcdefghijklm1234567891234” in-place and in O(n) time complexity.

"""
def reverse(input_string,start,end):
    if not input_string :
        return
    else :
        low = start
        high = end
        while low < high :
            input_string[low],input_string[high] = input_string[high],input_string[low]
            low += 1
            high -= 1
        return input_string

def transform(input_string):
    if not input_string  :
        return
    else:



if __name__=='__main__':
    testing = 'sagar'
    print(''.join(reverse(list(testing),0,len(testing)-1)))
    print(testing)