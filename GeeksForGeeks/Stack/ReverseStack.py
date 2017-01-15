"""
Reverse a stack using recursion

You are not allowed to use loop constructs like while, for..etc, and you can only use the following ADT functions on
Stack S:

isEmpty(S)
push(S)
pop(S)

"""


def insert_at_bottom(stac,item):
    if not len(stac) > 0 :
        stac.append(item)
    else :
        node = stac.pop()
        insert_at_bottom(stac,item)
        stac.append(node)

def reverse(st):
    if not len(st) :
        return
    else :
        node = st.pop()
        reverse(st)
        insert_at_bottom(st,node)
        #st.insert(0,node)


if __name__ =='__main__':
    stac = [1,2,3,4,5]

    reverse(stac)
    print(stac)