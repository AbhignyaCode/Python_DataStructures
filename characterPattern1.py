n = int(input("enter dimension: "))
i = 1
while(i <= n):
    j = 1
    x = 65
    while(j <= n):
        print(chr(x), end = " ") 
        x = x+1
        j = j+1
    print()
    i = i+1
