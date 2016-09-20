"""
1) find total_sum and subtract O(n)
2) sort and find which one is missing  - O(nlong(n))
3) Hashing
4) XOR -

"""

def find_missing(input_list):
    summation  = 0
    for element in input_list:
        summation += element
    n = len(input_list)
    total_sum = (n+1)*(n+2)//2
    return total_sum-summation

def _find_missing(input_list):
    input_list.sort()
    for i in range(0,len(input_list)):
        if input_list[i] != i+1:
            return i+1

def __find_missing(input_list):
    """
    Implementation to find the missing number with XOR - O(n) implementation
    :param input_list
    :return:
    """
    x=0
    for i in range(len(input_list)):
        x = x ^ i
        x = x ^ input_list[i]

    x = x^len(input_list)^(len(input_list)+1)
    return x




if __name__=="__main__":
    test = [1,2,4,5,6,7,8,9]
    print(find_missing(test))
    print(_find_missing(test))
    print(__find_missing(test))