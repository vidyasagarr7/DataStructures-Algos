
from Karumanchi.Trees import BinaryTree

def _check_identical(root1,root2):
    if not root1 and not root2:
        return True
    else:
        if not root1 and root2 or not root2 and root1:
            return False
        else :
            if root1.get_data()!= root2.get_data():
                return False
            else:
                return _check_identical(root1.get_left(),root2.get_left()) and \
                       _check_identical(root1.get_right(),root2.get_right())


if __name__=="__main__":

    tree1 = BinaryTree()
    for i in range(1,10):
        tree1.add_node(i)

    tree2 = BinaryTree()
    for j in range(1,10):
        tree2.add_node(j)

    tree = BinaryTree()
    for i in range(1,15):
        tree.add_node(i)

    print(_check_identical(tree.root,tree1.root))
    print(_check_identical(tree.root,tree2.root))

    print(_check_identical(tree1.root,tree2.root))