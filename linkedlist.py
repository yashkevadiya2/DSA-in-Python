class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singlelist:
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

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.haed = new_node

    def printList(self):
        current_node = self.head
        while current_node.next:
            print(current_node.data)
            current_node = current_node.next  

s1 = singlelist()
s1.append(10)
s1.append(4)
s1.append(6)
s1.append(12)
s1.printList()