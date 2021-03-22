arr = [0]*10001
n = int(input())
assert 1<= n <= 10**5
inp = list(map(int,input().split()))
for i in inp:
    arr[i]+=1
    assert(0 <= i<= 10**4)
i = 0
count = 0
while (i < len(arr)):
    if arr[i]>0:
        count+=1
        i+=4
    i+=1
print (count)
