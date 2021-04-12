import math
#손익분기점이 발생할려면 a + b(판매량) < c(판매량) a/(c-b)
a,b,c = input().split(" ")
a = int(a) #기본적으로 드는 돈
b = int(b) #재료비
c = int(c) #판매량
if (c-b) <= 0:
    print("-1")
else:
    SellAmount = a/(c-b)
    if int(SellAmount) == SellAmount:
        SellAmount += 1
    print(math.ceil(SellAmount))