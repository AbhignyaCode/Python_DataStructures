n = int(input("enter your number: "))
temp = n
sumEven = 0
sumOdd = 0
while(temp > 0):
    digit = temp%10
    temp = temp//10
    if(digit % 2 == 0):
        sumEven = sumEven + digit
    if(digit % 2 != 0):
        sumOdd = sumOdd + digit
print("sum of even digits: ",sumEven)
print("sum of odd digits: ",sumOdd)

