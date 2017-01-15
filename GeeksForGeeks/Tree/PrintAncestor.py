from GeeksForGeeks.Tree.BinaryTree import BinaryTree

"""
Print Ancestors of a given node in Binary Tree

Given a Binary Tree and a key, write a function that prints all the ancestors of the key in the given binary tree.

For example, if the given tree is following Binary Tree and key is 7, then your function should print 4, 2 and 1.


              1
            /   \
          2      3
        /  \
      4     5
     /
    7
"""

def print_ancestor(node,value):
    if not node :
        return False
    else :
        if node.data == value :
            return True
        elif print_ancestor(node.left,value) or print_ancestor(node.right,value):
            print(node.data)
            return True
        return False

def print_ancestors(root,value):
    if not root :
        return
    else :
        node = root
        stac = []
        while True :

            while node and node.data != value :
                stac.append(node)
                node = node.left

            if not node :
                node = stac[-1]



if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)
    print_ancestor(bt.root,7)