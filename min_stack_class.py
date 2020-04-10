class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        

    def push(self, x: int) -> None:
        self.items.insert(0, x)
        
    def pop(self) -> None:
        return self.items.pop(0)
        

    def top(self) -> int:
        return self.items[0]
        

    def getMin(self) -> int:
        return min(self.items)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
