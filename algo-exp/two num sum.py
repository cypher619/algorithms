arr = list(map(int, input().split()))
target = int(input())
h_table = []
for i in arr:
    if (target-i) in h_table:
        print("the target sum of "+str(target)+" is "+str(i)+" and "+str(target-i))
        break
    else:
        h_table.append(i)
