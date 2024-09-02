def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if(arr[j+1] < arr[j]):
                (arr[j] ,arr[j+1]) = (arr[j+1] ,arr[j])
        print(arr)
    return arr

arr = [1,4,2,8,3,9,0,12,60,15,44]
print(bubbleSort(arr))