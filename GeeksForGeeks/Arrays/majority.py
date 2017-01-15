
"""
Majority Element

Majority Element: A majority element in an array A[] of size n is an element that appears more than n/2 times
(and hence there is at most one such element).

Write a function which takes an array and emits the majority element (if it exists), otherwise prints NONE as follows:

       I/P : 3 3 4 2 4 4 2 4 4
       O/P : 4

       I/P : 3 3 4 2 4 4 2 4
       O/P : NONE


"""

def find_majority(input_list):

    majority = input_list[0]
    count = 1

    for i in range(1,len(input_list)):
        if input_list[i] == majority :
            count += 1
        else :
            count -= 1
        if count ==0 :
            majority = input_list[i]
            count = 1

    if count > 0 :
        count = 0
        for _ in input_list :
            if _ == majority :
                count +=1
        if count > len(input_list)/2 :
            return 'majority element {}'.format(majority)
        else :
            return 'there is not majority element'

if __name__=='__main__':
    input_list = [3,3,4,2,4,4,2,4,4]
    print(find_majority(input_list))