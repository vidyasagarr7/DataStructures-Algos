import queue
from BinaryTree import BinaryTree,BinaryTreeNode

def build_tree():
    tree = BinaryTree()
    for i in range(1,11):
        tree.add_node(i)
    return tree

def print_reverse_lo(root):
    """
    Non-recursive implementation of printing the level order data in reverse order
    :param node:
    :return:
    """
    if root is None:
        return
    else:
        stack =[]
        que = queue.Queue()
        que.put(root)
        while not que.empty():
            node = que.get()
            if node.get_left():
                que.put(node.get_left())
            if node.get_right():
                que.put((node.get_right()))
            stack.append(node.data)
        while stack:
            print(stack.pop())


def print_levelorder(root):
    if root is None:
        return
    else:
        que = queue.Queue()
        que.put(root)
        while not que.empty():
            node = que.get()
            print(node.data)
            if node.get_left() :
                que.put(node.get_left())
            if node.get_right():
                que.put(node.get_right())


if __name__=="__main__":

    tree = build_tree()
    print(print_reverse_lo(tree.root))
