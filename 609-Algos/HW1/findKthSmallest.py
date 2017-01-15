"""
    Find the Kth smallest element from the union of two sorted arrays
"""


def findKthSmallest(array1,array2,k):
    if len(array1) > len(array2):
        return findKthSmallest(array2,array1,k)
    if len(array1)==0 and len(array2) > 0 :
        return array2[k-1]
    if k==1:
        return min(array1[0],array2[0])
    i = min(len(array1),k//2)
    j= min(len(array2),k//2)
    if array1[i-1] < array2[j-1]:
        return findKthSmallest(array1[i-1:],array2[:j-1],k-i)
    elif array1[i-1] > array2[j-1]:
        return findKthSmallest(array1[:i-1],array2[j-1:],k-j)

if __name__=="__main__":
    array1=[1,2,3,4,5,6,7]
    array2=[9,12,16]
    print(findKthSmallest(array1,array2,4))
