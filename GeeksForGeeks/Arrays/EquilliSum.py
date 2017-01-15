

"""
def find equillibrium
"""

def find_equillibruim(input_list):
    if not input_list :
        return
    else :
        _sum = 0
        for i in range(len(input_list)):
            _sum += input_list[i]

        left_sum = 0
        for i in range(len(input_list)):
            _sum = _sum - input_list[i]
            if left_sum == _sum :
                return i
            left_sum += input_list[i]

if __name__=='__main__':
    test = [-1,3,-4,5,1,-6,2,1]
    print(find_equillibruim(test))