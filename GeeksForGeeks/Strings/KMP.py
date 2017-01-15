

def compute_lps(pattern):
    if not pattern :
        return
    else :
        index = 0
        i = 1
        lps = [0]*len(pattern)
        while i  <  len(pattern) :
            if pattern[i] == pattern[index] :
                index += 1
                lps[i] = index
                i += 1
            else :
                if index != 0  :
                    index = lps[index-1]
                else :
                    lps[i] = 0
                    i += 1
        return lps

def kmp(string,pattern):
    if not string :
        return
    else:
        lps = compute_lps(pattern)
        i = 0
        j = 0
        while i < len(string) :
            if string[i] == pattern[j]:
                i += 1
                j += 1

            if j == len(pattern) :
                print('pattern found at index {}'.format(i-j))
                j = lps[j-1]
            elif i < len(string) and pattern[j] != string[i] :
                if j != 0 :
                    j = lps[j-1]
                else :
                    i += 1


if __name__=='__main__':
    test = 'ABABDABACDABABCABAB'
    pattern = 'ABABCABAB'

    kmp(test,pattern)