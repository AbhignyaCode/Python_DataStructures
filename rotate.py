def rotate(arr,d):
        k = 0
        while(k < d):
            temp = arr[k]
            arr.append(temp)
            k = k+1
        n = 0
        while(n < d):
              arr.pop(0)
              n = n+1
              
        return arr

arr = [1,2,3,4,5,6]
d = 2
print(rotate(arr,d))

#DOUBT
