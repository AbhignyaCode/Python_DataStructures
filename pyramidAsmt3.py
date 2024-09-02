n = int(input())
i = 1
while(i <= n):
    j = 1
    while(j <= n-i):
        print(" ", end="")
        j =j+1
    k =i 
    while(k >= 1):
        print(k, end="")
        k = k-1
    l = 1
    while(l <= i-1):
        print(l+1, end = "")
        l = l+1
    print()
    i = i+1