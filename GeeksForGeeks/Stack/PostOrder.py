from GeeksForGeeks.Tree.BinaryTree import BinaryTree
"""

Iterative Postorder Traversal | Set 1 (Using Two Stacks)

We have discussed iterative inorder and iterative preorder traversals. In this post,
iterative postorder traversal is discussed which is more complex than the other two traversals
(due to its nature of non-tail recursion, there is an extra statement after the final recursive call to itself).
 The postorder traversal can easily be done using two stacks though. The idea is to push reverse
 postorder traversal to a stack. Once we have reverse postorder traversal in a stack, we can just
 pop all items one by one from the stack and print them, this order of printing will be in postorder
 because of LIFO property of stacks. Now the question is, how to get reverse post order elements in a stack –
 the other stack is used for this purpose. For example, in the following tree, we need to get
 1, 3, 7, 6, 2, 5, 4 in a stack. If take a closer look at this sequence, we can observe that this
 sequence is very similar to preorder traversal. The only difference is right child is visited before
 left child and therefore sequence is “root right left” instead of “root left right”. So we can do
  something like iterative preorder traversal with following differences.
a) Instead of printing an item, we push it to a stack.
b) We push left subtree before right subtree.
"""

def print_postorder(root):
    if not root :
        return
    else :
        stac1 = [root]
        stac2 = []
        while len(stac1) > 0:
            node = stac1.pop()
            stac2.append(node)
            if node.left :
                stac1.append(node.left)
            if node.right :
                stac1.append(node.right)

        while len(stac2) > 0 :
            node = stac2.pop()
            print(node.data)

if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)

    print_postorder(bt.root)



