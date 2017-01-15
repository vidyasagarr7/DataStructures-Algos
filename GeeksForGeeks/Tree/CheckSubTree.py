from GeeksForGeeks.Tree.BinaryTree import BinaryTree
from GeeksForGeeks.Tree.CheckIndentical import check_identical

def check_subtree(node1,node2):
    if not node2 and not node1 :
        return True
    elif not node1 and node2  :
        return False
    elif not node2 and node1  :
        return False
    else :

        if node1.data != node2.data :
            return check_subtree(node1,node2.left) and check_subtree(node1,node2.right)
        else :
            return check_identical(node1,node2)

if __name__=='__main__':
    bt = BinaryTree()
    
