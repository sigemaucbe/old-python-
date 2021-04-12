word = input()
wordlist = []
samecounter = []
max = 0
mostusedletter = 0
for i in range(len(word)):
    wordlist.append(ord(word[i]))
    if wordlist[i] >= 97:
        wordlist[i] -= 32
for i in range(26):
    samecounter.append(0)
for i in wordlist:
    samecounter[i - 65] += 1
for i in range(26):
    if max < samecounter[i]:
        max = samecounter[i]
        mostusedletter = i
samecounter.sort(reverse=True)
if samecounter[0] == samecounter[1]:
    print("?")
else:
    print(chr(mostusedletter+65))