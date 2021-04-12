import math
a,b,v = input().split(" ")
a = int(a) #낮에 올라간 거리
b = int(b) #밤에 떨어진 거리
v = int(v) #올라가야 하는 거리
m = 0
m = (v-a)/(a-b)
print(math.ceil(m)+1)