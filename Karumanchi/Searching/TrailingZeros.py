"""
Find number of trailing zeros in factorial(n)
"""

def compute_factorial(n):
    """
    Function to compute factorial of n
    :param n:
    :return:
    """
    if n==0 or n==1 :
        return 1
    else :
        return n*compute_factorial(n-1)

def num_trailing_zeros(n):
    """
    Function to find the number of trailing zeros
    :param n:
    :return:
    """
    count = 0
    i = 5 # multiples of 5
    while n//i > 0:
        count += n//i
        i *= 5
    return count

if __name__=="__main__":
    print(num_trailing_zeros(1000))

