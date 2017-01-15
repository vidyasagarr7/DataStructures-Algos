
"""
Given a string, find its first non-repeating character

Given a string, find the first non-repeating character in it.
For example, if the input string is “GeeksforGeeks”, then output should be ‘f’ and if input string is “GeeksQuiz”,
then output should be ‘G’.

"""

def find_first_nr(input_string):
    if len(input_string)==0 :
        return
    else :
        NO_CHARS = 256
        hash_table = [0]*NO_CHARS
        for ch in input_string:
            hash_table[ord(ch)] += 1

        for ch in input_string :
            if hash_table[ord(ch)]  ==1 :
                return ch


if __name__=='__main__':
    input_string = 'geeksforgeeks'
    print(find_first_nr(input_string))