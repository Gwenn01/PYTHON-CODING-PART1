class Tree:
    # Node class
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
     # root
     
    def __init__(self):
         self.root = None

          # add root     
    def addRoot(self, data):
         node = self.Node(data)
         self.root = node
      
     # add left        
    def addLeft(self, in_value, data):
         current = self.root
         while current:
             if in_value == current.val:
                 break
             current = current.left
             
         node = self.Node(data)
         current.left = node
         
    # add right
    def addRight(self, in_value, data):
        current = self.root
        while current:
             if in_value == current.val:
                 break
             current = current.right
            
        node = self.Node(data)
        current.right = node
        
    # display
    def display_temp(self, node, details):
        if node == None:
            return            
        print(details + str(node.val))
        self.display_temp(node.left, "Left child of: " + str(node.val) + ": ") 
        self.display_temp(node.right, "Right child of: " + str(node.val)+ ": ") 
                              
    def display(self):
        current = self.root
        details = "Root Node: "
        self.display_temp(current, details)  
  
# Treee                        
tree = Tree()
tree.addRoot(15)
tree.addLeft(15, 10)        
tree.addRight(15, 20)
tree.display()                                   