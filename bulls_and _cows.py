from collections import defaultdict


def getHint(secret: str, guess: str):
    B, C = 0, 0
    sDic = defaultdict(int)
    gDic = defaultdict(int)

    for s, g in zip(secret, guess):
        if s == g:
            B += 1
        else:
            sDic[s] += 1
            gDic[g] += 1

    for i in gDic:
        if i in sDic:
            C += min(sDic[i], gDic[i])

    return [B, C]


n = int(input())
d = {str(i): 0 for i in range(1, 10)}
arr = []
for i in range(n):
    inputs = input().split()
    guess = inputs[0]
    bulls = int(inputs[1])
    cows = int(inputs[2])
    arr.append([guess, bulls, cows])
for i in range(10000):
    s = str(i)
    s = '0' * (4 - len(s)) + s
    k = 0
    for g, b, c in arr:
        bb, cc = getHint(s, g)
        if bb == b and cc == c:
            k += 1
    if k == len(arr):
        print(s)
        exit()
