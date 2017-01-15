from GeeksForGeeks.Tree.BinaryTree import BinaryTree

"""

Vertical Sum in a given Binary Tree | Set 1

Given a Binary Tree, find vertical sum of the nodes that are in same vertical line.
 Print all sums through different vertical lines.

Examples:

      1
    /   \
  2      3
 / \    / \
4   5  6   7
The tree has 5 vertical lines

Vertical-Line-1 has only one node 4 => vertical sum is 4
Vertical-Line-2: has only one node 2=> vertical sum is 2
Vertical-Line-3: has three nodes: 1,5,6 => vertical sum is 1+5+6 = 12
Vertical-Line-4: has only one node 3 => vertical sum is 3
Vertical-Line-5: has only one node 7 => vertical sum is 7

So expected output is 4, 2, 12, 3 and 7

"""

def vertical_sum(node,htable,dist):
    if not node :
        return 0
    else :
        # store the sum in hash table
        if dist not in htable :
            htable[dist] = node.data
        else :
            htable[dist] += node.data

        # explore left and right trees 
        if node.left :
            vertical_sum(node.left,htable,dist-1)
        if node.right :
            vertical_sum(node.right,htable,dist+1)

if __name__=='__main__':

    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)

    htable = {}
    vertical_sum(bt.root,htable,0)
    for j in htable :
        print('vert : {} and sum : {}'.format(j,htable[j]))


