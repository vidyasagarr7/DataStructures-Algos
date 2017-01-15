from Karumanchi.Searching import FirstOccurance
"""
Find the last occurance of the element in a sorted array. - O(logn) solution.

"""


def last_occurance(input_list,element):

    return find_last_occurance(input_list,element,0,len(input_list))

def find_last_occurance(input_list,element,low,high):
    if low<=high:
        mid = low + (high-low)//2
        if (mid==len(input_list)-1 or input_list[mid+1]>element) and input_list[mid]==element:
            return mid
        elif input_list[mid]<=element:
            return find_last_occurance(input_list,element,mid+1,high)
        else :
            return find_last_occurance(input_list,element,low,mid-1)

if __name__=="__main__":
    test = [1,2,3,3,3,3,3,3,3,3,3,3,4,5,6,7,7,7,8,8]
    print(last_occurance(test,3))
    print('number of occurances : {}'.format(str(last_occurance(test,3)-FirstOccurance.first_occurance(test,3)+1)))

