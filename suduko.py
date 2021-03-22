# type hex okay okay
# lets start
def findNextCellToFill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y

    # so here there will be one more scenario
    # what if there are no 0 left starting from i,j
    # again we will check from starting onwards for Zeros
    # not from i,j Since we were filling it back with 0 during back tracking if e is notValid
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y

    # if still no zeroes sudoko is solved
    return -1, -1


def isValid(grid, i, j, e):
    # this is the tricy part try to understand
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        # similarly for columns
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            # now we will find where does i,j lies in which sectro
            secTopX = 3 * (i // 3)
            secTopY = 3 * (j // 3)
            for x in range(secTopX, secTopX + 3):
                for y in range(secTopY, secTopY + 3):
                    if grid[x][y] == e:
                        return False

            # other wise True
            return True
    # if row or col not okay
    return False


# back to solve

def solveSudoko(grid, i=0, j=0):
    # starting index 0,0
    # lets find 1st suitable position
    i, j = findNextCellToFill(grid, i, j)
    if i == -1:
        return True
    # now lets fill the solveSudoko
    for e in range(1, 10):
        # lets check whether the e selected is valid to fill or not
        if isValid(grid, i, j, e):
            grid[i][j] = e
            # now lets use recursion and again call the same method
            # if sudoko is solved totally
            if solveSudoko(grid, i, j):
                return True
            # else i,j is invalidand agin fill it with 0

            grid[i][j] = 0

    # return false if sudoko is not solvable, wrong input
    return False


grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]

solveSudoko(grid)

for i in grid:
    print(i)
solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]
