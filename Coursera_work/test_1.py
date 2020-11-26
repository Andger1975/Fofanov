xElement = -1
digital = xElement
i = 0
while xElement != 0:
    xElement = int(input())
    if digital < xElement:
        i = digital
        digital = xElement
    elif xElement != 0 and i < xElement:
        i = xElement
print(i)
