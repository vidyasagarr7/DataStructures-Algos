
"""
Tree Isomorphism Problem
Write a function to detect if two trees are isomorphic. Two trees are called isomorphic if one of them can be obtained from other by a series of flips, i.e. by swapping left and right children of a number of nodes. Any number of nodes at any level can have their children swapped. Two empty trees are isomorphic.

For example, following two trees are isomorphic with following sub-trees flipped: 2 and 3, NULL and 6, 7 and 8.

"""

class Node :
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right= None

def check_isomorphic(r1,r2) :
    if not r1 and not r1 :
        return True
    elif (not r1 and r2) or (not r2 and r1) :
        return False
    else :
        if r1.data != r2.data :
            return False
        else :
            return (check_isomorphic(r1.left,r2.left) and check_isomorphic(r1.right,r2.right) ) or \
                   (check_isomorphic(r1.left,r2.right) and check_isomorphic(r1.right,r2.left))

if __name__=='__main__':
    node = Node(1)
    node2 = None
    print(check_isomorphic(node,node2))
