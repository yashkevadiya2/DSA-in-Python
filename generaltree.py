class TreeNode:
    def __init__(self, data):
        self.data = data
        self.childran = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.childran.append(child)

def create_tree_structure():

    root = TreeNode("schools")

    sanskar = TreeNode("sanskar")

    mahila = TreeNode("mahila")

    root.add_child(sanskar)

    return root

if __name__ == "__main__":
    root = create_tree_structure()
    pass


    
