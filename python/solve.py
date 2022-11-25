import numpy as np
from utils import ind2row_col, print_grid
from validate import grid_is_valid, is_valid_move


def solve_sudoku(grid):
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
    for val in range(1, 10):
        # if adding that value is a valid move
        if is_valid_move(grid, row, col, val):

            # try using this value and recursively solve
            grid[row, col] = val
            new_grid, solution = solve_sudoku(grid)

            # if this gives a solution then return
            if solution:
                return new_grid, True
            # otherwise reset and try the next number
            else:
                grid[row, col] = 0
    # if no number fit then it's time to give up
    return grid, False
