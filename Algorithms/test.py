# def reverse(string):
#     if len(string) == 0:
#         return string
#     else:
#         return reverse(string[1:]) + string[0]
# a = str(input("Enter the string to be reversed: "))
# print(reverse(a))


t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    final = 9
    q = int(input())
    while q:
        if q == 0:
            break
        for i in range(len(arr) - 1, -1, -1):
            if q == 0:
                break
            if arr[i] == 0:
                break
            else:
                if q > arr[i]:
                    q = q - arr[i]
                    arr[i] = 0
                else:
                    arr[i] = arr[i] - q
                    q = 0
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != 0:
            final = i
            break

    print(final + 1, arr)
    print("=============")


