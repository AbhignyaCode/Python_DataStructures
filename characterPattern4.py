n = int(input("enter dimension: "))
i = 1
x = 64
while ( i <= n):
    j = 1
    while (j <= i):
        print(chr(x+i+j-1) , end= " ")
        j = j+1
    print()
    i = i+1
    
