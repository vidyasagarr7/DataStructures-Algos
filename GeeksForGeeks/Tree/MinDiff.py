from GeeksForGeeks.Tree.BST import BST

"""
Given a binary search tree and a target node K. The task is to complete the function which returns an integer denoting
the node having minimum absolute difference with given target value K.

Example



For above binary search tree
Input  :  k = 4
Output :  4

Input  :  k = 18
Output :  17

Input  :  k = 12
Output :  9


Input:
The first line of the input contains an integer 'T' denoting the number of test cases. Then 'T' test cases follow. Each test case consists of three lines. First line of each test case contains an integer N denoting the no of nodes of the BST . Second line of each test case consists of 'N' space separated integers denoting the elements of the BST. These elements are inserted into BST in the given order.The last line of each test case contains an integer k as specified in problem statement.

Output:
The output for each test case will be the value of the node with minimum absolute difference with given target value K.


Constraints:
1<=T<=100
1<=N<=200


Example(To be used only for expected output):
Input:
2
9
9 4 3 6 5 7 17 22 20
18
9
9 4 3 6 5 7 17 22 20
4
Output:
17
4
"""


def min_diff(node,k,diff,min_node):

    """
    :param node:
    :param k:
    :param diff:
    :return:
    """
    if not node :
        return 0
    else :
        if node.right and node.left :
            min_node = min(min_diff(node.left,k,diff,min_node),min_diff(node.right,k,diff,min_node))
        elif node.right and not node.left :
            min_node = min_diff(node.right,k,diff,min_node)
        elif node.left and not node.right :
            min_node = min_diff(node.left,k,diff,min_node)
        else :
            min_node = node.data

        if abs(node.data-k) < diff :
            diff = abs(node.data-k)
            min_node = node.data

        return min_node

if __name__=='__main__':
    bst = BST()
    bst.add_node(9)
    bst.add_node(4)
    bst.add_node(17)
    bst.add_node(3)
    bst.add_node(6)
    bst.add_node(None)
    bst.add_node(22)
    bst.add_node(None)
    bst.add_node(None)
    bst.add_node(5)
    bst.add_node(7)
    bst.add_node(20)

    print(min_diff(bst.root,4,100000,bst.root.data))
