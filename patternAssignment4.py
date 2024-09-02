n = int(input("enter dimension: "))
if(n == 1):
    print("1")
elif(n > 1):
    print("1")

    for k in range(1,n):
        print(k*(10**k)+k)
    print()
