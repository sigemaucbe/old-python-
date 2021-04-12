WordAmount = int(input())
WordList = [] 
UsedLetter = [] #이미 나온 글자를 저장
GroupWordCounter = WordAmount #그룹 글자 개수를 저장
for w in range(WordAmount):
    WordList.append(input())
for w in WordList: #Wordlist의 한 단어는 w
    UsedLetter.append(w[0]) #맨 첫글자는 바로 넣기
    for c in range(len(w)-1): #w의 글자 하나(마지막 글자는 비교 안하기)
        if w[c+1] in UsedLetter: #맨 앞자리 글자는 이미 UsedLetter에 넣었으므로 두번째 글자부터 비교하기
            if w[c+1] != w[c]:
                GroupWordCounter -= 1 #그룹단어가 아니면 GroupWordCounter에서 1 빼기
                break #다음 단어로 넘어가지 않고 한 단어에서 GroupWordCounter의 값이 여러번 줄어드는 걸 방지하기 위해서 break 사용
print(GroupWordCounter)