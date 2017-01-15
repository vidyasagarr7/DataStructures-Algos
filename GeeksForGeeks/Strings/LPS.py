
"""
Longest Palindromic Substring | Set 1

Given a string, find the longest substring which is palindrome.
For example, if the given string is “forgeeksskeegfor”, the output should be “geeksskeeg”.

"""

def find_lps(input_string):
    if not input_string :
         return
    else :
        start = 0
        maxlength = 1

        for i in range(1,len(input_string)):

            low = i -1
            high = i

            # even length palindrome
            while low > 0 and high < len(input_string) and input_string[low] == input_string[high] :
                if high - low + 1 > maxlength :
                    maxlength = high - low + 1
                    start = low
                high += 1
                low -= 1

            low = i-1
            high = i+1
            while low > 0 and high < len(input_string) and input_string[low] == input_string[high] :
                if high - low +1 > maxlength  :
                    maxlength = high - low +1
                    start = low
                high += 1
                low -= 1
        print(input_string[start:start+maxlength])

if __name__=='__main__' :
    find_lps('forgeeksskeegforfor')












