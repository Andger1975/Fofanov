k, m, n = int(input()), int(input()), int(input())
if n <= k:
    minT = 2 * m
elif n * 2 % k == 0:
    minT = m * (n * 2 // k)
else:
    minT = m * (1 + (n * 2 // k))
print(minT)
