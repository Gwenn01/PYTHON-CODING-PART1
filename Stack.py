class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
        self.top = -1
    # function of stack
    def push(self,data):
        self.top += 1
        self.stack.append(data)
        self.size += 1
        
    def pop(self):
        data = self.stack[self.top]
        self.stack.pop()
        self.top -= 1
        self.size -= 1
        return data
        
    def peek(self):
        if not self.isEmpty():
            return self.stack[self.top]
        return None
        
    def isEmpty(self):
        return self.size == 0
        
    def display(self):
        return print(self.stack)
        
# try it
stack = Stack()
stack.push(2)   
stack.push(10)
stack.push(5)
stack.push(12)   
stack.push(3)
stack.push(15)  
print(stack.peek())  
print(stack.pop())
stack.display()
