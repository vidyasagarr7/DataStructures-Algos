"""
Length of the largest subarray with contiguous elements | Set 1

Given an array of distinct integers, find length of the longest subarray which contains numbers that can be
arranged in a continuous sequence.

Examples:

Input:  arr[] = {10, 12, 11};
Output: Length of the longest contiguous subarray is 3

Input:  arr[] = {14, 12, 11, 20};
Output: Length of the longest contiguous subarray is 2

Input:  arr[] = {1, 56, 58, 57, 90, 92, 94, 93, 91, 45};
Output: Length of the longest contiguous subarray is 5


"""

def find_largest(arr):
    if not arr  :
        return None
    else :

        max_len = 0
        for i in range(len(arr)) :
            # min and max values in a particular subset
            _min = arr[i]
            _max = arr[i]


            for j in range(i+1,len(arr)):
                # updating max and min values
                _min = min(_min,arr[j])
                _max = max(_max,arr[j])

                # updating max length of the subarray - works only if the elements in the input are distinct.
                if _max-_min == j-i  and j-i > max_len:
                    max_len = j-i +1
        return max_len



# this allows duplicates of the elements aswell
def _find_largest(arr):
    if not arr  :
        return None
    else :

        max_len = 0
        #htable = {}
        for i in range(len(arr)) :
            # min and max values in a particular subset
            _min = arr[i]
            _max = arr[i]
            htable  = {}
            htable[arr[i]] = 1
            for j in range(i+1,len(arr)):
                # updating max and min values
                if arr[j] in htable:
                    break

                htable[arr[j]] = 1
                _min = min(_min,arr[j])
                _max = max(_max,arr[j])

                # check this once again. 
                # updating max length of the subarray

                if _max-_min == j-i:
                    print(' {} {} : {}'.format(j,i,j-i))
                    max_len = max(max_len,_max-_min+1)
        return max_len



if __name__ =='__main__':
    arr1 = [10, 12, 11]
    print(find_largest(arr1))

    arr2 = [14, 12, 11, 20]
    print(find_largest(arr2))

    arr3 = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
    print(find_largest(arr3))



    # revisit this.
    arr1 = [10, 12,12,11,10, 11,10,11,11,11,11,11,11,11,11]
    print(_find_largest(arr1))

    arr2 = [14, 12,11,12,11,12, 11, 20]
    print(_find_largest(arr2))

    arr3 = [1, 56, 58, 57, 90, 92, 92,91,94, 93, 91, 45]
    print(_find_largest(arr3))
