class Stack():
    def __init__(self, stack_size):
        self.stack_arr = []
        self.stack_size = stack_size
    
    def isEmpty(self):
        return len(self.stack_arr) == 0
    
    def isFull(self):
        return len(self.stack_arr) == self.stack_size
    
    def pushStack(self, item):
        if(self.isFull()):
            return "Stack is Full"
        
        self.stack_arr.append(item)
        print("Pushed Item: {}".format(item))
    
    def popStack(self):
        if(self.isEmpty()):
            return "Stack is Empty"
        
        return self.stack_arr.pop()
    
    def displayStack(self):
        print("Current Stack: ", self.stack_arr)


lol = Stack(5)
lol.pushStack(5)
lol.pushStack(4)
lol.pushStack(3)
lol.pushStack(2)
lol.pushStack(1)
lol.pushStack(0)
lol.displayStack()
print(lol.popStack(),"was popped!")
lol.displayStack()
print("CODE CHANGE!!!")