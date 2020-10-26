a = int(input())
b = int(input())
c = int(input())
if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    print('NO')
elif not a % 2 == 0 and not b % 2 == 0 and not c % 2 == 0:
    print('NO')
else:
    print('YES')
