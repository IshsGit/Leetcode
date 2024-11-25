class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # This will keep track of the minimum elements

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Maintain the minimum value using an auxiliary stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            popped_val = self.stack.pop()
            # If the popped value is the current minimum, remove it from the min_stack
            if popped_val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]

# Usage example:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # Output: -3
minStack.pop()
print(minStack.top())     # Output: 0
print(minStack.getMin())  # Output: -2
