
class Heap:
    def __init__(self):
        self.heaplist = []
        self.size = 0

    def parent(self,index):
        """
        returns parent index of a specified index element
        :param index:
        :return:
        """
        return index//2

    def left_child(self,index):
        """
        returns left child
        :param index:
        :return:
        """
        return 2*index+1

    def right_child(self,index):
        """
        returns right child
        :param index:
        :return:
        """
        return 2*index+2

    def children(self,index):
        """
        returns children
        :param index:
        :return:
        """
        left_child = self.left_child(index)
        right_child = self.right_child(index)
        return left_child,right_child

    def percolate_down(self,index):
        """
        Heapify algorithm to
        :param index:
        :return:
        """







