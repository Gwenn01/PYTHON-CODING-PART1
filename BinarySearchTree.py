class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    # root
    root = None
    # add
    def insert_recur(self, data, node):
        if node == None:
            new_node = self.Node(data)
            return new_node
            
        if data < node.data:
            node.left = self.insert_recur(data, node.left)
        if data > node.data:
            node.right = self.insert_recur(data, node.right)   
                 
        return node  
        
    def insert(self, data):
        if self.root == None:
            node = self.Node(data)
            self.root = node
            return
        # call recursive
        self.root = self.insert_recur(data, self.root)
        
    # display
    def display_temp(self, node, details):
        if node == None:
            return            
        print(details + str(node.data))
        self.display_temp(node.left, "Left child of: " + str(node.data) + ": ") 
        self.display_temp(node.right, "Right child of: " + str(node.data)+ ": ") 
                              
    def display(self):
        current = self.root
        details = "Root Node: "
        self.display_temp(current, details)
        
bst = BST();
bst.insert(20)
bst.insert(50)
bst.insert(10)
bst.insert(15)
bst.display()