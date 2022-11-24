import numpy as np


def grid_is_valid(grid):
    # check whether a sudoku grid is valid
    raise NotImplementedError


def generate_grid(n_filled):
    # create a valid sudoku grid

    grid = np.array([[0 for i in range(9)] for j in range(9)])

    indices = np.random.choice(81, n_filled, replace=False)

    print(indices)
    rows = indices // 9
    columns = indices % 9

    entries = np.random.randint(1, 10, n_filled)

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


print_grid(generate_grid(20))
