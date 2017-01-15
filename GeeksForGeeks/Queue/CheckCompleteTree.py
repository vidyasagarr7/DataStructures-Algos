from queue import Queue
from Trees.BinaryTree import BinaryTree

"""
Check whether a given Binary Tree is Complete or not | Set 1 (Iterative Solution)

Given a Binary Tree, write a function to check whether the given Binary Tree is Complete Binary Tree or not.

A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all
nodes are as far left as possible. See following examples.

The following trees are examples of Complete Binary Trees
    1
  /   \
 2     3

       1
    /    \
   2       3
  /
 4

       1
    /    \
   2      3
  /  \    /
 4    5  6
The following trees are examples of Non-Complete Binary Trees
    1
      \
       3

       1
    /    \
   2       3
    \     /  \
     4   5    6

       1
    /    \
   2      3
         /  \
        4    5

"""

# Rev

def check_complete(root):
    if not root :
        return True

    else :
        que = Queue()
        que.put(root)
        full_node = False
        while not que.empty() :
            node = que.get()

            if node.left :
                if full_node :
                    return False
                que.put(node.left)

            else :
                full_node = True

            if node.right :
                if full_node :
                    return False
                que.put(node.right)
            else :
                full_node = True

        return True

if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,5):
        bt.add_node(i)

    for i in range(2):
        bt.add_node(None)

    for i in range(6,15):
        bt.add_node(i)

    bt.print_levelorder()

    print(check_complete(bt.root))

    bt2 = BinaryTree()
    for j in range(1,15):
        bt2.add_node(j)

    print(check_complete(bt2.root))











