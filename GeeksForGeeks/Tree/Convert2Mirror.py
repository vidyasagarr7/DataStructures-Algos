import queue
from GeeksForGeeks.Tree.BinaryTree import BinaryTree

def create_mirror(node):
    """
    Non - recursive implementation
    :param node:
    :return:
    """

    if not node :
        return
    else :
        que = queue.Queue()
        que.put(node)
        while not que.empty():
            node = que.get()
            if node.left :
                que.put(node.left)
            if node.right :
                que.put(node.right)

            node.left, node.right = node.right, node.left

def _create_mirror(node):
    """
    Recursive implementation
    :param node:
    :return:
    """
    if not node :
        return None
    else :
        _create_mirror(node.left)
        _create_mirror(node.right)
        node.left,node.right = node.right, node.left



if __name__=='__main__':
    tree = BinaryTree()
    for i in range(1,10):
        tree.add_node(i)
    create_mirror(tree.root)
    tree.print_levelorder()
    _create_mirror(tree.root)
    tree.print_levelorder()