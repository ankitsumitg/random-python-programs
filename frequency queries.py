from collections import Counter


def freqQuery(queries):
    freq = Counter()
    cnt = Counter()
    arr = []
    for q in queries:
        if q[0] == 1:
            cnt[freq[q[1]]] -= 1
            freq[q[1]] += 1
            cnt[freq[q[1]]] += 1
        elif q[0] == 2:
            if freq[q[1]] > 0:
                cnt[freq[q[1]]] -= 1
                freq[q[1]] -= 1
                cnt[freq[q[1]]] += 1
        else:
            if cnt[q[1]] > 0:
                arr.append(1)
            else:
                arr.append(0)
    return arr


queries = [
[1, 5],
[1 ,6],
[3 ,2],
[1 ,10],
[1 ,10],
[1, 6],
[2 ,5],
[3 ,2]]
print(freqQuery(queries))