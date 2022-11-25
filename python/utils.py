import numpy as np

from validate import grid_is_valid


def generate_valid_grid(n_filled, print_attempts=False):
    i = 1
    grid = generate_grid(n_filled=n_filled)
    while not grid_is_valid(grid):
        grid = generate_grid(n_filled=n_filled)
        i += 1

    if print_attempts:
        print(f"Required {i} attempts to get a valid grid")

    return grid


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
