def sort(arr):
    c0 = 0
    c1 = 0
    c2 = 0
    for i in range(len(arr)):
        if (arr[i] == 0):
            c0 = c0+1
        elif(arr[i] == 1):
            c1 = c1+1
        else:
            c2 = c2+1
    print("0" *c0 + "1"*c1 + "2"*c2)

arr = [1,2,1,0,0,1,2,0,0,2,2,1]
sort(arr)
    