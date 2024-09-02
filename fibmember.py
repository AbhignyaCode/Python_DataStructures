def checkMember(n):
#Implement Your Code Here
    fold = 0
    fnew = 1

    if(n == 0 or n == 1):
        return True

    while(n > fnew):
        temp = fnew
        fnew = fold + fnew
        if(n == fnew):
            return True
        fold = temp
    
    return False
        

        

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")

n = int(input())
checkMember(n)





    