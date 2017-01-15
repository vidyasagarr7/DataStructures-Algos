class Node:
    next_node = None
    prev_node = None
    data = None

    def __init__(self, data):
        self.data = data


# Use this class to implement the LinkedList
# A Linked List is a data structure made of Nodes, which each contain a reference to the next Node in the list
# You may choose to construct a Doubly Linked List, where each Node also contains a reference to the
# previous Node in the list, but doing so is not required.
# The important idea is that Nodes don't know about all of the items in the list, only the next
# (and in a Doubly Linked List, the previous) element.
# You should not have a table of all of the elements in this structure.
class LinkedList:
    sentinel = Node(None)

    def __init__(self):
        self.sentinel.next_node = self.sentinel
        self.sentinel.prev_node = self.sentinel

    # Use this function to insert a new element in the LinkedList
    # Like a stack, elements should be added to the front (called the sentinel) of the LinkedList.
    # None should not be allowed to be added to the list.
    def insert(self, data):
        if data is None:
            return
        n = Node(data)
        n.prev_node = self.sentinel
        n.next_node = self.sentinel.next_node
        self.sentinel.next_node.prev_node = n
        self.sentinel.next_node = n

    # Use this function to find a Node with the specified data in the LinkedList
    # If the end of the list is reached, and the data are not found, return None.
    # If the list contains multiple Nodes with the requested Data, you only need to return the first one you find.
    def find(self, data):
        n = self.sentinel.next_node
        while n.data is not None:
            if n.data == data:
                return n
            n = n.next_node
        return None

    # Use this function to remove the specified Node from the LinkedList
    # Note that this function takes a Node (not data) as an argument.
    # Once the Node is removed, the list should still be able to be traversed - references will
    # need to be updated to accomplish this task!
    # Think carefully about what needs to happen if the Node at the front of the list is removed,
    # or if this node is the last Node in the list.
    # noinspection PyMethodMayBeStatic
    def remove(self, node):
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node


    def print_linkedlist(self):
        temp = self.sentinel
        while temp:
            print(temp.data)
            temp = temp.next

if __name__=="__main__":
    ll = LinkedList()
    for i in range(1, 5):
        ll.insert(i)
    print('printing before')
    print(ll.print_linkedlist())
    print(ll.find(1))
    print('printing after')
    print(ll.print_linkedlist())