import numpy as np


def grid_is_valid(grid, verbose=False):
    """Check whether a sudoku grid is valid

    Check that each row has no repeated numbers, each column has no repeated numbers and that each 3x3 box
    has no repeated numbers.

    Parameters
    ----------
    grid : `list` of `lists`
        9x9 grid of sudoku entries
    verbose : `bool`, optional
        Whether to print out why a grid is invalid, by default False

    Returns
    -------
    valid : `bool`
        Whether the grid is valid
    """
    if not has_valid_rows(grid):
        if verbose:
            print("A row has a repeated entry")
        return False
    if not has_valid_rows(grid.T):
        if verbose:
            print("A column has a repeated entry")
        return False
    if not has_valid_boxes(grid):
        if verbose:
            print("A box has a repeated entry")
        return False
    return True


def has_valid_boxes(grid):
    """Check whether a sudoku grid has valid 3x3 boxes

    Parameters
    ----------
    grid : `list` of `lists`
        9x9 grid of sudoku entries

    Returns
    -------
    valid : `bool`
        Whether the grid has valid boxes
    """
    for rs in range(3):
        for cs in range(3):
            box = grid[rs * 3:(rs + 1) * 3, cs * 3:(cs + 1) * 3]
            if np.any(box) > 0:
                _, counts = np.unique(box[box > 0], return_counts=True)
                if any(counts > 1):
                    return False
    return True


def has_valid_rows(grid):
    """Check whether a sudoku grid has valid rows

    NOTE: You can pass the transpose of the grid to check the columns

    Parameters
    ----------
    grid : `list` of `lists`
        9x9 grid of sudoku entries

    Returns
    -------
    valid : `bool`
        Whether the grid has valid rows
    """
    for row in grid:
        # check if the row has any filled values (0 = empty)
        if any(row) > 0:
            # check how many unique entries there are for each value
            _, counts = np.unique(row[row > 0], return_counts=True)

            # if any are repeated then grid is invalid
            if any(counts > 1):
                return False
    return True
