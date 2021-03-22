n = int(input())
for i in range(n):
    b, k = input().split()
    b = list(b)
    k = int(k)
    n = len(b) - k
    flips = 0
    i = 0
    while i<= n:
        if b[ i ] == '0':
            for j in range(i,k+i):
                if b[ j ] == '0':
                    b[ j ] = '1'
                else:
                    b[ j ] = '0'
            flips += 1
        i += 1
    while i < len(b):
        if b[ i ] == '0':
            flips = -1
        i += 1
    print(flips)


