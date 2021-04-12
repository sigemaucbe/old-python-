n = int(input())
BunJa = 0 #분자의 값을 저장
BunMo = 0 #분모의 값을 저장
WhatNumber = 1 #분자랑 분모의 값을 계산할 때 쓰는 변수
a = 1 #몇번째 칸인지 나타내는 수
while n > WhatNumber:
    a += 1
    WhatNumber += a
NumberToSubtract = WhatNumber - a
n -= NumberToSubtract
#분자, 분모 구하는 식
if a%2 == 1: #n이 홀수일때
    BunJa = a + 1 - n
    BunMo = n
else: #n이 짝수일때
    BunJa = n
    BunMo = a + 1 - n
print(str(BunJa) + "/" + str(BunMo))