Sugar = int(input())
s = 0 #3kg짜리 봉지 개수
o = 0 #5kg짜리 봉지 개수
while (Sugar-(3*s))%5 != 0:
    s += 1
o = (Sugar-(3*s))//5
if Sugar == 4 or Sugar == 7:
    print("-1")
else:
    print(s+o)