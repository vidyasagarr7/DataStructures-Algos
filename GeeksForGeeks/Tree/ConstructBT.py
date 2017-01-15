import sys

"""
Construct Special Binary Tree from given Inorder traversal
Given Inorder Traversal of a Special Binary Tree in which key of every node is greater than keys in left and right children, construct the Binary Tree and return root.

Examples:

Input: inorder[] = {5, 10, 40, 30, 28}
Output: root of following tree
         40
       /   \
      10     30
     /         \
    5          28

Input: inorder[] = {1, 5, 10, 40, 30,
                    15, 28, 20}
Output: root of following tree
          40
        /   \
       10     30
      /         \
     5          28
    /          /  \
   1         15    20
"""

class Node :
    def __init__(self,data):
        self.data= data
        self.left = None
        self.right = None

def find_max(io_list,start,end):
    _max = io_list[start]
    max_idx = start
    for i in range(start+1,end+1):
        if io_list[i] > _max :
            max_idx = i
            _max = io_list[i]
    return max_idx

def construct_bt(io,start,end):
    if not io  or start > end:
        return
    else :
        max_idx = find_max(io,start,end)

        node = Node(io[max_idx])

        if start == end :
            return node

        node.left = construct_bt(io,start,max_idx-1)
        node.right = construct_bt(io,max_idx+1,end)

        return node

def print_preorder(node):
    if not node :
        return
    else :
        print(node.data)
        print_preorder(node.left)
        print_preorder(node.right)

if __name__=='__main__':
    test = [5, 10, 40, 30, 28]
    root = construct_bt(test,0,len(test)-1)
    print_preorder(root)
