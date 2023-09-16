class Solution:
    class Node:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
     # root node       
    def __init__(self):
        self.root = None
    # add root
    def add_root(self, val):
        node = self.Node(val)
        self.root = node
        
    # add left
    def add_leftof(self, value_of, val):
         current = self.root
         self.add_left_temp(current, value_of, val)    
         
    def add_left_temp(self, node, value_of, val):
         if node is None:
             return
         if node.val == value_of:
             new_node = self.Node(val)
             node.left = new_node 
             return
         self.add_left_temp(node.left, value_of, val)
         self.add_left_temp(node.right, value_of, val)
    
    # add right                                     
    def add_rightof(self, value_of, val):
             current = self.root
             self.add_right_temp(current, value_of, val)
             
    def add_right_temp(self, node, value_of, val):
             if node is None:
                 return                
             if node.val == value_of:
                 new_node = self.Node(val)
                 node.right = new_node
                 return
             self.add_right_temp(node.right, value_of, val)
             self.add_right_temp(node.left, value_of, val) 

    # displaying the value
    def display(self):
        current = self.root
        detail = "Root Node: "
        self.display_temp(current, detail)
        
    def display_temp(self, node, detail):
         if node == None:
             return
         print(f"{detail}: {node.val}")
         self.display_temp(node.left, f"Left child of {node.val}: ")
         self.display_temp(node.right, f"Right child of {node.val}: ")   
     
   # Solutions 
    def main(self):
       return self.isSymmetric(self.root)
    # answer
    def is_symmetric(self, left, right):
        # check if the node leaf is balanced
        if left is None and right is None:
            return True
        # check if one of them is not balanced
        if left is None or right is None:
            return False
        # check the value and then call every recursive
        return left.val == right.val and self.is_symmetric(left.left, right.right) and self.is_symmetric(left.right, right.left)
                                          
    def isSymmetric(self, root):
        return self.is_symmetric(root.left, root.right)
        
             
         
tree = Solution()
tree.add_root(1)
tree.add_leftof(1, 2)
tree.add_rightof(1, 3)
tree.display()
answer = tree.main()
print(answer)
    