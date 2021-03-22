def threesum(lst,k):
    lst.sort()
    ans = 0
    n = len(lst)
    diff = 100000
    for i in range(0,n):
        l = i+1
        r = n-1
        while(l<r):
            t = lst[l]+lst[i]+lst[r]
            if abs(t-k)<diff:
                diff = abs(t-k)
                ans = t
            if t == k:
                return t
            if t > k:
                r -= 1
            else:
                l += 1
    return ans

print(threesum([-1,2,1,-4],1))