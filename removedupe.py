def removeConsecutiveDuplicates(string) :
    ans = string[0]
    for i in range(1,len(string)):
        if(string[i] != string[i-1]):
            ans = ans + string[i]
    return ans

string = str(input("enter i/p string : "))
print(removeConsecutiveDuplicates(string))
        

