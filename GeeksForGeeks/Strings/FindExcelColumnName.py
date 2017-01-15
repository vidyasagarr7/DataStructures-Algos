

"""
Find Excel column name from a given column number

MS Excel columns has a pattern like A, B, C, … ,Z, AA, AB, AC,…. ,AZ, BA, BB, … ZZ, AAA, AAB ….. etc.
In other words, column 1 is named as “A”, column 2 as “B”, column 27 as “AA”.

Given a column number, find its corresponding Excel column name. Following are more examples.

Input          Output
 26             Z
 51             AY
 52             AZ
 80             CB
 676            YZ
 702            ZZ
 705            AAC

"""


def find_cname(k):
    if not k :
        return
    else :

        res = ['0']*50
        if k <= 26 :
            return chr(ord('a')+k-1)
        i = 0
        while k > 0 :
            rem = k%26
            if rem == 0 :
                res[i]  = 'z'
                k = k//26 -1
            else :
                res[i] = chr(ord('a')+rem-1)
                k = k//26
            i += 1
        result = res[:i]
        result.reverse()
        return ''.join(result)
    
if __name__=='__main__':
    test = [25,26,51,52,80,676,702,705]
    for num in test :
        print(find_cname(num))