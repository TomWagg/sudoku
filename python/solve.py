import numpy as np
from utils import ind2row_col, empty_k_grid_spots
from validate import is_valid_move


def solve_sudoku(grid, shuffle=False):
    # flattened version of the 9x9 grid
    flat_grid = grid.flatten()

    # get a list of the empty locations in the grid
    empty_locations = np.where(flat_grid == 0)[0]

    # if there are none then this is solved!
    if len(empty_locations) == 0:
        return grid, True

    # pick the first empty location and convert to row+col
    ind = empty_locations[0]
    row, col = ind2row_col(ind)

    # try every possible value
    val_range = list(range(1, 10))
    if shuffle:
        np.random.shuffle(val_range)
    for val in val_range:
        # if adding that value is a valid move
        if is_valid_move(grid, row, col, val):

            # try using this value and recursively solve
            grid[row, col] = val
            new_grid, solution = solve_sudoku(grid, shuffle=shuffle)

            # if this gives a solution then return
            if solution:
                return new_grid, True
            # otherwise reset and try the next number
            else:
                grid[row, col] = 0
    # if no number fit then it's time to give up
    return grid, False


def generate_solvable_grid(n_filled):
    # generate a fully solved grid, then erase some values!
    grid = np.zeros((9, 9)).astype(int)
    grid = _fill_diagonals(grid)
    grid, _ = solve_sudoku(grid, shuffle=True)

    n_remove = max(81 - n_filled, 0)
    if n_remove > 0:
        grid = empty_k_grid_spots(grid, n_remove)
    return grid


def _fill_diagonals(grid):
    for i in range(3):
        grid[i * 3:(i + 1) * 3, i * 3:(i + 1) * 3] = np.random.choice(9, size=9, replace=False).reshape(3, 3) + 1
    return grid
