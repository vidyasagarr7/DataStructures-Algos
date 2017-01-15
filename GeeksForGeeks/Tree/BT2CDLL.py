from GeeksForGeeks.Tree.BinaryTree import BinaryTree


def BT2CDLL(node):
    if not node :
        return None
    else :
        _left = BT2CDLL(node.left)
        _right = BT2CDLL(node.right)

        node.left = node.right = node
        return concat(concat(_left,node),_right)

def concat(left,right):
    if not left :
        return right
    if not right :
        return left

    l_last = left.left
    r_last = right.left

    l_last.right = right
    right.left = l_last

    r_last.right = left
    left.left = r_last

    return left

def print_dll(head):

    print(head.data)
    cur = head.right
    while cur != head :
        print(cur.data)
        cur = cur.right
    return

if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)


    out = BT2CDLL(bt.root)
    print_dll(out)


