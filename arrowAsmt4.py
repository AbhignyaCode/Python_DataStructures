n = int(input())
i = 1
while i <= n//2:
    print(" " * (i - 1) + "* " * i)
    i = i+ 1
i = (n//2) + 1
while i >= 1:
    print(" " * (i - 1) + "* " * i)
    i =i- 1

