def twoSum( nums, target: int):
    d = dict()
    d[nums[0]] = 0
    for i in range(1, len(nums)):
        if d.get(target - nums[i]):
            return [d[target - nums[i]], i]
        d[nums[i]] = i
print(twoSum([3,2,4],6))
