class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

def create_linked_list():
    linked_list = LinkedList()
    n = int(input("Enter the number of elements in the linked list: "))
    for i in range(n):
        data = int(input("Enter element {}: ".format(i + 1)))
        linked_list.append(data)
    return linked_list

linked_list = create_linked_list()
print("Length of the linked list:", linked_list.length())
