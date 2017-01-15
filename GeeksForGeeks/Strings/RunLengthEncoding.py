"""
Run Length Encoding

Given an input string, write a function that returns the Run Length Encoded string for the input string.

For example, if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6”.


"""

def run_length_encoded(string):
    out_list = []
    count = 0
    prev = string[0]
    out_list.append(prev)
    for i in range(1,len(string)) :
        if string[i] == prev :
            count += 1
        else  :
            out_list.append(str(count+1))
            count = 0
            prev = string[i]
            out_list.append(string[i])
    out_list.append(str(count+1))

    return ''.join(out_list)

if __name__ =='__main__':
    string = 'wwwwaaadexxxxxx'
    print(run_length_encoded(string))
    string = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
    print(run_length_encoded(string))

