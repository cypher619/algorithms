def bin_search(arr, l, h ,key):
    mid = l + (h - l) // 2
    while h>=l:
        if arr[mid]==key:
            return mid
        if key>arr[mid]:
            return bin_search(arr,mid+1,h,key)
        bin_search(arr,l,mid-1,key)
    return -1




arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
l = 0
h = len(arr) - 1
print(bin_search(arr, l, h,51))
