class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """

        self.stk = []
        self.maxstk= []

    def push(self, x: int) -> None:

        self.stk.append(x)

        if not self.maxstk:
            self.maxstk.append(x)
        else:
            self.maxstk.append(max(x, self.maxstk[-1]))

    def pop(self) -> int:
        self.maxstk.pop()
        return self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def peekMax(self) -> int:
        return self.maxstk[-1]

    def popMax(self) -> int:
        n = self.maxstk.pop()
        i = len(self.stk) - 1
        tmp = []
        while n != self.stk[-1]:
            tmp.append(self.pop())
        ret = self.stk.pop()
        for i in range(len(tmp)-1, -1, -1):
            self.push(tmp[i])
        return ret

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()