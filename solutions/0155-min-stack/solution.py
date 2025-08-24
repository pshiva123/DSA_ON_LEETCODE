class MinStack:

    def __init__(self):
        self.st=[]
        self.minst=[]
        

    def push(self, val: int) -> None:
        self.st.append(val)
        mini=val
        if len(self.minst)>0:
            mini=min(self.minst[-1],mini)
        self.minst.append(mini)

    def pop(self) -> None:
        self.minst.pop()
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]
        
    def getMin(self) -> int:
        return self.minst[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
