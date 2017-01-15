
def count_words(string):
    _state = 0

    list_str = list(string)
    wc = 0

    for i in range(len(list_str)):

        if list_str[i] == ' ' or list_str[i] == '   ' or list_str[i]=='\n':
            _state = 0

        elif _state == 0 :
            _state = 1
            wc += 1
    return wc

if __name__=='__main__':
    string = 'One two          three\n  four\nfive  '
    print(count_words(string))