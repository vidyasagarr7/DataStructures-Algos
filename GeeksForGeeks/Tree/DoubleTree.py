from GeeksForGeeks.Tree.BinaryTree import BinaryTree,Node

"""
Double Tree
Write a program that converts a given tree to its Double tree. To create Double tree of the given tree,
create a new duplicate for each node, and insert the duplicate as the left child of the original node.


"""

def double_tree(node):
    if not node :
        return
    else :
        double_tree(node.left)
        double_tree(node.right)

        new_node = Node(node.data)
        left = node.left
        node.left = new_node
        new_node.left = left

if __name__ == '__main__':
    bt = BinaryTree()
    for i in range(1,4):
        bt.add_node(i)

    double_tree(bt.root)
    bt.print_levelorder()
