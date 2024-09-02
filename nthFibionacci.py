n = int(input("enter number: "))
f1 = 1 
f2 = 1
if( n == 1 or n ==2 ):
    print("1")
else:
    i = 3
    while(i<=n): 
        ans = f1 + f2
        f1 = f2
        f2 = ans
        i = i + 1
print(ans)