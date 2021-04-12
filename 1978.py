PrimeAmount = 0
ThisIsUselessLol = int(input())
numbers = input().split(" ")
for r in range(len(numbers)):
    numbers[r] = int(numbers[r])
for n in numbers:
    ron = int(n ** 0.5)
    IsPrime = True
    if n == 1:
        IsPrime = False
    for i in range(2, ron+1):
        if n%i == 0:
            IsPrime = False
    if IsPrime == True or n == 2:
        PrimeAmount += 1
print(PrimeAmount)