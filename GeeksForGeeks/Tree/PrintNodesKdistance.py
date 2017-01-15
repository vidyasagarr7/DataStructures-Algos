import queue
from GeeksForGeeks.Tree.BinaryTree import BinaryTree

"""
Print nodes at k distance from root

Given a root of a tree, and an integer k. Print all the nodes which are at k distance from root.

For example, in the below tree, 4, 5 & 8 are at distance 2 from root.
            1
          /   \
        2      3
      /  \    /
    4     5  8
The problem can be solved using recursion. Thanks to eldho for suggesting the solution.

"""

def print_nodes_k_distance(root,k):
    if not root :
        return
    else :
        que = queue.Queue()
        que.put((root,1))
        while not que.empty() :
            node,level = que.get()
            if level == k :
                print(node.data)
            if node.left :
                que.put((node.left,level+1))
            if node.right :
                que.put((node.right,level+1))

def print_nodes(node,k):
    if not node  :
        return
    if k == 1 :
        print(node.data)
    else :
        print_nodes(node.left,k-1)
        print_nodes(node.right,k-1)

if __name__=='__main__':

    bt = BinaryTree()
    for i in range(1,25):
        bt.add_node(i)
    print_nodes_k_distance(bt.root,3)
    print_nodes(bt.root,3)



