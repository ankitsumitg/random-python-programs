def travel(mat, vis, i, j):
    val = 0
    if i + 1 < len(mat) and mat[i + 1][j] == 1 and vis[i + 1][j] == 0:
        vis[i + 1][j] = 1
        val = val + 1 + travel(mat, vis, i + 1, j)
    if i - 1 >= 0 and mat[i - 1][j] == 1 and vis[i - 1][j] == 0:
        vis[i - 1][j] = 1
        val = val + 1 + travel(mat, vis, i - 1, j)
    if j + 1 < len(mat[0]) and mat[i][j + 1] == 1 and vis[i][j + 1] == 0:
        vis[i][j + 1] = 1
        val = val + 1 + travel(mat, vis, i, j + 1)
    if j - 1 >= 0 and mat[i][j - 1] == 1 and vis[i][j - 1] == 0:
        vis[i][j - 1] = 1
        val = val + 1 + travel(mat, vis, i, j - 1)
    return val


def riverSizes(matrix):
    # Write your code here.
    w = len(matrix)
    h = len(matrix[0])
    vis = [[0 for j in range(h)] for i in range(w)]
    ans = list()
    for i in range(w):
        for j in range(h):
            if (matrix[i][j] == 1) and vis[i][j] == 0:
                vis[i][j] = 1
                ans.append(travel(matrix, vis, i, j) + 1)
    return ans


testInput = [
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 0, 0],
    [0, 0, 0],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 1]
]
expected = [[10, 1, 1, 2, 6]]
print(riverSizes(testInput))
