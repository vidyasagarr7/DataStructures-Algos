"""
Find the two numbers with odd occurrences in an unsorted array
Given an unsorted array that contains even number of occurrences for all numbers except two numbers.
Find the two numbers which have odd occurrences in O(n) time complexity and O(1) extra space.

Examples:

Input: {12, 23, 34, 12, 12, 23, 12, 45}
Output: 34 and 45

Input: {4, 4, 100, 5000, 4, 4, 4, 4, 100, 100}
Output: 100 and 5000

Input: {10, 20}
Output: 10 and 20


"""

def find_numbers(input_list):
    val1 = val2 = 0
    val = 0
    for i in range(len(input_list)):
        val = val ^ input_list[i]

    set_bit = val & ~(val-1)

    for i in range(len(input_list)):
        if input_list[i]&set_bit :
            val1 = val1 ^ input_list[i]
        else :
            val2 = val2 ^ input_list[i]
    return val1,val2

if __name__=='__main__':
    input_list = [12, 23, 34, 12, 12, 23, 12, 45]
    print(find_numbers(input_list))

    input_list = [4, 4, 100, 5000, 4, 4, 4, 4, 100, 100]
    print(find_numbers(input_list))