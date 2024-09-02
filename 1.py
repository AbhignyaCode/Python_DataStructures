n = int(input())
i = 1
while(i <= n):
    j = 1
    while( j <= n-i+1):
        if(j == n-i+1):
            print("*" , end= "")
        else:
            print(n-j+1, end = "")
        j = j+1
    k  = 1
    while(k <= i-1):
        r = i-1
        while(r >= 1):
          print(r , end= "")
          r = r -1
          k = k+1
    print()
    i = i+1


    