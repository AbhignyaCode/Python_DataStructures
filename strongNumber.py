n = int(input("Enter your number: "))
temp = n
sum = 0
while(temp > 0):
    digit = temp%10
    fact = 1
    for k in range(1,digit+1):
        fact = fact*k
    sum = sum + fact
    temp = temp // 10
if(sum == n):
    print("This is a strong number")
else:
    print("this is not a strong number")