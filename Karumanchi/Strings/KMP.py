

def search(text,pattern):
    """
    O(n) algorithm for pattern matching
    :param text:
    :param pattern:
    :return:
    """

    t = len(text)
    p = len(pattern)

    lps = lpps(pattern)
    print(lps)
    j =0
    i=0
    while i < t-p+1:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == p-1 :
            print('pattern found at {}'.format(i-j))
            j = lps[j-1]
        elif i < t and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            if j == 0 :
                i += 1

    return

def lpps(pattern):
    length = 0

    lps=[0]*len(pattern)
    i=1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else :
            if length != 0 :
                length = lps[length-1]
            else :
                i += 1
    return lps

if __name__=="__main__":
    text = 'this is test test test a test text test test'
    pattern = 'test'
    search(text,pattern)




