from GeeksForGeeks.Tree.BinaryTree import BinaryTree
"""
Diameter of a Binary Tree
The diameter of a tree (sometimes called the width) is the number of nodes on the longest path
between two leaves in the tree. The diagram below shows two trees each with diameter nine,
the leaves that form the ends of a longest path are shaded (note that there is more than one path
 in each tree of length nine, but no path longer than nine nodes).

"""

def height(node):
    if not node :
        return 0
    else :
        return 1 + max(height(node.left),height(node.right))

def diameter(node):
    if not node :
        return 0
    else :
        return max(max(diameter(node.left),diameter(node.right)),1+height(node.left)+height(node.right))



def _diamater(node) :
    if not node :
        return 0,0
    else :

        ldia, lh = _diamater(node.left)
        rdia, rh = _diamater(node.right)
        ht = max(lh,rh)+1
        dia = max(lh+rh+1,ldia,rdia)
        return dia,ht

if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)
        
    print(diameter(bt.root))

    print(_diamater(bt.root)[0])
