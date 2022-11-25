import numpy as np

from validate import grid_is_valid


def ind2row_col(ind):
    return ind // 9, ind % 9


def generate_valid_grid(n_filled, print_attempts=False):
    """Generate a *valid* sudoku grid

    Parameters
    ----------
    n_filled : `int`
        How many entries to fill
    print_attempts : `bool`, optional
        Whether to print how many attempts this required, by default False

    Returns
    -------
    valid_grid : `list` of `lists`
        9x9 grid of sudoku entries
    """
    # randomly generate grids until you find one that works
    i = 1
    grid = generate_grid(n_filled=n_filled)
    while not grid_is_valid(grid):
        grid = generate_grid(n_filled=n_filled)
        i += 1

    if print_attempts:
        print(f"Required {i} attempts to get a valid grid")

    return grid


def generate_grid(n_filled):
    """Generate a sudoku grid

    Parameters
    ----------
    n_filled : `int`
        How many entries to fill

    Returns
    -------
    grid : `list` of `lists`
        9x9 grid of sudoku entries
    """
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
            if grid[i][j] == 0:
                print(" ", end=" ")
            else:
                print(grid[i][j], end=" ")
            if (j - 2) % 3 == 0 and j < 8:
                print("|", end=" ")
        print()
        if (i - 2) % 3 == 0 and i < 8:
            print(*["-" for _ in range(9 + 2)], end=" ")
            print()


def empty_k_grid_spots(grid, k):
    remove_inds = np.random.choice(81, size=k, replace=False)
    rows, cols = ind2row_col(remove_inds)
    grid[rows, cols] = 0
    return grid


def parse_grid(grid_str):
    """Parse a grid from a string input.

    Use . to represent a blank square and | can optionally be used to note the end of rows.

    Parameters
    ----------
    grid_str : `str`
        A string representation of a sudoku grid

    Returns
    -------
    grid : `np.ndarray`
        The sudoku grid
    """
    return np.asarray([num for num in grid_str.replace(".", "0").replace("|", "")]).astype(int).reshape(9, 9)
