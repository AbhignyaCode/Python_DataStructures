n = int(input("enter dimension: "))
i = 1
while(i <= n):
    j = 1
    while(j <= n-i+1):
        print(j, end = " ")
        j = j+1
    print()
    i = i+1