def sortZeroesAndOne(arr) :
    #Your code goes here 
    c1 = 0
    c2 = 0
    for i in range(len(arr)):
        if(arr[i] == 0):
            c1 = c1+1
        elif(arr[i] == 1):
            c2 = c2+1
    for k in range(c1):
        print("0" , end = " ")
    for k in range (c2):
        print("1" , end = " ")
   
    
arr = [1,0,1,0,0,1,0,1,1,1]
sortZeroesAndOne(arr)



