def findGcd(x, y):

    i = 1
    gcd = 1

    while (i <= x and i <= y):
        if (x % i == 0 and y % i == 0):
            gcd = i
        i = i+1

    return gcd

x  = int(input("enter 1st num"))
y = int(input("enter 2nd num"))
print(findGcd(x,y))
