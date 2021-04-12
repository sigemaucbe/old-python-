alphabetinput = input()
summ = 0
for i in range(len(alphabetinput)):
    if (alphabetinput[i] == "A" or alphabetinput[i] == "B") or alphabetinput[i] == "C":
        summ += 3
    elif (alphabetinput[i] == "D" or alphabetinput[i] == "E") or alphabetinput[i] == "F":
        summ += 4
    elif (alphabetinput[i] == "G" or alphabetinput[i] == "H") or alphabetinput[i] == "I":
        summ += 5
    elif (alphabetinput[i] == "J" or alphabetinput[i] == "K") or alphabetinput[i] == "L":
        summ += 6
    elif (alphabetinput[i] == "M" or alphabetinput[i] == "N") or alphabetinput[i] == "O":
        summ += 7
    elif (alphabetinput[i] == "P" or alphabetinput[i] == "Q") or (alphabetinput[i] == "R" or alphabetinput[i] == "S"):
        summ += 8
    elif (alphabetinput[i] == "T" or alphabetinput[i] == "U") or alphabetinput[i] == "V":
        summ += 9
    elif (alphabetinput[i] == "W" or alphabetinput[i] == "X") or (alphabetinput[i] == "Y" or alphabetinput[i] == "Z"):
        summ += 10
print(summ)