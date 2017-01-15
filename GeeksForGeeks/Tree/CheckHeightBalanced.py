from GeeksForGeeks.Tree.BinaryTree import BinaryTree

"""
How to determine if a binary tree is height-balanced?
A tree where no leaf is much farther away from the root than any other leaf.
 Different balancing schemes allow different definitions of “much farther” and different
  amounts of work to keep them balanced.

"""

def height(node):
    if not node :
        return 0
    else :
        return max(height(node.left),height(node.right))+1

def check_ht_bal(node):
    if not node :
        return True
    else :
        lh = height(node.left)
        rh = height(node.right)

        if abs(lh-rh)<=1 and check_ht_bal(node.left) and check_ht_bal(node.right) :
            return True
        return False
if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,8):
        bt.add_node(i)
    print(check_ht_bal(bt.root))

    bt2 = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)

    print(check_ht_bal(bt2.root))