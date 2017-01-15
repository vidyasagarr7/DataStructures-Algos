from Karumanchi.Trees import BinaryTree
from Karumanchi.Queue import Queue

"""
Construct a tree from Inorder and Preorder traversals
"""

def construct(inorder_string,preorder_string):
    """
    Constructing a tree from Inorder and Preorder traversals
    :param inorder_string:
    :param preorder_string:
    :return:
    """
    if not inorder_string and not preorder_string:
        return None
    else :
        que = Queue.Queue1()
        root = preorder_string[0]
        preorder_string = preorder_string[1:]
        left_string,right_string = inorder_string.split(root)[0],inorder_string[2]
        