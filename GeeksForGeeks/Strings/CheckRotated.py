"""

A Program to check if strings are rotations of each other or not

Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1 using only one call to strstr
routine?

(eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)

"""

def check_rotated(string1,string2):
    if len(string1) != len(string2) :
        return False
    else :
        temp = string1*2
        if temp.count(string2)>0 :
            return True
        else :
            return False

if __name__=='__main__':
    str1 = 'ABCD'
    str2 = 'CDAB'
    print(check_rotated(str1,str2))
    str2 = 'ACBD'
    print(check_rotated(str1,str2))
