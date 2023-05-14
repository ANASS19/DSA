arr = [x for x in range(10)]
print(arr)


def binarysearch(arr, target):
    last = len(arr) - 1
    first = 0
    while first <= last:
        mid = (first+last) // 2
        print("this is: "+str(mid))
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return -1


result = binarysearch(arr, 5)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
