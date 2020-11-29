N1 = int(input())
N2 = 0
while N1 > 0:
    digit = N1 % 10
    N1 = N1 // 10
    N2 = N2 * 10
    N2 = N2 + digit
print(N2)
