EnterContestAmount = int(input()) #대회에 참가한 횟수
Contest2017Winner = [ [1] , [2,3] , [4,5,6] , [7,8,9,10] , [11,12,13,14,15] , [16,17,18,19,20,21] ] #2017년 대회 순위   
Contest2018Winner = [ [1] , [2,3] , [4,5,6,7] , [8,9,10,11,12,13,14,15] , [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]] #2018년 대회 순위
Contest2017Prize = [5000000 , 3000000 , 2000000 , 500000 , 300000 , 100000]
Contest2018Prize = [5120000 , 2560000 , 1280000 , 640000 , 320000]
for w in range(EnterContestAmount): #첫번째 대회랑 두번째 대회에서 몇번째로 잘했는지 EnterContestAmount만큼 입력
    aMoney = 0
    bMoney = 0
    a,b = input().split(" ")
    a = int(a)
    b = int(b) 
    for s17 in Contest2017Winner: #Contest2017Winner에서 변수 하나씩 가져오기
        if a in s17:
            a = Contest2017Winner.index(s17)
            aMoney = Contest2017Prize[a]
    for s18 in Contest2018Winner: #Contest2018Winner에서 변수 하나씩 가져오기
        if b in s18:
            b = Contest2018Winner.index(s18)
            bMoney = Contest2018Prize[b]
    print(aMoney+bMoney)