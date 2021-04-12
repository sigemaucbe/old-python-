x = int(input())
y = int(input())
z = int(input())
numlist = [0,0,0,0,0,0,0,0,0,0]
n = x*y*z
# 변수 o는 임시로 저장하는 변수
o = 0
while n != 0:
    o = n%10
    numlist[o] += 1
    n = n//10
for i in range(10):
    print(numlist[i])