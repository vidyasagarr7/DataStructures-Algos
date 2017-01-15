


def get_maxarea(input_list):
    if not input_list :
        return 0
    else:
        _max = 0
        i =0
        stac = []
        while i < len(input_list) :

            if len(stac) == 0 or input_list[stac[-1]] <= input_list[i] :
                stac.append(i)
                i += 1
            else  :

                top = stac.pop()
                _area = input_list[top] * (i if len(stac)==0 else i - stac[-1] -1 )
                if _max < _area :
                    _max = _area

        while len(stac) >0  :
            top = stac.pop()
            _area = input_list[top] * (i if len(stac)==0 else i-stac[-1]-1)
            if _max < _area :
                _max = _area
        return _max

if __name__=='__main__':
    test = [6, 2, 5, 4, 5, 1, 6]
    print(get_maxarea(test))