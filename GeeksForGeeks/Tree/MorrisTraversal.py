from GeeksForGeeks.Tree.BinaryTree import BinaryTree

"""
Inorder traversal without recursion and without stack
"""

def morris_traversal(root):
    if not root :
        return
    else :

        node = root

        while node :

            if node.left is None :
                print(node.data)
                node= node.right
            else  :
                pre = node.left

                while pre.right and pre.right is not node:
                    pre = pre.right

                if pre.right is None :
                    pre.right = node
                    node = node.left
                else :
                    pre.right = None
                    print(node.data)
                    node = node.right

def inorder(root):
    if not root :
        return
    else:
        s = []
        node = root

        while node or len(s)>0 :
            if node :
                s.append(node)
                node = node.left
            else:
                node = s.pop()
                print(node.data)
                node = node.right

if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)
    #morris_traversal(bt.root)
    bt.print_inorder()
    inorder(bt.root)
