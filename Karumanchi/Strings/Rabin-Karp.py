


def search(text, pattern):
    no_chars = 256 # number of chars
    prime = 101

    T = len(text)
    P = len(pattern)
    hash_value = 1

    for i in range(P-1):
        hash_value = (hash_value * no_chars)% prime

    hash_p = 0
    hash_t = 0
    # generate hash values for pattern and first window in text
    for i in range(P):
        hash_p = (hash_p * no_chars + ord(pattern[i])) % prime
        hash_t = (hash_t * no_chars + ord(text[i])) % prime

    for i in range(T-P+1) :
        if hash_p == hash_t :
            for j in range(P):
                if text[i+j] != pattern[j]:
                    break
            if j == P-1:
                print('pattern match found at {}'.format(i))

        if i < T-P :
            hash_t = (no_chars * (hash_t - (ord(text[i]) * hash_value)) + ord(text[i+P])) % prime
            if hash_t < 0:
                hash_t = hash_t+prime

if __name__=="__main__":
    text = 'test#test#test#'
    pattern = 'test'
    search(text,pattern)
    #_search(text,pattern)






