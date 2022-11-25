import numpy as np


def grid_is_valid(grid, verbose=False):
    # check whether a sudoku grid is valid
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
    for rs in range(3):
        for cs in range(3):
            box = grid[rs * 3:(rs + 1) * 3, cs * 3:(cs + 1) * 3]
            if np.any(box) > 0:
                _, counts = np.unique(box[box > 0], return_counts=True)
                if any(counts > 1):
                    return False
    return True


def has_valid_rows(grid):
    for row in grid:
        # print(row)
        if any(row) > 0:
            _, counts = np.unique(row[row > 0], return_counts=True)
            if any(counts > 1):
                return False
    return True