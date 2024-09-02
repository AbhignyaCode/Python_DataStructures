def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if(arr[j] < arr[min]):
                min = j
        (arr[i] , arr[min]) = (arr[min] ,arr[i])
    return arr




arr = [5,8,2,7,11,5]
print(selectionSort(arr))