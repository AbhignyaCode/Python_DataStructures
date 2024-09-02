def unique(li):
    for i in range(len(li)):
        isUnique = True  
        for j in range(len(li)):
            if i != j and li[i] == li[j]:
                isUnique = False
                break
        if isUnique:
            return li[i]
    return None  

li = [1, 2, 3, 5, 3, 2, 1]
print(unique(li))
