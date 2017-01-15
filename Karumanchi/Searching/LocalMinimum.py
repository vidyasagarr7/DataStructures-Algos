
"""
Find the local minimum in the array : design an O(log(n)) algorithm to find that element - arr[i-1] < arr[i] < arr[i+1]

"""

def find_local_min(input_list):
    """
    O(logn) algorithm to find the local minimum
    :param input_list:
    :return:
    """
    return _find_local_min(input_list,0,len(input_list))

def _find_local_min(input_list,start,end):

    if start < end :
        mid = (start+end)//2
        if input_list[mid-1] > input_list[mid] and input_list[mid] < input_list[mid+1]:
            return input_list[mid]
        elif input_list[mid-1] < input_list[mid]:
            return _find_local_min(input_list,start,mid-1)
        else:
            return _find_local_min(input_list,mid+1,end)

if __name__=="__main__":
    test = [8,5,3,5,3,7,9,2,1,6,8,4,2,3,4,5,6,7]
    print(find_local_min(test))

