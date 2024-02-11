class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_last_node(self):
        if not self.head:
            print("List is empty")
            return

        if not self.head.next:
            self.head = None
            return

        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Create a linked list
ll = LinkedList()

# Take user input for appending nodes
n = int(input("Enter the number of elements to append: "))
print("Enter the elements:")
for _ in range(n):
    data = int(input())
    ll.append(data)

print("Original Linked List:")
ll.display()

# Delete the last node
ll.delete_last_node()
print("Linked List after deleting the last node:")
ll.display()
