
def add_two_binary_arrays(arr1,arr2):
    """
    Add two n-bit binary arrays stored in two lists into a (n+1) bit binary array
    :param arr1: n-bit binary array 1
    :param arr2: n-bit binary array 2
    :return:
    """
    n = len(arr1)
    res = [0]*(n+1)
    for i in range(n):
        summ = arr1[n-i-1]+arr2[n-i-1]+res[n-i]
        res[n-i] = summ % 2
        res[n-i-1] = summ//2
    return res

if __name__=="__main__":
    test1 = [1,0,1,0,0,0,1,1,0]
    test2 = [0,1,0,1,1,1,1,1,1]
    print(add_two_binary_arrays(test1,test2))
