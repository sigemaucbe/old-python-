import math
m = int(input())
n = int(input())
PrimeList = []
for i in range(m,n+1):
    PrimeYes = True
    r = math.sqrt(i)
    r = math.ceil(r)
    if i == 1 or i == 4:
        PrimeYes = False
    if i == 2:
        PrimeList.append(2)
        continue
    for j in range(2,r+1):
        if i%j == 0:
            PrimeYes = False
            break
    if PrimeYes == True:
        PrimeList.append(i)
if len(PrimeList) <= 0:
    print("-1")
else:
    hap = 0
    for i in PrimeList:
        hap = hap + i
    print(hap)
    print(min(PrimeList))