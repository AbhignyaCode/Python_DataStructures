def insertionSort(arr) :  
    for i in range (1 ,len(arr)):
        j = i-1
        temp = arr[i]
        while(j >= 0 and arr[j] > temp):
            arr[j+1] = arr[j]
            j = j-1
            arr[j+1] = temp
    return arr

arr = [6,2,9,3,7,1,4]
print(insertionSort(arr))