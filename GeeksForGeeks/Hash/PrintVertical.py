from GeeksForGeeks.Tree.BinaryTree import BinaryTree

"""
Print a Binary Tree in Vertical Order | Set 2 (Hashmap based Method)
Given a binary tree, print it vertically. The following example illustrates vertical order traversal.

           1
        /    \
       2      3
      / \    / \
     4   5  6   7
             \   \
              8   9


The output of print this tree vertically will be:
4
2
1 5 6
3 8
7
9

"""


def print_vertical(node,htable,dist) :
    if not node :
        return None

    else :
        if dist not in htable :
            htable[dist] = [node.data]
        else :
            htable[dist].append(node.data)

        if node.left  :
            print_vertical(node.left,htable,dist-1)
        if node.right :
            print_vertical(node.right,htable,dist+1)

if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)
    htable = {}
    print_vertical(bt.root,htable,0)

    for dist in htable :
        print('hd : {} and elements : {} '.format(dist,htable[dist]))