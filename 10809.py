alphabetlist = []
ascii = 0 
for i in range(26):
    alphabetlist.append(-1)
word = input()
for i in range(len(word)):
    ascii = ord(word[i])-97
    if alphabetlist[ascii] == -1:
        alphabetlist[ascii] = i
for i in range(26):
    print(alphabetlist[i],end = " ")