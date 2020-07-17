class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        number=int(number)
        # cat=self.minMaxStack.peek()
        # if number > self.minMaxStack.peek():
        #     self.minMaxStack.append(number)
        # else:
        #     self.minMaxStack.append(cat)
        # return self.stack.append(number)
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax['min'] = min(lastMinMax["min"], number)
            newMinMax['max'] = max(lastMinMax["max"], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    def getMin(self):
        topMin = self.minMaxStack[len(self.minMaxStack) - 1]
        return topMin['min']

    def getMax(self):
        topMax = self.minMaxStack[len(self.minMaxStack) - 1]
        return topMax['max']


a = MinMaxStack()
a.push(2)
a.push(5)
a.push(7)
print(a.peek())
print(a.getMax())
print(a.getMin())

a.pop()
print(a.peek())
print(a.getMax())
print(a.getMin())

