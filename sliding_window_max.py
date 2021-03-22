nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]
k = 3
res = []
decq = []
for i in range(k):
    while decq and nums[i] > decq[-1]:
        decq.pop()
    decq.append(nums[i])
res.append(decq[0])
for i in range(len(nums) - k):
    while decq and nums[i + k] > decq[-1]:
        decq.pop()
    decq.append(nums[i + k])
    if decq[0] == nums[i]:
        decq.pop(0)
    res.append(decq[0])
print(res)