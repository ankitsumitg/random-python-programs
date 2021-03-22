def isValidSubsequence(array, sequence):
    # Write your code here.
    i = 0
    j = 0
    while i < len(array) and j < len(sequence):
        if sequence[j] == array[i]:
            j += 1
        i += 1
    return j == len(sequence)


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(isValidSubsequence(array, sequence))
