

def search(text,pattern):
    t = len(text)
    p = len(pattern)

    for i in range(t-p+1):

        for j in range(p):
            if text[i+j]!=pattern[j] :
                break
        if j == p-1:
            print('pattern found at {}'.format(i))

def _search(text,pattern):
    t = len(text)
    p = len(pattern)

    i = 0

    while i < t-p+1 :
        j=0
        while j < p :
            if text[i+j] != pattern[j]:
                break
            j+=1
        if j == p :
            print('pattern found {}'.format(i))
        i+=1

if __name__=="__main__":
    text = 'this is test test test a test text test test'
    pattern = 'test'
    search(text,pattern)
    _search(text,pattern)




