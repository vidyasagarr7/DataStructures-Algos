from GeeksForGeeks.Tree.BinaryTree import BinaryTree

import queue
"""
Check if all leaves are at same level
Given a Binary Tree, check if all leaves are at same level or not.

          12
        /    \
      5       7
    /          \
   3            1
  Leaves are at same level

          12
        /    \
      5       7
    /
   3
   Leaves are Not at same level


          12
        /
      5
    /   \
   3     9
  /      /
 1      2
 Leaves are at same level

"""

def check_leaflevels(root):
    if not root :
        return
    else :
        que = queue.Queue()
        que.put((root,1))
        leaf_level = -1
        while not que.empty() :
            node,level = que.get()

            if not node.left and not node.right :
                if leaf_level == -1  :
                    leaf_level = level
                elif leaf_level != level :
                    return False

            if node.left :
                que.put((node.left,level+1))
            if node.right :
                que.put((node.right,level+1))
        return True

if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,16):
        bt.add_node(i)

    print(check_leaflevels(bt.root))













