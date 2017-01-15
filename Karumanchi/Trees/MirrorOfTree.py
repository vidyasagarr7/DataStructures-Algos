from Karumanchi.Trees import BinaryTree
from Karumanchi.Queue import Queue

def mirror_of_tree(node):
    """
    Non-Recursive implementation for building the mirror of a tree
    :param node:
    :return:
    """
    if not node :
        return None
    else:
        que = Queue.Queue1()
        que.enqueue(node)
        while not que.is_empty():
            node = que.dequeue()
            if node.get_left() and node.get_right():
                node.left, node.right = node.get_right(), node.get_left()
            if node.get_left():
                que.enqueue(node.get_left())
            if node.get_right():
                que.enqueue(node.get_right())

def _mirror(node):
    if not node :
        return None
    else:

        _mirror(node.get_left())
        _mirror(node.get_right())
        temp = node.get_left()
        node.left = node.get_right()
        node.right = temp


if __name__=="__main__":
    tree = BinaryTree()
    for i in range(1,10):
        tree.add_node(i)
    #mirror_of_tree(tree.root)
    _mirror(tree.root)
    tree.print_preorder()
