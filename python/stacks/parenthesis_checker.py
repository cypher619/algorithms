#!/bin/python3

import math
import os
import random
import re
import sys

opened = ["[", "{", "("]
closed = ["]", "}", ")"]


# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    for i in s:
        if i in opened:
            stack.append(i)
        elif i in closed:
            pos = closed.index(i)
            if (len(stack) > 0 and opened[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
