Sentence = input()
WordAmount = 0
Itsblank = True
for i in range(1,(len(Sentence)-1)):
    if (Sentence[i] == " " and Sentence[i-1] != " ") and Sentence[i+1] != " ":
        WordAmount += 1
for i in range(len(Sentence)):
    if Sentence[i] != " ":
        Itsblank = False
if Itsblank == True:
    print(0)
else:
    print(WordAmount+1)