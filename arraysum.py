def sum(arr):
    num = 0
    i = 0
    while(i < len(arr)):
        dig = arr[i]
        num = num*10 + dig
        i = i+1
    return num

def sumarray(arr1,arr2):
    num1 = sum(arr1)
    num2 = sum(arr2)
    print(num1+num2)

arr1 = [9,9,8]
arr2 = [2,8,6]
sumarray(arr1,arr2)
    


