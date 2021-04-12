amount = int(input())
for a in range(amount):
    ox = input()
    ox = (ox + "X")
    onum = 0
    score = 0
    for i in range(len(ox)):
        if ox[i] == "O":
            onum += 1
        if ox[i] == "X":
            for s in range(onum):
                score += onum
                onum -= 1
            onum = 0
    print(score)