
def binary_search(input_list,key):

    return _binary_search(input_list,0,len(input_list)-1,key)


def _binary_search(input_list,start,end,key):
    """
    Recursive Implementation of searching for an element in a sorted list - O(ln(n)) time
    :param input_list:
    :param start:
    :param end:
    :param key:
    :return:
    """
    if not input_list:
        return False
    if start == end:
        if input_list[start] == key:
            return True
    elif start < end :
        mid = start + (end-start)//2
        if input_list[mid] == key:
            return True
        elif input_list[mid] > key:
            return _binary_search(input_list,start,mid-1,key)
        else :
            return _binary_search(input_list,mid+1,end,key)
    return False

def binary_search_nr(input_list,key):
    if not input_list:
        return False
    else:
        low =0
        high = len(input_list)-1
        while low <= high:
            mid = low + (high-low)//2
            if input_list[mid] > key:
                high=mid-1
            elif input_list[mid] < key :
                low=mid+1
            else:
                return True
        return False

if __name__=="__main__":
    
    test=[1,2,3,4,5,6,7,8,9]

    print(binary_search(test,5))
    print(binary_search(test,11))

    print(binary_search_nr(test,5))
    print(binary_search_nr(test,11))
