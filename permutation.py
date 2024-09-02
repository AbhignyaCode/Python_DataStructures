def checkperm(str1 , str2):
    if(len(str1) == len(str2)):
        count = 0
        for i in range (len(str1)):
            for j in range (len(str2)):
                if(str1[i] == str2[j]):
                    count = count+1
                    break
        if(count == len(str1)):
            return True
        else:
            return False 
    else:
        return False
    
str1 = "hello"
str2 = "llohe"
print(checkperm(str1,str2))
    
            


