n = int(input("enter dimension: "))
i = 1
k = 65
while(i <= n):
    j = 1
    while(j <= i):
        print(chr(k),end = " ")
        j = j+1
    print()
    i = i+1
    k = k+1