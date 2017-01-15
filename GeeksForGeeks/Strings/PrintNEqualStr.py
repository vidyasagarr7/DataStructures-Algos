"""

Divide a string in N equal parts


Question:
Write a program to print N equal parts of a given string.


"""

def print_n_parts(input_string,n):

    if len(input_string) ==0 :
        return
    else :
        part_size = len(input_string)/n
        k=0
        for ch in input_string:
            if k>0 and k%part_size==0 :
                print('')
            print(ch,end='')
            k+=1

if __name__=='__main__':
    string = "a_simple_divide_string_quest"
    print_n_parts(string,4)