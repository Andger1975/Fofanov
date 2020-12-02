k = -1
owerK = k
sumK = 0
nowK = 0
while k != 0:
    k = int(input())
    if k == owerK:
        nowK += 1
    elif k != owerK:
        owerK = k
        if nowK > sumK:
            sumK = nowK
            nowK = 1
        else:
            nowK = 1
print(sumK)
