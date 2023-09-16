class LinkedList:
    # node class
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
        
    def __init__(self):
     # head of node    
     self.head = None
     # add value to node
    def add(self, data):
         node = self.Node(data)
         if self.head == None:
             self.head = node
         else:
             current = self.head
             while current.next:
                 current = current.next
             current.next = node
    # delete value in our node
    def remove(self):
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
            
        data = current.value
        prev.next = None
        return data
    # display the value of node
    def display(self):
        current = self.head
        while current:
            print(str(current.value) + " -> ", end="")
            current = current.next
        print(" END")

# lets try it
list = LinkedList()
list.add(5)
list.add(10)
list.add(15)
list.add(20)
list.add(30)
print(list.remove())
list.display()
