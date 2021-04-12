amount = int(input())
for a in range(amount):
    inputt = input().split(" ")
    for i in range(len(inputt[1])):
        for j in range(int(inputt[0])):
            print(inputt[1][i],end="")
    print("")