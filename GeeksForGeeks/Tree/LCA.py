from GeeksForGeeks.Tree.BST import BST

"""
Lowest Common Ancestor in a Binary Search Tree.

Given values of two nodes in a Binary Search Tree, write a c program to find the Lowest Common Ancestor (LCA).
You may assume that both the values exist in the tree.

"""

def find_lca(node,val1,val2):
    if not node:
        return None
    else :
        if node.data < val1 and node.data < val2 :
            return find_lca(node.right,val1,val2)
        elif node.data > val1 and node.data > val2 :
            return find_lca(node.left,val1,val2)
        return node.data

def _find_lca(root,val1,val2) :
    if not root :
        return None
    else :

        current = root

        while True :
            if current.data > val1 and current.data > val2 :
                current = current.left
            elif current.data < val1 and current.data < val2 :
                current = current.right
            else :
                return current.data




if __name__=='__main__':
    bst = BST()
    bst.add_node(5)

    bst.add_node(2)
    bst.add_node(1)
    bst.add_node(3)

    bst.add_node(7)
    bst.add_node(6)
    bst.add_node(8)

    print(find_lca(bst.root,6,8))

    print(_find_lca(bst.root,6,8))
