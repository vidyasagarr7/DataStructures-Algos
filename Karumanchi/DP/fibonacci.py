

def fib(n):
    """
    O(2^n) algorithm
    :param n:
    :return:
    """
    if n==0 or n==1:
        return 1
    else :
        return fib(n-1)+fib(n-2)

def _fib(n):
    """
    O(n)/O(n) algorithm
    :param n:
    :return:
    """
    fib_list = [1,1]
    for i in range(2,n+1):
        fib_list.append(fib_list[i-1]+fib_list[i-2])
    return fib_list[n]

if __name__ == '__main__':
    print(fib(5))
    print(_fib(5))
