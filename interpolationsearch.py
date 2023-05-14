def interpolationsearch(array, value):
    high = len(array) - 1
    low = 0
    while array[low] <= value <= array[high] and low <= high:
        probe = low + (high - low) * (value - array[low]) // (array[high] - array[low])
        print("probe is: " + str(probe))

        if array[probe] == value:
            return probe
        elif array[probe] < value:
            low = probe + 1
        else:
            high = probe - 1


arr = [x for x in range(10)]
print(arr)
index = interpolationsearch(arr, 8)
if index != -1:
    print("Element found at index: " + str(index))
else:
    print("Element not found")
