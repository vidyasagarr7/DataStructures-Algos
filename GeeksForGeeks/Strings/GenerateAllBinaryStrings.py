import  queue

"""
Generate all binary strings from given pattern
Given a string containing of ‘0’, ‘1’ and ‘?’ wildcard characters, generate all binary strings that can be formed by replacing each wildcard character by ‘0’ or ‘1’.

Input str = "1??0?101"
Output:
        10000101
        10001101
        10100101
        10101101
        11000101
        11001101
        11100101
        11101101

"""

def generate_strings(input_string,index):
    if not input_string :
        return
    else :

        if index == len(input_string) :
            print(''.join(input_string))
            return
        else :
            if input_string[index] == '?' :
                input_string[index] = '0'
                generate_strings(input_string,index+1)


                input_string[index] = '1'
                generate_strings(input_string,index+1)
                input_string[index] = '?'
            else :
                generate_strings(input_string,index+1)







if __name__=='__main__':
    test = list('1??0?101')
    print(generate_strings(test,0))
    #generate_strings(test)