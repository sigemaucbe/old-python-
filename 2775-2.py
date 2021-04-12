import math
n = int(input())
for i in range(n):
    h = int(input())+1 #사각형의 가로
    v = int(input())-1 #사각형의 세로
    print(int(math.factorial(h+v)/(math.factorial(h)*math.factorial(v))))