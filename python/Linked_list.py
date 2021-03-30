class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        current_node = self.head
        while current_node.next is not None:
            print(current_node.data)
            current_node = current_node.next
        print(current_node.data)

    def insert_at_front(self, data):
        newNode = Node(data)
        if self.head:

            newNode.next = self.head
            self.head = newNode
        else:
            self.head = newNode

    def insert_at_end(self, data):
        newNode = Node(data)
        if self.head:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = newNode
        else:
            self.head = newNode


llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)
llist.head.next = second
second.next = third

llist.printList()
print("In beginning")
llist.insert_at_front(10)
llist.insert_at_front(12)
llist.insert_at_front(20)
llist.printList()
print("In Ending")
llist.insert_at_end(100)
llist.insert_at_end(120)
llist.insert_at_end(200)
llist.printList()
