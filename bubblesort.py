arr=[7,8,56,8,23,15,65]

def bubbleSort(theSeq):
    n=len(theSeq)
    for i in range(n-1):
        for j in range(n-1-i):
            if theSeq[j] >theSeq[j+1]:
                temp=theSeq[j+1]
                theSeq[j]=theSeq[j+1]
                theSeq[j+1]=temp
    return theSeq   
print(bubbleSort(arr))