# def split(word):
#     arr=[char for char in word]
#     small=0
#     big=0
#     for i in arr:
#         if i.isupper():
#             big+=1
#         else:
#             small+=1
#     if big>small:
#         return 1
#     else:
#         return 0
#
#
# word = input()
# flag=split(word)
# if flag == 1:
#     print(word.upper())
# else:
#     print(word.lower())
#
# print(2031%100)
n = int(input())
ranklist = list(map(int, input().split()))
rank = [1]
it = 1

counter = 1
while counter != n - 1:
    if ranklist[counter - 1] != ranklist[counter]:
        rank.append(rank[-1] + 1)
    else:
        rank.append(rank[-1])
    counter += 1
no = int(input())
a = list(map(int, input().split()))
j = 0
for i in range(n - 1, -1):
    while a[j] >= ranklist[i] and i >= 0:
        i -= 1
    if i==0:
        print("1 \n")
    else:
        print(str(i))
