n = int(input("enter dimension: "))
i = 1
x = 65
while(i <= n):
    j = 1
    while(j <= n):
        print(chr(x),end = " ")
        j = j+1
    print()
    i = i+1
    x = x+1
