from Karumanchi.Trees import BinaryTree
from Karumanchi.Trees.MirrorOfTree import _mirror

def check_mirrors(root1,root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.data != root2.data:
        return False
    else :
        return check_mirrors(root1.left,root2.right) and check_mirrors(root1.right,root2.left)

if __name__=="__main__":
    tree = BinaryTree()
    for i in range(1,10):
        tree.add_node(i)
    _mirror(tree.root)
    tree2 = BinaryTree()
    for i in range(1,10):
        tree2.add_node(i)
    tree1 = BinaryTree()
    for i in range(1,7):
        tree1.add_node(i)
    print(check_mirrors(tree.root,tree2.root))
    print(check_mirrors(tree.root,tree1.root))