def reverse(n):
    rev = 0
    while(n > 0):
        temp = n%10
        rev = rev*10 + temp
        n = n//10
    return rev
 
m = int(input())
if( m <= 9):
     print("true")
else:
    reverse(m)
    if(reverse(m) == m):
        print("true")
    else:
        print("false")

