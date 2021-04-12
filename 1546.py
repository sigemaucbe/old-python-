a = int(input())
num = []
num = input().split(" ")
sum = 0
for i in range(a):
    num[i] = int(num[i])
max = num[0]
for x in range(a-1):
    if max < num[x+1]:
        max = num[x+1]
for i in range(a):
    num[i] = num[i]/max * 100
for i in range(a):
    sum += num[i]
print(sum/a)