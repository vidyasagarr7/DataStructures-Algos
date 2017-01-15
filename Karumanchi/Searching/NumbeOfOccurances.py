
from Karumanchi.Searching import BinarySearch

def find_occurances(input_list,k):
    """
    Linear time - O(n)
    :param input_list:
    :param k:
    :return:
    """
    count =0
    for i in range(len(input_list)):
        if input_list[i]==k:
            count +=1
    return count

def _find_occurances(input_list,k):
    """
    Binary Search tweaked version - O(logn)
    :param input_list:
    :param k:
    :return:
    """
    count = 0
    left = 0
    right = len(input_list)-1
    mid = (left+right)//2

def first_occurance(input_list,low,high,k):
    if low <= high :
        mid = (low + high)//2
        if (mid==low and input_list[mid]==k) or (input_list[mid]==k and input_list[mid-1]<k):
            return mid
        elif k > input_list[mid]:
            first_occurance(input_list,mid+1,high,k)
        else :
            first_occurance(input_list,low,mid-1,k)
    return -1

if __name__=="__main__":
    test =[1,2,4,5,5,5,5,5,5,5,6]
    print(find_occurances(test,5))

    #print(_find_occurances(test,5))

    print(first_occurance(test,0,len(test)-1,5))
