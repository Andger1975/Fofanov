n = int(input())
ost = n % 10
if 10 <= n <= 20 or ost >= 5 or ost == 0:
    print(n, 'korov')
elif n % 10 == 1:
    print(n, 'korova')
else:
    print(n, 'korovy')
