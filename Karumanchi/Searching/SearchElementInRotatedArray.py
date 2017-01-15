

# Revisit this problem
def search_element(input_list,k):
    left = 0
    right = len(input_list)-1

    while left <= right:

        mid = (left+right)//2
        if input_list[mid]==k:
            return mid

        # first half
        if input_list[mid]>=input_list[right] and k<input_list[mid]:
            right = mid-1
        if input_list[mid]>=input_list[right] and k>input_list[mid]:
            left = mid+1
        # second half
        if input_list[mid]<=input_list[right] and k>input_list[mid]:
            left = mid+1
        if input_list[mid]<=input_list[right] and k<input_list[mid]:
            right=mid+1

    return -1

if __name__=="__main__":
    test = [5,6,7,8,9,1,2,3,4]
    print(search_element(test,3))