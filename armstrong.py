def checkArmstrong(n):
    m = n
    arm = 0
    count = 0
    while(n > 0):
        k = n%10
        if(k != 0):
            count+=1
            n= n//10
    while(m > 0):
        digit = m %10
        arm = arm + digit**3
        m = m//10
    return arm

n = int(input("enter n : "))
if(n == checkArmstrong(n)):
    print("true")
else:
    print("false")
       

