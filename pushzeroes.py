def pushZerosAtEnd(arr) :
    count = 0
    array =[]
    for i in range(len(arr)):
        if(arr[i] == 0):
            count = count+1
    
    for k in range (len(arr)):
        if(arr[k] != 0):
                array.append(arr[k])
    for m in range (count):
                array.append("0")
    return array

arr = [5,0,7,4,8,1,3,0,7,2,0 ]
print(pushZerosAtEnd(arr))