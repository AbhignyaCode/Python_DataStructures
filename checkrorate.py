def check(arr):
    min = arr[0]
    min_i = 0
    for i in range(len(arr)):
        if(arr[i] < min):
            min = arr[i]
            min_i = i      
    return min_i  

arr = [5,6,1,2,3,4]
print(check(arr))

