class Solutions:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    # Root node
    def __init__(self):
        self.root = None
        
    def add(self, val):
        node = self.ListNode(val)
        if self.root is None:
            self.root = node
            return
        temp = self.root
        while temp.next != None:
             temp = temp.next
        temp.next = node
    
    def display(self, node):
        temp = node
        while temp != None:
            print(f"{temp.val} -> ", end="")
            temp = temp.next
    # Remove Elements
    def removeElements(self, head, val):
        if head is None:
            return head
        # recursion call
        head.next = self.removeElements(head.next, val)  
        # if head val = val return the next 
        if head.val == val:
            return head.next
        return head           

    # main
    def main(self, val):
        self.display(self.root)
        temp = self.removeElements(self.root, val)
        print() 
        self.display(temp)
        
                
list = Solutions()
list.add(1)      
list.add(2)
list.add(6)
list.add(3)
list.add(4)
list.add(5)
list.add(6)
val = 6
list.main(val)