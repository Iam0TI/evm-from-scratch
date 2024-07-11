class Stack:

    """The EVM stack has a maximum capacity of 1024 items. Every item on the stack is at max a 256 bit value (32 bytes)."""
    global MAXIMUM_STACK_SIZE  
    MAXIMUM_STACK_SIZE  = 1024
    def __init__(self):
        self.items = []
    def __str__ (self): 
        ws = []
        for i, item in enumerate(self.items[::-1]):
            if   i == 0   :
                ws.append(f"{item} <first")
            elif i == len(self.items)-1: 
                ws.append(f"{item} <last") 
            else  :
                ws.append(str(item))
        return "\n".join(ws)
    
    def is_empty (self)  :
        if len(self.items) == 0:
            return False
        return True
    
    def push(self, value): 
        if len(self.items) == MAXIMUM_STACK_SIZE-1: 
            raise Exception("Stack overflow")
        self.items.append(value)    
    
    def pop(self, n=-1):
        if len(self.items) < n:
            raise Exception("Stack overflow")
        del self.items[n]
    def peek(self):
        if self.is_empty():
            raise Exception("peek from empty stack")
        return self.items[-1]