

def lcs(str1, str2):
    # base case
    if len(str1) == 0 or len(str2) == 0:
        return ""

    # same character
    if str1[0] == str2[0]:
        return str1[0]+ lcs(str1[1:], str2[1:])

    foo = lcs(str1[1:],str2)
    bar = lcs(str1,str2[1:])

    return foo if len(foo)>len(bar) else bar

if __name__ == "__main__":
    print(lcs('sagar', 'atestaar'))

    print(lcs('algorithm','gorilla'))

    # print(lcs('ACCGCGGAAGCCGGCCGAA','GTCCGTTGCTCTGTAAA'))