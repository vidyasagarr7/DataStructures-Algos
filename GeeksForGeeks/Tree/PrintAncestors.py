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

def print_ancestors(node,target):
    # recursive algorithm to print all the ancestors of a node
    if not node :
        return False
    else :
        if node.data == target  :
            return True

        if print_ancestors(node.left,target) or print_ancestors(node.right,target):
            print(node.data)
            return True
        return False

def ancestors(root,item):
    if not root :
        return
    else :
        node = root
        stac = []
        while True  :

            while node and node.data != item :
                stac.append(node)
                node = node.left

            if node and node.data == item :
                break

            if stac[-1].right == None :
                node = stac.pop()

                while len(stac) > 0 and stac[-1].right == node :
                    node = stac.pop()

            node = None if len(stac) == 0 else stac[-1].right


        while len(stac) > 0 :
            node = stac.pop()
            print(node.data)




if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)
    print_ancestors(bt.root,8)

    ancestors(bt.root,8)