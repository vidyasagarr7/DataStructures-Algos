

"""
Print all possible words from phone digits

Before advent of QWERTY keyboards, texts and numbers were placed on the same key.
For example 2 has “ABC” if we wanted to write anything starting with ‘A’ we need to type key 2 once.
 If we wanted to type ‘B’, press key 2 twice and thrice for typing ‘C’. below is picture of such keypad.
"""

htable  = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
# code doesnt work if there is 0 or 1 in the number

def print_words(number,current,out,n) :
    if current ==n  :
        print(''.join(out))
        return

    else :
        if int(number[current]) == 0 or int(number[current]) ==1  :
            current = current+1
        for i in range(len(htable[int(number[current])])):
            out[current] = htable[int(number[current])][i]
            print_words(number,current+1,out,n)



if __name__=='__main__':
    number = '324'
    out = ['0']*len(number)
    print_words(number,0,out,len(number))