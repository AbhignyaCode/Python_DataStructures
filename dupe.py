def first(arr,x):
    lower = 0
    upper = len(arr) - 1
    while(lower <= upper):
        mid = (lower+upper)//2
        if(arr[mid] == x):
            while(mid > 0):
                if(arr[mid-1] == x):
                    mid = mid-1
                return mid
        elif(x < arr[mid]):
            upper = mid -1
        else:
            lower = mid + 1
    return -1
    
def last(arr,x):
    lower = 0
    upper = len(arr) - 1
    while(lower <= upper):
        mid = (lower+upper)//2
        if(arr[mid] == x):
            while(mid < len(arr)):
                if(arr[mid+1] == x):
                    mid = mid + 1
                return mid
        elif (x < arr[mid]):
            upper = mid -1
        else:
            lower = mid + 1
    return -1

arr = [1,2,2,3,3,3,3,3,4,4,4]
x = 3
print("first : " ,first(arr,x))
print("last : " ,last(arr,x) )


        