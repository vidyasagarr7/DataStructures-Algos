
class LinkedList:
    def __init__(self):
        self.head = None

    # Use this function to insert a new element in the LinkedList
    # Like a stack, elements should be added to the front (called the head) of the LinkedList.
    # None should not be allowed to be added to the list.
    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    # Use this function to find a Node with the specified data in the LinkedList
    # If the end of the list is reached, and the data are not found, return None.
    # If the list contains multiple Nodes with the requested Data, you only need to return the first one you find.
    def find(self, data):
        if self.head != None:
            while self.head.next != None:
                if (self.head.data == data):
                    return data
                self.head = self.head.next
            if (self.head.data == data):
                return self.head
        else:
            return None

    # Use this function to remove the specified Node from the LinkedList
    # Note that this function takes a Node (not data) as an argument.
    # Once the Node is removed, the list should still be able to be traversed - references will need to be updated to accomplish this task!
    # Think carefully about what needs to happen if the Node at the front of the list is removed, or if this node is the last Node in the list.
    def remove(self, node):
        temp = node.prev
        node.prev.next = node.next
        node.prevv = temp

    def print_linkedlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


# Use this class to represent a single element of the LinkedList
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


if __name__ == "__main__":
    ll = LinkedList()
    for i in range(1, 5):
        ll.insert(i)
    print('printing before')
    print(ll.print_linkedlist())
    print(ll.find(1))
    print('printing after')
    print(ll.print_linkedlist())

