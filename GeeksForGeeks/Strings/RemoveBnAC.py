

"""
Remove “b” and “ac” from a given string

Given a string, eliminate all “b” and “ac” in the string, you have to replace them in-place,
and you are only allowed to iterate over the string once. (Source Google Interview Question)

Examples:

acbac   ==>  ""
aaac    ==>  aa
ababac  ==>   aa
bbbbd   ==>   d
"""

def remove_abc(input_list):
    if not input_list :
        return

    else :
        i = 0
        j = 0
        while i < len(input_list) :
            if i < len(input_list)-1 and input_list[i] =='a' and input_list[i+1] == 'c' :
                i += 2
            elif input_list[i] == 'b' :
                i += 1
            elif input_list[i] =='c' and input_list[j] =='a' :
                j -= 1
                i +=1
            else :
                input_list[j] = input_list[i]
                i +=1
                j+= 1
        return ''.join(input_list[:j])
ONE = 1
TWO = 2
def remove_bac(input_list):
    if not input_list :
        return
    else :
        state = ONE
        j = 0
        for i in range(len(input_list)) :
            if state ==ONE and input_list[i] != 'a' and input_list[i] != 'b' :
                input_list[j] = input_list[i]
                j += 1

            if state == TWO and input_list[i] != 'c' :
                input_list[j] = 'a'
                j += 1

                if input_list[i] != 'a' and input_list[i] != 'b' :
                    input_list[j] = input_list[i]
                    j +=1
            if (j > 1 and input_list[j - 2] == 'a' and input_list[j - 1] == 'c'):
                j -= 2
            state = TWO if input_list[i] == 'a' else ONE
        if state == TWO :
            input_list[j] = 'a'
            j +=1
        return ''.join(input_list[:j])


if __name__=='__main__':
    test  = 'acbac'
    print(remove_bac(list(test)))

    print(remove_abc(list(test)))

    test = 'aaac'
    print(remove_bac(list(test)))

    print(remove_abc(list(test)))

    test  = 'ababac'
    print(remove_bac(list(test)))

    print(remove_abc(list(test)))

    test = 'bbbbd'
    print(remove_bac(list(test)))

    print(remove_abc(list(test)))

    test = 'react'
    print(remove_bac(list(test)))
    print(remove_abc(list(test)))

    test = 'aacacc'
    print(remove_abc(list(test)))
    print(remove_bac(list(test)))