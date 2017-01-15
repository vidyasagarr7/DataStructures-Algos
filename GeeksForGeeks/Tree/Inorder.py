from GeeksForGeeks.Tree.BinaryTree import BinaryTree

"""
Inorder Tree Traversal without Recursion

"""

def inorder_traversal(root):
    # inorder traversal with using stack
    if not root :
        return
    else :
        node = root
        stac = []
        while node or len(stac) > 0 :
            if node :
                stac.append(node)
                node = node.left
            else :
                node  = stac.pop()
                print(node.data)
                node = node.right

def _inorder_traversal(root):
    if not root :
        return
    else :
        current = root
        while current is not None :
            if current.left is None :
                print(current.data)
                current = current.right
            else :
                pre_suc = current.left
                while pre_suc.right is not None and pre_suc.right is not current :
                    pre_suc = pre_suc.right

                if pre_suc.right is None  :
                    pre_suc.right = current
                    current = current.left
                else:
                    pre_suc.right = None
                    print(current.data)
                    current = current.right


def _inorder(root):
    # inorder traversal with out stack or without recursion. -- > Morris Traversal

    if not root :
        return
    else  :
        # Set current to root of binary tre

        current = root

        while (current is not None):

            if current.left is None:
                print(current.data)
                current = current.right
            else:
                # Find the inorder predecessor of current
                pre = current.left
                while (pre.right is not None and pre.right is not current):
                    pre = pre.right

                # Make current as right child of its inorder predecessor
                if (pre.right is None):
                    pre.right = current
                    current = current.left

                    # Revert the changes made in if part to restore the original
                    # tree i.e., fix the right child of predecssor
                else:
                    pre.right = None
                    print(current.data)
                    current = current.right


if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)
    #inorder_traversal(bt.root)
    _inorder(bt.root)
    #_inorder_traversal(bt.root)