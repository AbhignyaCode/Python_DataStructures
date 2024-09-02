n = int(input("enter number: "))
i = 1 
while(i <= n):
    j = 1
    while(j <= i):
        print(i+j-1, end = " ")
        j = j+1
    print()
    i = i+1
    