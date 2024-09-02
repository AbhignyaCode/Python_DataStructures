def convert(s, e, w):
    k = s
    cel = 0
    while( k <= e):
        cel = (k - 32) * (5/9)
        print(str(k) + " " + str(int(cel)))
        k = k+w

start =  int(input())
stop = int(input())
step = int(input())
table = convert(start, stop , step)
    
    