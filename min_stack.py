class MinStack:

    def __init__(self):
        self.stack = []
        self.minimos = []

    def push(self, val: int) -> None:
        if not self.minimos:
            self.minimos.append(val)
        else:
            self.minimos.append(min(val, self.minimos[-1]))

        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimos.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimos[-1]