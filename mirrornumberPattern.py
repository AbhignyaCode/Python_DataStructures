n = int(input())

i = 1

while(i<=n):
    spaces = n-i
    j = 1
    while(j<=spaces):
        print(" ",end = '')
        j = j+1
    k = 1
    while(j<=n):
        print(k, end = '')
        k = k+1
        j = j+1
    print()
    i = i+1
