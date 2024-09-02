def swap(li):

    for i in range(0 , len(li) - 1 , 2):
        li[i] , li[i+1] = li[i+1], li[i]
    print(li)

n = int(input())
if(n == 1):
    print("")
else:
    li = [int(x) for x in input().split()]
    swap(li) 



