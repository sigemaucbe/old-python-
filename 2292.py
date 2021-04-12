Number = int(input())
HiveWhatDonut = 1 #벌집의 몇번째 고리에 있는지에 관한 변수
OneByOne = 1 #반복할때마다 1씩 커지는 수
while Number > HiveWhatDonut:
    HiveWhatDonut += 6*OneByOne
    OneByOne += 1
print(OneByOne)