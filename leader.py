def leader(li):
    ptr = li[0]
    ptr_index = 0
    for i in range(1,len(li)):
        if(li[i] > li[ptr_index]):
            ptr_index = i
            ptr = li[ptr_index]
    count = 0
    for k in range(ptr_index , len(li)):
        if(li[k] < ptr):
            count = count+1
    if(count == len(li) - ptr_index - 1):
        return (ptr, li[len(li)-1])

li = str(input())
li = int(str.split())
print(leader(li))