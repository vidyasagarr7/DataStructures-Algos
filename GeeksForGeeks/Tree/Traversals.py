from GeeksForGeeks.Tree.BinaryTree import BinaryTree

def preorder(node):
    if not node :
        return
    else :
        print(node.data)
        preorder(node.left)
        preorder(node.right)

def pre_order(root):
    if not root :
        return
    else:
        stac = [root]

        while len(stac) > 0 :
            node = stac.pop()
            print(node.data)
            if node.right :
                stac.append(node.right)
            if node.left :
                stac.append(node.left)

def postorder(node):
    if not node :
        return
    else :
        postorder(node.left)
        postorder(node.right)
        print(node.data)

def _postorder(root):
    if not root :
        return
    else :
        stac1 = [root]
        stac2 = []
        while len(stac1) > 0  :
            node = stac1.pop()
            stac2.append(node)
            if node.left :
                stac1.append(node.left)
            if node.right :
                stac1.append(node.right)

        while len(stac2)>0 :
            print(stac2.pop().data)

def post_order(root):
    if not root :
        return
    else :
        stac = []
        node = root

        while True :

            while node :
                if node.right :
                    stac.append(node.right)
                stac.append(node)
                node = node.left

            node = stac.pop()

            if len(stac) > 0 and node.right and stac[-1] == node.right :
                stac.pop()
                stac.append(node)
                node = node.right
            else :
                print(node.data)
                node = None

            if len(stac) <= 0 :
                break



if __name__=='__main__':
    bt = BinaryTree()
    for i in range(1,10):
        bt.add_node(i)
    #pre_order(bt.root)
    #bt.print_preorder()
    #_postorder(bt.root)
    post_order(bt.root)
