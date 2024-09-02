def rotate(arr,d):
    rot_arr = arr[d:] + arr[:d] 
    return rot_arr

arr = [1,2,3,4,5,6]
d = 2
print(rotate(arr,d))
 
    
  
   