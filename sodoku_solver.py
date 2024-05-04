""" 
test
"""


def full_grid_check(grid, row, col):  # ? for full board solve

    s = set(
        {
            grid[row][col],
            grid[row + 1][col],
            grid[row + 1][col + 1],
            grid[row + 1][col - 1],
            grid[row - 1][col - 1],
            grid[row - 1][col + 1],
            grid[row - 1][col],
            grid[row][col + 1],
            grid[row][col - 1],
        }
    )

    return len(s) == len(grid[0])


def test_case_grid_check(grid, row, col):
    """t"""

    arr = [
        grid[row][col],
        grid[row + 1][col + 1],
        grid[row - 1][col - 1],
        grid[row][col + 1],
        grid[row][col - 1],
        grid[row + 1][col],
        grid[row - 1][col],
        grid[row - 1][col + 1],
        grid[row + 1][col - 1],
    ]

    dict = {}
    for i in arr:

        if i != "." and i in dict:
            return False

        dict[i] = 1 + dict.get(i, 0)

    return True


def check_col(grid, col):
    """t"""

    dict = {}
    for i in range(len(grid)):

        if grid[i][col] != "." and grid[i][col] in dict:
            return False

        dict[(grid[i][col])] = 1 + dict.get(grid[i][col], 0)

    return True


def check_row(grid, row):
    """t"""

    dict = {}
    for i in grid[row]:

        if i != "." and i in dict:
            return False

        dict[i] = 1 + dict.get(i, 0)

    return True


def axises(grid, row, col):
    if row >= len(grid[0]) or col >= len(grid[0]):
        return True

    r = check_row(grid, row)
    c = check_col(grid, col)

    # r = True if len(set(grid[row])) == grid[0] else False #? for solving a full sudoku grid
    # c = True if len(set([rr[col] for rr in grid])) == grid[0] else False #? for solving a full sudoku grid

    if r and c:
        return axises(grid, row + 1, col + 1)

    return False


def grids(grid):
    mid = len(grid[0]) // 2

    res = (
        test_case_grid_check(grid, mid, mid)
        & test_case_grid_check(grid, mid + 3, mid + 3)
        & test_case_grid_check(grid, mid - 3, mid - 3)
        & test_case_grid_check(grid, mid, mid + 3)
        & test_case_grid_check(grid, mid, mid - 3)
        & test_case_grid_check(grid, mid + 3, mid)
        & test_case_grid_check(grid, mid - 3, mid)
        & test_case_grid_check(grid, mid - 3, mid + 3)
        & test_case_grid_check(grid, mid + 3, mid - 3)
    )

    return res


def solve(grid):
    """t"""

    return axises(grid, 0, 0) and grids(grid)


def main():

    grid = []

    grid = list(map(str, input().split()))

    print(solve(grid))


if __name__ == "__main__":
    main()

""" 
87654321 2........ 3........ 4........ 5........ 6........ 7........ 1........ 9........

534678912 672195348 198342567 859761423 426853791 713924856 961537284 287419635 345286179

....5..1. .4.3..... .....3..1 8......2. ..2.7.... .15...... .....2... .2.9..... ..4......
"""
