# FibArray = [0, 1]
#
#
#
#
# def fibonacci(n):
#     if n < 0:
#         print("Incorrect input")
#     elif n < len(FibArray):
#         return FibArray[n]
#     else:
#         temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
#         FibArray.append(temp_fib)
#         return temp_fib
arr = [0, 1]


def fib(n):
    if n < 0:
        print("jnklm")
    elif n < len(arr):
        return arr[n]
    else:
        temp_fib = fib(n - 1) + fib(n - 2)
        arr.append(temp_fib)
        return temp_fib


n = 23
for i in range(n):
    print(fib(i), end=" ")
# t = int(input())
# while t:
#     n = int(input())
#     print(fibonacci(n + 1) % 1000000007)
#   0 1 1 2  3 5 8

# 6
# 5 4
# 4 3
# 3 2
# 2 1
# 1 0
