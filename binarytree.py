class binary_search_tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if self.data == data:
            return
        
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = binary_search_tree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = binary_search_tree(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
    def search(self,val):
        if self.data == val:
            return True
        
        if val< self.data:
            if self.left:
                return self.left.search(val)
            else: 
                return False

        else:
            if self.right:
                return self.right.search(val)
            else:
                return False        
        


def build_tree(elements):
    print("bulding tree with elements: ",elements)

    root = binary_search_tree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root



if __name__ ==  "__main__":
    numbers = [5,20,25,8,9,6,2]

    root = build_tree(numbers)

    print(root.in_order_traversal())

    print(root.search(25))

    pass




        
