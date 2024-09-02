n = int(input("enter dimension: "))
if (n == 1):
    print("1")
elif(n > 1):
    print("1")
    for i in range(2,n+1):
        print("1", end="")
        for k in range (1,i-1):
            print("2", end = "")
        print("1", end = "")
        print()
