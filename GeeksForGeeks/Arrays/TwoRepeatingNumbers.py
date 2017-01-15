

"""
Find the two repeating elements in a given array

You are given an array of n+2 elements. All elements of the array are in range 1 to n.
And all elements occur once except two numbers which occur twice. Find the two repeating numbers.

For example, array = {4, 2, 4, 5, 2, 3, 1} and n = 5

The above array has n + 2 = 7 elements with all elements occurring once except 2 and 4 which occur twice.
So the output should be 4 2.

"""

def find_repeating(input_list,n):
    if not input_list :
        return
    else :
        _xor = input_list[0]
        for i in range(1,n+1):
            _xor = _xor ^ input_list[i] ^ i
        _xor = _xor ^ input_list[n+1]

        set_bit = _xor & ~(_xor-1)
        a,b = 0,0
        for i in range(len(input_list)):
            if input_list[i] & set_bit :
                a = a ^ input_list[i]
            else:
                b = b ^ input_list[i]
        for i in range(1,n+1):
            if i & set_bit :
                a = a ^ i
            else :
                b = b^i
        return a,b

if __name__=='__main__':
    test = [4, 2, 4, 5, 2, 3, 1]
    print(find_repeating(test,5))