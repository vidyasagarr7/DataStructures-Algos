

"""
Construct a special tree from given preorder traversal
Given an array ‘pre[]’ that represents Preorder traversal of a spacial binary tree where every node has either 0 or 2 children. One more array ‘preLN[]’ is given which has only two possible values ‘L’ and ‘N’. The value ‘L’ in ‘preLN[]’ indicates that the corresponding node in Binary Tree is a leaf node and value ‘N’ indicates that the corresponding node is non-leaf node. Write a function to construct the tree from the given two arrays.

Source: Amazon Interview Question

Example:

Input:  pre[] = {10, 30, 20, 5, 15},  preLN[] = {'N', 'N', 'L', 'L', 'L'}
Output: Root of following tree
          10
         /  \
        30   15
       /  \
      20   5
"""

class Node :
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

class Index :
    def __init__(self,index):
        self.index = 0

def construct_tree(po,po_ch,index,end):
    if not po  :
        return
    else :

        if index.index==end :
            return

        node = Node(po[index.index])
        index.index += 1

        if index.index < end and  po_ch[index.index] =='N' :
            node.left = construct_tree(po,po_ch,index,end)
            node.right = construct_tree(po,po_ch,index,end)
        elif index.index < end and po_ch[index.index] == 'L':
            node.left = Node(po[index.index])
            index.index+= 1
            node.right = Node(po[index.index])
            index.index += 1

        return node

def print_preorder(node):
    if not node :
        return
    else :
        print(node.data)
        print_preorder(node.left)
        print_preorder(node.right)

if __name__=='__main__':
    po = [10, 30, 20, 5, 15]
    po_ch = ['N', 'N', 'L', 'L', 'L']
    idx = Index(0)
    node = Node()
    root = construct_tree(po,po_ch,idx,len(po))
    print_preorder(root)