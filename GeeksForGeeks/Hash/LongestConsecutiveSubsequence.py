

"""
Longest Consecutive Subsequence

Given an array of integers, find the length of the longest sub-sequence such that elements in the subsequence
 are consecutive integers, the consecutive numbers can be in any order.

Examples

Input: arr[] = {1, 9, 3, 10, 4, 20, 2};
Output: 4
The subsequence 1, 3, 4, 2 is the longest subsequence
of consecutive elements

Input: arr[] = {36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42}
Output: 5
The subsequence 36, 35, 33, 34, 32 is the longest subsequence
of consecutive elements.

"""
# for contiguous elements without repetition
def lcs(input_list):
    if not input_list :
        return
    else :

        _max_len = 0
        for i in range(len(input_list)) :
            _min = input_list[i]
            _max = input_list[i]
            for j in range(i+1,len(input_list)):
                _min = min(_min,input_list[j])
                _max = max(_max,input_list[j])

                if _max - _min == j-i :
                    _max_len = max(_max_len,_max-_min+1)
        return _max_len

def lcsu(input_list):
    """
    O(n*logn) solution.
    :param input_list:
    :return:
    """
    if not input_list :
        return
    else :
        return lcs(sorted(input_list))

def create_hash(input_list):
    if not input_list :
        return
    else  :
        htable = {}
        for num in input_list :
            if num not in htable :
                htable[num]  = 1
            else :
                htable[num] +=1
        return htable

def _lcsu(input_list):
    """
    O(n) time algorithm
    :param input_list:
    :return:
    """

    if not input_list :
        return
    else :
        htable = create_hash(input_list)
        max_len = 0
        for num in htable :
            count = 0
            if num-1 not in htable :
                current = num
                while current in htable :
                    current = current +1
                    count += 1
                max_len = max(count,max_len)
        return max_len

if __name__=='__main__':
    test = [1, 9, 3, 10, 4, 20, 2]
    #print(lcs(test))

    test2 = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
    #print(lcs(test2))

    print(lcsu(test))
    print(lcsu(test2))

    print(_lcsu(test))
    print(_lcsu(test2))