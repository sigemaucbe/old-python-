numlist = input().split(" ")
changednumlist = []
for i in range(2):
    changednumlist.append(int(numlist[i][2]+numlist[i][1]+numlist[i][0]))
changednumlist.sort()
print(changednumlist[1])