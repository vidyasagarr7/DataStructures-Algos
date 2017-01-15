

"""
Run Length Encoding

Given an input string, write a function that returns the Run Length Encoded string for the input string.

For example, if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6”.

"""

def len_encoding(input_list):
    if not input_list :
        return
    else :
        if len(input_list) == 1 :
            return input_list.append(1)

        ret_idx = 0
        cur_idx = 1
        count = 1
        out_list = [0]*2*len(input_list)
        while cur_idx < len(input_list) :
            if input_list[cur_idx] == input_list[cur_idx-1] :
                count += 1
            else :
                out_list[ret_idx] = input_list[cur_idx-1]
                ret_idx += 1
                out_list[ret_idx] = count
                ret_idx += 1
                count = 1
            cur_idx += 1
        out_list[ret_idx] = input_list[cur_idx-1]
        ret_idx += 1
        out_list[ret_idx] = count
        return ''.join(map(str,out_list[:ret_idx+1]))

if __name__=='__main__':
    string = 'wwwwaaadexxxxxx'
    print(len_encoding(list(string)))

    string = 'abcdefghtisk'
    print(len_encoding(list(string)))