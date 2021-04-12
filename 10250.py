a = int(input())
for i in range(a):  
    h,w,n = input().split(" ")
    h = int(h)
    w = int(w)
    n = int(n)
    y = n%h
    if y == 0:
        y = h
    x = n//h
    if n%h != 0:
        x += 1
    if x < 10:
        x = str(x)
        y = str(y)
        print(y+"0"+x)
    else:
        x = str(x)
        y = str(y)
        print(y+x)