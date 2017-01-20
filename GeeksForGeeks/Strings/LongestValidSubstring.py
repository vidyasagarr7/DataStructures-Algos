
"""
Length of the longest valid substring
Given a string consisting of opening and closing parenthesis, find length of the longest valid parenthesis substring.

Examples:

Input : ((()
Output : 2
Explanation : ()

Input: )()())
Output : 4
Explanation: ()()

Input:  ()(()))))
Output: 6
Explanation:  ()(()))

"""

def longest_substring(input_string):
    if not input_string :
        return 0
    else :
        stac = [-1]
        out = 0
        for i in range(len(input_string)):
            if input_string[i] == '(' :
                stac.append(i)
            else :
                stac.pop()
                if len(stac) > 0 :
                    out = max(out,i-stac[-1])
                else :
                    stac.append(i)
        return out

if __name__=='__main__':

    test = '((()'
    print(longest_substring(list(test)))

    test = list('())))))))((((((((()))))')
    print(longest_substring(test))

    test = list(')()))))))())')
    print(longest_substring(test))
