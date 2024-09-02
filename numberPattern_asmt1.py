n = int(input())
i = 1
while(i <= n):
    j = 1
    while(j <= i):
        print(j, end="")
        j = j+1
    k = 1
    while(k <= n-i):
        print(" ", end="")
        k = k+1
    l = 1
    while(l <= n-i):
        print(" ", end="")
        l = l+1
    m = i
    while(m >= 1):
        print(m, end = "")
        m = m-1
    print()
    i = i+1
    