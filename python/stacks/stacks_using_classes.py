class Stack:
    def __init__(self):
        self.arr = []

    def push(self, data):
        self.arr.append(data)

    def pop(self):
        self.arr = self.arr[:-1]

    def display(self):
        print(self.arr)


new = Stack()
new.push(2)
new.push(4)
new.push(5)
new.push(26)
new.pop()
new.push(8)
new.display()
