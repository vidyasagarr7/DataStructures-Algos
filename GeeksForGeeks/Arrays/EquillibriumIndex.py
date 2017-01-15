

"""

Equilibrium index of an array

Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to
the sum of elements at higher indexes. For example, in an arrya A:

A[0] = -7, A[1] = 1, A[2] = 5, A[3] = 2, A[4] = -4, A[5] = 3, A[6]=0

3 is an equilibrium index, because:
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

6 is also an equilibrium index, because sum of zero elements is zero, i.e., A[0] + A[1] + A[2] + A[3] + A[4] + A[5]=0

7 is not an equilibrium index, because it is not a valid index of array A.

Write a function int equilibrium(int[] arr, int n); that given a sequence arr[] of size n,
returns an equilibrium index (if any) or -1 if no equilibrium indexes exist.

"""

def equillibrium_index(input_list):
    if not input_list :
        return
    else :

        _sum = 0
        for num in input_list :
            _sum += num

        left_sum = 0
        for i in range(len(input_list)) :
            _sum = _sum - input_list[i]
            if i == 0  and _sum==left_sum:
                return 0
            elif i != 0 :
                left_sum = left_sum + input_list[i-1]
                if _sum == left_sum :
                    return i

if __name__=='__main__':
    test = [-7,1,-5,5,2,-4,3,0,5,5]
    print(equillibrium_index(test))









