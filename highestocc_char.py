def highfreq(str):
    arr =[0]*256
    for i in range(len(str)):
        index = ord(str[i])
        arr[index] = arr[index] + 1
    max = arr[0]

    for k in range(len(arr)):
        if(arr[k] > max):
            max = arr[k]
            maxindex = k
    return chr(maxindex)

str = str(input("enter string : "))
print(highfreq(str))
