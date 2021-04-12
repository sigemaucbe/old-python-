sentencenumber = int(input())
for a in range(sentencenumber):
    scorelist = []
    scorelist = input().split(" ")
    scoresum = 0
    average = 0
    averagenum = 0
    upnumber = 0
    overaverageratio = 0
    for i in range(len(scorelist)-1):
        scorelist[i+1] = int(scorelist[i+1])
        scoresum += scorelist[i+1]
    average = scoresum/(len(scorelist)-1)
    for i in range(len(scorelist)-1):
        if scorelist[i+1] > average:
            averagenum += 1
    finaloutput = (averagenum/(len(scorelist)-1))*100
    overaverageratio = round(finaloutput,3)
    print(("{0:.3f}".format(overaverageratio)) + "%")