from collections import Counter


def sherlockAndAnagrams(s):
    n = len(s)
    i = 1
    l = list()
    while i < n:
        j = 0
        while j + i <= n:
            l.append(''.join(sorted(s[j:j + i])))
            j += 1
        i += 1
    ans = Counter()
    for i in l:
        ans[i] += 1
    final = 0
    for k in ans:
        if ans[k] >= 2:
            final += sum(range(ans[k]))
    return final


print(sherlockAndAnagrams('cdcd'))
