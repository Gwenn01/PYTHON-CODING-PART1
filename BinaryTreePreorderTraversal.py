class Solutions:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    # root
    def __init__(self):
        self.root = None
    # add  
    def add(self, val):
        if self.root is None:
            node = self.TreeNode(val)
            self.root = node
            return
        self.root = self.add_temp(self.root, val)
    # temp add   
    def add_temp(self, node, val):
        if node is None:
            new_node = self.TreeNode(val)
            return new_node
        if val < node.val:
            node.left = self.add_temp(node.left, val)
        if val > node.val:
            node.right = self.add_temp(node.right, val)        
        return node
     # Preorder Traversal
    def temp(self, node, container):
         if node is None:
             return
         container.append(node.val)
         self.temp(node.left, container)
         self.temp(node.right, container)
         
    def preorder_traversal(self, root):
        container = []
        self.temp(root, container)
        return container
        
     # main 
    def main(self):
         ans = self.preorder_traversal(self.root)
         print(ans)
        
        
      
tree = Solutions()
tree.add(2)
tree.add(5)
tree.add(3)
tree.add(1)
tree.add(9)
tree.main()
            