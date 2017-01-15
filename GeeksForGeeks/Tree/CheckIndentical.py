from GeeksForGeeks.Tree.BinaryTree import BinaryTree
"""
Write Code to Determine if Two Trees are Identical
Two trees are identical when they have same data and arrangement of data is also same.

To identify if two trees are identical, we need to traverse both trees simultaneously, and
while traversing we need to compare data and children of the trees.
"""


def check_identical(node1,node2):
    if not node1 and not node2 :
        return True
    if not node1 and node2 or not node2 and node1 :
        return False
    if node1.data != node2.data :
        return False
    else :
        return (node1.data == node2.data) and check_identical(node1.left,node2.left) and check_identical(node1.right,node2.right)

if __name__=='__main__':
    tree1 = BinaryTree()
    for i in range(1,10):
        tree1.add_node(i)
    tree2 = BinaryTree()
    for i in range(1,10):
        tree2.add_node(i)
    tree = BinaryTree()
    for i in range(1,15):
        tree.add_node(i)

    print(check_identical(tree1.root,tree2.root))
    print(check_identical(tree.root,tree1.root))
    print(check_identical(tree2.root,tree.root))