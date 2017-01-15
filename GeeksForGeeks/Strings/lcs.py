

"""
Printing Longest Common Subsequence

Given two sequences, print the longest subsequence present in both of them.

Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

We have discussed Longest Common Subsequence (LCS) problem in a previous post.
The function discussed there was mainly to find the length of LCS. To find length of LCS, a 2D table L[][] was
constructed. In this post, the function to construct and print LCS is discussed.
"""

def lcs(str1,str2,first,second):
    if (not str1 and str2 ) or ( not str2 and str1 ):
        return
    if first == len(str1) or second == len(str2) :
        return 0
    else:
        if first < len(str1) and second < len(str2) :
            if str1[first] == str2[second] :
                return 1+lcs(str1,str2,first+1,second+1)
            else :
                return max(lcs(str1,str2,first+1,second),lcs(str1,str2,first,second+1))



if __name__=='__main__':
    str1 = 'ABCDGH'
    str2 = 'AEDFHR'
    print(lcs(str1,str2,0,0))


    str1 = 'AGGTAB'
    str2 = 'GXTXAYB'
    print(lcs(str1,str2,0,0))





