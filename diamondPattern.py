n = int(input("enter dimension:"))
i = 1
while(i <= (n//2)+1):
    j = 1
    while( j <= (n//2) -i+1):
        print(" " , end="")
        j = j+1
    k = 1
    while(k <= i):
        print("*" , end="")
        k = k+1
    l = 1
    while(l <= i-1):
        print("*" , end="")
        l = l+1
    print()
    i = i+1
ii = 1
while(ii <= n//2):
    m = 1
    while(m <= ii):
        print(" ", end="")
        m = m+1
    o = 1
    while(o <= (n//2) -ii+1):
        print("*" , end="")
        o = o+1
    p = 1
    while(p <= (n//2)-ii):
        print("*", end="")
        p = p+1
    print()
    ii = ii+1

    


