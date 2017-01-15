import math


def solution(x) :
    if not x :
        return
    else :
        temp_arr = []

        input_list = list(str(x))


        if len(input_list)==2 :
            return math.ceil(int(input_list[0])+int(input_list[1])//2)
        _max = 0
        for i in range(1,len(input_list)-1):

            _sum = math.ceil((int(input_list[i])+int(input_list[i-1]))/2)
            if i == len(input_list)-1 :
                value = int(''.join(input_list[:i-1]) + str(_sum))
            else :
                value = int(''.join(input_list[:i-1])+str(_sum)+''.join(input_list[i+1:]))\

            if value > _max :
                _max = value

        return _max

if __name__=='__main__':
    test = 623315
    print(solution(test))

    test = 12
    print(solution(test))

    test = 128
    print(solution(test))

    test = 1234
    print(solution(test))

    test = 4756
    print(solution(test))