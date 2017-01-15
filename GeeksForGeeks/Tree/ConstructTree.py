from GeeksForGeeks.Tree.BinaryTree import Node,BinaryTree

"""
Construct Tree from given Inorder and Preorder traversals
Let us consider the below traversals:

Inorder sequence: D B E A F C
Preorder sequence: A B D E C F

In a Preorder sequence, leftmost element is the root of the tree. So we know ‘A’ is root for given sequences.
By searching ‘A’ in Inorder sequence, we can find out all elements on left side of ‘A’ are in left subtree and
elements on right are in right subtree. So we know below structure now.

                 A
               /   \
             /       \
           D B E     F C
We recursively follow above steps and get the following tree.

         A
       /   \
     /       \
    B         C
   / \        /
 /     \    /
D       E  F

"""

def search(arr, start, end, value):
    for i in range(start, end+1):
        if arr[i] == value:
            return i

def build_tree(io_list,po_list,start,end,index):

    if start>end :
        return None

    node = Node(po_list[index])
    index +=1

    if start==end :
        return node

    io_idx = search(io_list,start,end,po_list[index-1])
    print(node.data)

    node.left = build_tree(io_list,po_list,start,io_idx-1,index)
    node.right = build_tree(io_list,po_list,io_idx+1,end,index)

    return node

def print_preorder(node):
    if not node :
        return
    else :
        print(node.data)
        print_preorder(node.left)
        print_preorder(node.right)

if __name__=='__main__':

    io = ['D', 'B','E', 'A', 'F', 'C']

    po = ['A', 'B', 'D', 'E', 'C', 'F']
    index =  0
    root = build_tree(io,po,0,len(io)-1,index)
    print_preorder(root)






