n = int(input())
i = 1
while(i <= n):
    j =1
    while(j <= i):
        if(j == i):
            print("*" , end = "")
        else:
            print("0", end= "")
        j = j+1
    k = 1
    while(k <= n-i):
        print("0", end="")
        k = k+1
    l = 1
    while(l <= n-i+1):
        if(l == 1):
            print("*", end = "")
        else:
            print("0", end="")
        l = l+1
    m = 1
    while( m <= i):
        if(m == 1):
            print("*", end="")
        else:
            print("0", end = "")
        m = m+1
    print()
    i = i+1
        
        

