def find_first_x(coeffs, limit):
    size = len(coeffs)
    if size <= 1:
        return -1
    if coeffs[0] > limit:
        return 0
    val = 1
    ans = 0
    while True:
        for i in range(0, len(coeffs)):
            ans = ans + coeffs[i] * (val ** i)
        if ans > limit:
            return val
        ans = 0
        val = val + 1


print(find_first_x([1, 2, 3], 20))

print(find_first_x([2,5],50)) # 10
print(find_first_x([2],50) )# -1
print(find_first_x([0,3,5,7],500) )# 4
print(find_first_x([25,10,5,2,1],99999) )# 18
