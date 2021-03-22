# Find three numbers whose sum is equal to k


#debug not tight i j k must be diffrent


def sumk(lst, k):
    # Your code here
    m = dict()
    for i in range(lst.__len__()):
        m[lst[i]] = i
    for i in range(lst.__len__()):
        s1 = k - lst[i]
        for j in range(i+1, lst.__len__()):
            s2 = s1 - lst[j]
            if m.get(s2):
                    return [lst[i], lst[j], s2]


print(sumk([2, 4, 1, 7, -5], 15))  # -> [4,1,-5]