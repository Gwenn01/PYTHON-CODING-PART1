class Solution():
    class Node:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            
    # root     
    def __init__(self):
         self.root1 = None
         self.root2 = None
    
    # add root
    def add_root1(self, val):
        node = self.Node(val)
        self.root1 = node
        
    def add_root2(self, val):
        node = self.Node(val)
        self.root2 = node
        
     # add left node
    def add_left1(self, val):
         current = self.root1
         self.add_leftt1(current, val)
     
    def add_leftt1(self, node, val):
        if node.left == None:
            new_node = self.Node(val)
            node.left = new_node
            return
        self.add_leftt1(node.left, val)
        
    def add_left2(self, val):
         current = self.root2
         self.add_leftt2(current, val)
     
    def add_leftt2(self, node, val):
        if node.left == None:
            new_node = self.Node(val)
            node.left = new_node
            return
        self.add_leftt2(node.left, val)
    
    # add right node
    def add_right1(self, val):
        current = self.root1
        self.add_rightt1(current, val)
        
    def add_rightt1(self, node, val):
        if node.right == None:
             new_node = self.Node(val)
             node.right = new_node
             return
        self.add_rightt1(node.right, val)
     
    def add_right2(self, val):
        current = self.root2
        self.add_rightt2(current, val)
        
    def add_rightt2(self, node, val):
        if node.right == None:
             new_node = self.Node(val)
             node.right = new_node
             return
        self.add_rightt2(node.right, val)
    
    # displaying the value
    def display(self, node):
        current = node
        detail = "Root Node: "
        self.display_temp(current, detail)
        
    def display_temp(self, node, detail):
         if node == None:
             return
         print(f"{detail}: {node.val}")
         self.display_temp(node.left, f"Left child of {node.val}: ")
         self.display_temp(node.right, f"Right child of {node.val}: ")
         
    def isSameTree(self, p, q):
        #check if we reach the end
        if p is None and q is None:
            return True
        #check if one is reach the end  
        if p is None or q is None:
            return False
        # if not equal                     
        if p.val != q.val:
            return False
        # recursive call
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)  
            
    # adding value 
    def main(self):
        # add value in first node
        self.add_root1(1)
        self.add_left1(2)
        self.add_right1(3)
        self.display(self.root1)
        print()
        # add value in second node
        self.add_root2(1)
        self.add_left2(2)
        self.add_right2(3)
        self.display(self.root2)
        print()
        # class out solution in main 
        ans = self.isSameTree(self.root1, self.root2)
        print("Is Same Tree")
        print(ans)
                
        
solution = Solution()
solution.main()