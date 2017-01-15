from queue import Queue
from Trees.BinaryTree import BinaryTree

"""
Level Order Tree Traversal

Level order traversal of a tree is breadth first traversal for the tree.

Level order traversal of the above tree is 1 2 3 4 5

"""


def _level_order(root):
    #algorithm to print level order traversal - O(n) time - using queue - iterative approach
    if not root :
        return
    else :

        que = Queue()
        que.put(root)
        while not que.empty():
            node = que.get()
            print(node.data)
            if node.left :
                que.put(node.left)
            if node.right :
                que.put(node.right)

def find_height(node):
    if not node :
        return 0
    else :
        lh = find_height(node.left)
        rh = find_height(node.right)

        return max(lh,rh)+1

def level_order(root):
    # O(n^2) algorithm using recursion, prints elements at every level
    ht = find_height(root)

    for i in range(1,ht+1):
        print_level(root,i)

def print_level(node,level):
    if not node :
        return
    if level == 1 :
        print(node.data)
    else :
        print_level(node.left,level-1)
        print_level(node.right,level-1)


if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)
    #_level_order(bt.root)

    level_order(bt.root)
