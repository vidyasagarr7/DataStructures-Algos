
"""
Find the minimum in sorted and rotated array
Logic : min element is the only element with previous element greater than that element - use binary search
"""

# debug this.
def find_min(input_list):
    """

    :param input_list:
    :return:
    """
    return _find_min(input_list,0,len(input_list))

def _find_min(input_list,left,right):
    """
    Recursive implementation
    :param input_list:
    :param left:
    :param right:
    :return:
    """
    while left <= right:
        if left == right:
            return input_list[left],left
        mid = (left+right)//2
        if mid>left and input_list[mid-1] > input_list[mid]:
            return input_list[mid],mid
        if mid<right and input_list[mid] > input_list[mid+1]:
            return input_list[mid+1],mid+1
        if input_list[mid]<input_list[right]:
            right = mid-1
        else:
            left=mid+1

def __find_min(input_list,low,high):
    """
    Recursive implementation
    :param input_list:
    :param low:
    :param high:
    :return:
    """

    if low==high:
        return input_list[low],low
    mid = low + (high-low)//2
    if mid>low and input_list[mid]<input_list[mid-1]:
        return input_list[mid],mid
    if mid < high and input_list[mid+1]<input_list[mid]:
        return input_list[mid+1],mid+1
    if input_list[mid]<input_list[high]:
        high = mid-1
    if input_list[mid]>input_list[high]:
        low = mid+1
    __find_min(input_list,low,high)


if __name__=="__main__":
    test = [15,16,17,18,19,1,2,3]
    print(find_min(test))
    print(__find_min(test,0,len(test)))