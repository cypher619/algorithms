
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



class Parenthesis_checker:
    def __init__(self,input):
        self.stack =[]
        for i in input:
            self.stack.append(i)

    def displayStack(self):
        print(self.stack)

    def checkValidity(self):
        SS =Stack()
        i=0
        for element in self.stack:
            pass


Checker = Parenthesis_checker("()")
Checker.displayStack()


