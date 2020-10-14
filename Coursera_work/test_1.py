A = int(input())
B = int(input())
rev_1 = 0 ** (B // (A + 1)) * A
rev_2 = 0 ** (A // B) * B
print(rev_1 + rev_2)
