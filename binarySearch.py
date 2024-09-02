def binarySearch(arr,x):
    si = 0
    ei = len(arr) - 1
    while(si <= ei):
        mid = (si + ei)//2
        if(arr[mid] == x):
            return mid
        elif(x > arr[mid]):
            si = mid + 1
        else:
            ei = mid - 1
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
x = 7
print(binarySearch(arr,x))