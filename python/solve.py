import numpy as np
from utils import ind2row_col, empty_k_grid_spots, print_grid, parse_grid
from validate import is_valid_move


def solve_sudoku(grid, algorithm="retracing", shuffle=False, stepbystep=False):
    """Solve a sudoku puzzle!

    Parameters
    ----------
    grid : `np.ndarray` or `str`
        Sudoku grid or string representation of grid
    algorithm : `str`, optional
        Which algorithm to use, by default "retracing"
    shuffle : `bool`, optional
        Whether to randomly choose which number to try instead of in order, by default False
    stepbystep : `bool`, optional
        Whether to print out the step-by-step solution, by default False

    Returns
    -------
    solved_grid : `np.ndarray`
        The fully filled in grid (if a solution is possible)
    can_be_solved : `bool`
        Whether the puzzle can be solved

    Raises
    ------
    ValueError
        If an invalid algorithm name is passed
    """
    # parse out a grid from a string if necessary
    if isinstance(grid, str):
        grid = parse_grid(grid)

    # solve the sudoku using the requested algorithm
    if algorithm == "retracing":
        return _solve_sudoku_retracing(grid, shuffle=shuffle, stepbystep=stepbystep)
    else:
        raise ValueError(f"Invalid algorithm name: `{algorithm}`")


def _solve_sudoku_retracing(grid, shuffle=False, stepbystep=False):
    """Solve a sudoku puzzle using the "retracing your steps" algorithm.

    For each empty entry, check if a number can be put there and the grid remain valid. If yes recurse, if no
    try the next number. If no numbers left then no solution. If no empty spots left then solution is complete

    Parameters
    ----------
    grid : `np.ndarray` or `str`
        Sudoku grid or string representation of grid
    shuffle : `bool`, optional
        Whether to randomly choose which number to try instead of in order, by default False
    stepbystep : `bool`, optional
        Whether to print out the step-by-step solution, by default False

    Returns
    -------
    solved_grid : `np.ndarray`
        The fully filled in grid (if a solution is possible)
    can_be_solved : `bool`
        Whether the puzzle can be solved
    """
    if stepbystep:
        print_grid(grid)
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
            new_grid, solution = solve_sudoku(grid, shuffle=shuffle, stepbystep=stepbystep)

            # if this gives a solution then return
            if solution:
                return new_grid, True
            # otherwise reset and try the next number
            else:
                grid[row, col] = 0
    # if no number fit then it's time to give up
    return grid, False


def generate_solvable_grid(n_filled):
    """Generate a fully solvable sudoku grid with `n_filled` non-empty squares

    Parameters
    ----------
    n_filled : `int`
        Number of squares to fill in

    Returns
    -------
    grid : `np.ndarray`
        The generated grid
    """
    # start with an empty grid
    grid = np.zeros((9, 9)).astype(int)

    # fill in the diagonals independently since they can't affect one another
    grid = _fill_diagonals(grid)

    # iteratively solve the puzzle
    grid, _ = solve_sudoku(grid, shuffle=True)

    # erase the required number of squares
    n_remove = max(81 - n_filled, 0)
    if n_remove > 0:
        grid = empty_k_grid_spots(grid, n_remove)
    return grid


def _fill_diagonals(grid):
    for i in range(3):
        grid[i * 3:(i + 1) * 3, i * 3:(i + 1) * 3] = np.random.choice(9, size=9, replace=False).reshape(3, 3) + 1
    return grid
