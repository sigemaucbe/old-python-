numlist = [0,0,0,0,0,0,0,0,0,0]
calculation = []
for i in range(10):
    numlist[i] = int(input())%42
for a in numlist:
    zungbok = False
    for b in calculation:
        if a == b:
            zungbok = True
    if zungbok == False:
        calculation.append(a)
print(len(calculation))