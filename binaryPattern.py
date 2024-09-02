n = int(input("enter dimension: "))
i = n
count = 1
while(i >= 1):
    j = 1
    while(j <= i):
        if(count % 2 == 0):
         print("0", end = " ")
         j = j+1

        else:
           print("1", end = " ")
           j = j+1

    print()
    i = i-1
    count = count+1