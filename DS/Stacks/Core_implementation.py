# Implementation of Stacks

# Stacks is a one Dimensional Datastructure that follows First-IN-LAST-OUT
#
# Stacks generally has 4 core methods
# 1)PUSH
# 2)POP
# 3)REMOVE
# 4)DISPLAY

class Stack:
    def __init__(self):
        self.arr=[]

    def push(self,element):
        self.arr.append(element)

    def pop(self):
        self.arr.pop();

    def remove_index(self,index):
        self.arr.pop(index)

    def remove_value(self,value):
        self.arr.remove(value)

    def display(self):
        print(self.arr)

stack =Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.push(4)
stack.push(5)
stack.remove_value(1)
stack.remove_index(0)
stack.display()

