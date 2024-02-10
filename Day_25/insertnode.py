class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    linked_list = LinkedList()

    while True:
        data = input("Enter data to insert at the beginning (or type 'exit' to stop): ")
        if data.lower() == "exit":
            break
        linked_list.insert_at_beginning(int(data))

    print("Linked List after insertions:")
    linked_list.display()
