

"""
Printing Longest Common Subsequence
Given two sequences, print the longest subsequence present in both of them.

Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
"""
def print_lcs(str1,str2):
    if not str1 or not str2 :
        return
    else :
        m = len(str1)
        n = len(str2)
        lps = [[0 for x in range(m+1)] for x in range(n+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i==0 or j ==0  :
                    lps[i][j] = 0
                elif str1[i-1] == str2[j-1] :
                    lps[i][j] = lps[i-1][j-1] + 1
                else :
                    lps[i][j] = max(lps[i-1][j],lps[i][j-1])
        index = lps[m][n]
        i = m
        j = n
        out = ['0']*index
        while i> 0 and j > 0 :
            if str1[i-1]==str2[j-1] :
                index -= 1
                out[index] = str2[j-1]
                i -= 1
                j -=1
            elif lps[i-1][j] > lps[i][j-1] :
                i -= 1
            else :
                j -=1
        return ''.join(out)



if __name__=='__main__':
    str1 = 'ABCDGH'
    str2 = 'AEDFHR'
    print(print_lcs(list(str1),list(str2)))