from GeeksForGeeks.Tree.BinaryTree import BinaryTree

"""
Remove all nodes which don’t lie in any path with sum>= k

Given a binary tree, a complete path is defined as a path from root to a leaf.
 The sum of all nodes on that path is defined as the sum of that path. Given a number K,
  you have to remove (prune the tree) all nodes which don’t lie in any path with sum>=k.

Note: A node can be part of multiple paths. So we have to delete it only in case when all paths from
it have sum less than K.

Consider the following Binary Tree
          1
      /      \
     2        3
   /   \     /  \
  4     5   6    7
 / \    /       /
8   9  12      10
   / \           \
  13  14         11
      /
     15

For input k = 20, the tree should be changed to following
(Nodes with values 6 and 8 are deleted)
          1
      /      \
     2        3
   /   \        \
  4     5        7
   \    /       /
    9  12      10
   / \           \
  13  14         11
      /
     15

For input k = 45, the tree should be changed to following.
      1
    /
   2
  /
 4
  \
   9
    \
     14
     /
    15
"""

def remove_nodes(node,_sum):
    if not node :
        return
    else :
        node.left = remove_nodes(node.left, _sum - node.data)
        node.right = remove_nodes(node.right, _sum - node.data)

        if not node.left and not node.right :
            if node.data < _sum :
                node  = None
        return node

if __name__ =='__main__':
    bt = BinaryTree()
    for i in range(1,20):
        bt.add_node(i)
    remove_nodes(bt.root,25)
    bt.print_levelorder()




