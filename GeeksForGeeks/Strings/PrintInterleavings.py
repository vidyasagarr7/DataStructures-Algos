

def print_interleavings(str1,str2,out,m,n,idx):

    # basecase
    if m==0 and n==0 :
        print(''.join(out))

    # exploring first string
    if m != 0 :
        out[idx] = str1[0]
        print_interleavings(str1[1:],str2,out,m-1,n,idx+1)

    # exploring second string
    if n != 0 :
        out[idx] = str2[0]
        print_interleavings(str1,str2[1:],out,m,n-1,idx+1)



if __name__=='__main__':
    str1 = 'AB'
    str2 = 'CD'
    out = ['']*(len(str1)+len(str2))
    print_interleavings(str1,str2,out,len(str1),len(str2),0)