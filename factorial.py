for n in range(1,11):
    fact = 1
    for j in range (1,n+1):
     fact = fact*j
     j = j+1
    print(n, fact)