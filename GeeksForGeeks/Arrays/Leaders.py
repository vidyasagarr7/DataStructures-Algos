

"""
Leaders in an array
Write a program to print all the LEADERS in the array. An element is leader if it is greater than all the
elements to its right side. And the rightmost element is always a leader.

For example int the array {16, 17, 4, 3, 5, 2}, leaders are 17, 5 and 2.

Let the input array be arr[] and size of the array be size.

"""

def find_leaders(input_list):
    if not input_list :
        return
    else :
        _max = input_list[len(input_list)-1]
        leaders = [_max]
        for i in range(len(input_list)-2,-1,-1):
            if _max < input_list[i] :
                _max = input_list[i]
                leaders.append(_max)
        return leaders

if __name__=='__main__':
    test = [16, 17, 4, 3, 5, 2]
    res = find_leaders(test)
    res.reverse()
    print(res)


