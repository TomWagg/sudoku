import numpy as np


def grid_is_valid(grid, verbose=False):
    # check whether a sudoku grid is valid
    if not has_valid_rows(grid):
        print("A row has a repeated entry")
        return False
    if not has_valid_rows(grid.T):
        print("A column has a repeated entry")
        return False
    if not has_valid_boxes(grid):
        print("A box has a repeated entry")
        return False


def has_valid_boxes(grid):
    return True


def has_valid_rows(grid):
    for row in grid:
        # print(row)
        if any(row) > 0:
            uniques, counts = np.unique(row[row > 0], return_counts=True)
            if any(counts > 1):
                return False
    return True


def generate_grid(n_filled):
    # create a blank sudoku grid
    grid = np.zeros(shape=(9, 9)).astype(int)

    # pick some random indices and convert them into rows and columns
    indices = np.random.choice(81, n_filled, replace=False)
    rows = indices // 9
    columns = indices % 9

    # choose some random entries for those rows and columns
    entries = np.random.randint(1, 10, n_filled)

    # populate grid with random entries
    grid[rows, columns] = entries
    return grid


def print_grid(grid):
    """Print out a sudoku grid

    Parameters
    ----------
    grid : `list` of `lists`
        9x9 grid of sudoku entries
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end=" ")
            if (j - 2) % 3 == 0 and j < 8:
                print("|", end=" ")
        print()
        if (i - 2) % 3 == 0 and i < 8:
            print(*["-" for _ in range(9 + 2)], end=" ")
            print()


grid = generate_grid(20)
print_grid(grid)
print(grid_is_valid(grid))
