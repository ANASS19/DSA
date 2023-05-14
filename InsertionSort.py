arr=[12,5,6,94,5,1,3,78,9,15]
def insertionsort(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[j] >temp:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
print(arr)
insertionsort(arr)
print(arr)

