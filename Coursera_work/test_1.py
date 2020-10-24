x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 > 8 or y1 > 8 or x2 > 8 or y2 > 8 \
        or x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
    print('NO')
else:
    if (x1 + x2) % 2 == (y1 + y2) % 2 and y2 > y1:
        print('YES')
    else:
        print("NO")
