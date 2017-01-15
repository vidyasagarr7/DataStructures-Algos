"""

Return maximum occurring character in the input string

Write an efficient C function to return maximum occurring character in the input string e.g.,
if input string is “test” then function should return ‘t’.

"""


# number of ASCII characters
NO_CHARS = 256

def max_char(input_str):
    # init
    count_arr = [0] * NO_CHARS

    for ch in input_str :
        count_arr[ord(ch)] += 1

    _maxc = -1

    _maxch = -1
    # iterate through count_arr instead of input_str - this can have many items.
    for i in range(len(count_arr)) :
        # updating max everytime
        if count_arr[i] > _maxc :
            _maxc = count_arr[i]
            _maxch = i
    return chr(_maxch)

if __name__=='__main__':
    _input = 'cbbbbcccccccc'
    print(max_char(_input))
