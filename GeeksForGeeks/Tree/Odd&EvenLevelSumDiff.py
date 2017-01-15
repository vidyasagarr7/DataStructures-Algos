
import queue
from GeeksForGeeks.Tree.BinaryTree import BinaryTree

"""
Difference between sums of odd level and even level nodes of a Binary Tree
Given a a Binary Tree, find the difference between the sum of nodes at odd level and the sum of nodes at
 even level. Consider root as level 1, left and right children of root as level 2 and so on.

For example, in the following tree, sum of nodes at odd level is (5 + 1 + 4 + 8) which is 18.
 And sum of nodes at even level is (2 + 6 + 3 + 7 + 9) which is 27. The output for following tree should be
 18 – 27 which is -9.

      5
    /   \
   2     6
 /  \     \
1    4     8
    /     / \
   3     7   9

"""

def find_diff(root):
    if not root:
        return 0
    else  :

        que = queue.Queue()
        que.put((root,1))
        even_sum = 0
        odd_sum = 0
        while not que.empty() :
            node,level  = que.get()

            if level & 1 :
                odd_sum += node.data
            else :
                even_sum += node.data

            if node.left :
                que.put((node.left,level+1))
            if node.right :
                que.put((node.right,level+1))
        return odd_sum-even_sum

if __name__=='__main__' :
    bt = BinaryTree()
    for i in range(1,15):
        bt.add_node(i)
    print(find_diff(bt.root))



