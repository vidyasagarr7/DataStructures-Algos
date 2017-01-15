

"""
Given an array of pairs, find all symmetric pairs in it

Two pairs (a, b) and (c, d) are said to be symmetric if c is equal to b and a is equal to d.
For example (10, 20) and (20, 10) are symmetric. Given an array of pairs find all symmetric pairs in it.

It may be assumed that first elements of all pairs are distinct.

Example:

Input: arr[] = {{11, 20}, {30, 40}, {5, 10}, {40, 30}, {10, 5}}
Output: Following pairs have symmetric pairs
        (30, 40)
        (5, 10)

"""

def find_symmetric_pairs(input_dict):
    if not input_dict :
        return
    else :
        htable = {}

        for k,v in input_dict.items() :
            if v in htable and htable[v] == k :
                print((k,v))
            else :
                htable[k]=v

if __name__=='__main__':
    test = {11:20, 30:40, 5: 10, 40: 30, 10: 5}
    find_symmetric_pairs(test)