"""
Find the number occuring an odd number of times
"""

def find_number(input_list):
    x=0
    for element in input_list:
        x = x ^ element
    return x

if __name__=="__main__":
    test = [1,1,2,2,3,3,3,4,5,5,4]
    print(find_number(test))