import queue
from GeeksForGeeks.Tree.BinaryTree import BinaryTree

"""
Extract Leaves of a Binary Tree in a Doubly Linked List


Given a Binary Tree, extract all leaves of it in a Doubly Linked List (DLL).
 Note that the DLL need to be created in-place. Assume that the node structure of DLL and
  Binary Tree is same, only the meaning of left and right pointers are different. In DLL,
   left means previous pointer and right means next pointer.

Let the following be input binary tree
        1
     /     \
    2       3
   / \       \
  4   5       6
 / \         / \
7   8       9   10


Output:
Doubly Linked List
7<->8<->5<->9<->10

Modified Tree:
        1
     /     \
    2       3
   /         \
  4           6


"""


def extract_leaves(root):
    if not root :
        return
    else :
        


def preorder(root):
    if not root :
        return
    else :
        stac = [root]

        while len(stac) > 0 :
            node = stac.pop()
            print(node.data)
            if node.right :
                stac.append(node.right)
            if node.left :
                stac.append(node.left)

def levelorder(root):
    if not root :
        return
    else :
        que = queue.Queue()
        que.put(root)
        while not que.empty() :
            node = que.get()
            print(node.data)
            if node.left :
                que.put(node.left)
            if node.right :
                que.put(node.right)


if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)
    preorder(bt.root)





