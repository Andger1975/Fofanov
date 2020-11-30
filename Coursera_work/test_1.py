K = int(input())
number = K
counterNumber = 0
Flip = 0
while K != 0:
    while number > 0:
        Flip = Flip * 10 + number % 10
        number //= 10
    if Flip == K:
        counterNumber += 1
    Flip = 0
    K -= 1
    number = K
print(counterNumber)
