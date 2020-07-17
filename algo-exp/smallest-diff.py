import sys

arr = [-1, 5, 10, 20, 28, 3]
brr = [26, 134, 135, 15, 17]
arr.sort()
brr.sort()
man=[0,0]
i=0
j=0
small=sys.maxsize
while i<len(arr)-1 and j<len(brr)-1:
    if arr[i]-brr[j]==0:
        small=0
        break
    else:
        if arr[i]<brr[j]:
            i+=1
        else:
            j+=1
        small=min(small,abs(arr[i]-brr[j]))
        man[0]=arr[i]
        man[1]=brr[j]
        print(small,man)
