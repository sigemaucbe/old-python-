#lj는 x로, nj는 y로
Word = input()
BeforeSwitch = ["c=","c-","dz=","d-","lj","nj","s=","z="] #배열
AfterSwitch = ["č","ć","d","đ","x","y","š","ž"] #배열
for r in range(8):
    Word = Word.replace(BeforeSwitch[r], AfterSwitch[r])
print(len(Word))