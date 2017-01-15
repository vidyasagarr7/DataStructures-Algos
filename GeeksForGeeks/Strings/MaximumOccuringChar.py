
def maximum_occuring_char(string):
    dictionary = {}
    max_val = 0
    max_key = ''
    for ch in string :
        if ch not in dictionary :
            dictionary[ch] = 1
        else :
            dictionary[ch] +=1
    print(dictionary)
    for k,v in dictionary.items() :
        print('{} and val {}'.format(k,v))
        if v > max_val :
            print('max_val {} and max_key {}'.format(v,k))
            max_val = v
            max_key = k
    return max_key

if __name__=='__main__':
    input_str = 'sagar'
    print(maximum_occuring_char(input_str))