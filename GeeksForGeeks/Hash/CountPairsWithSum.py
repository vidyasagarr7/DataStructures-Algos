

"""
Count pairs with given sum

Given an array of integers, and a number ‘sum’,
find the number of pairs of integers in the array whose sum is equal to ‘sum’.
"""

def count_pairs(input_list,s):
    if not input_list :
        return
    else :
        htable = {}
        for i in range(len(input_list)):
            if input_list[i] not in htable :
                htable[input_list[i]] = 1
            else :
                htable[input_list[i]] += 1
        count = 0
        for i in range(len(input_list)):
            if s - input_list[i] in htable :
                count += htable[s-input_list[i]]
            if s-input_list[i] == input_list[i]  :
                count -= 1
        print(count//2)
        return

if __name__=='__main__':
    count_pairs([1, 1, 1, 1],2)
    count_pairs([1, 5, 7, -1, 5],6)