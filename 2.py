def ninjaPuzzle(n):
 i = 1
 while( i <= n):
    j = 1
    while( j<= i-1):
        print(" ", end= "")
        j = j+1
    k = 1
    while(k <=n-i+1):
        print("*" , end= "")
        k = k+1
    print()
    i = i+1

n1 = int(input("how many tc"))
for x in range(1 , n1+1):
    t = int(input("enter tc"))
    ninjaPuzzle(t)
