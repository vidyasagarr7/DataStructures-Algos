

def toh(n,fromlist,tolist,auxlist):
    if n==1 :
        print('mode disk 1 from {} and to  {}'.format(fromlist,tolist))
        return
    toh(n-1,fromlist,auxlist,tolist)
    print('moving disk {} from  {} to  {}'.format(n,fromlist,tolist))
    toh(n-1,auxlist,tolist,fromlist)

if __name__=='__main__':
    toh(4,'a','b','b')
