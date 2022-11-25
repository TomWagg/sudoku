from validate import grid_is_valid
from utils import generate_valid_grid, print_grid
from solve import solve_sudoku
import numpy as np
import time

# grid = generate_valid_grid(20)

def basic_g4g_test():
    grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
           [5, 2, 0, 0, 0, 0, 0, 0, 0],
           [0, 8, 7, 0, 0, 0, 0, 3, 1],
           [0, 0, 3, 0, 1, 0, 0, 8, 0],
           [9, 0, 0, 8, 6, 3, 0, 0, 5],
           [0, 5, 0, 0, 9, 0, 6, 0, 0],
           [1, 3, 0, 0, 0, 0, 2, 5, 0],
           [0, 0, 0, 0, 0, 0, 0, 7, 4],
           [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    grid = np.array(grid)

    start = time.time()
    print_grid(grid)
    grid, solution_found = solve_sudoku(grid)

    print()
    print()
    print(f"Solution found in {time.time() - start:1.1f}s")
    print_grid(grid)

def random_grid_test():
    start = time.time()
    grid = generate_valid_grid(25)
    print(f"Grid creation took {time.time() - start:1.1f}s")

    start = time.time()
    print_grid(grid)
    grid, solution_found = solve_sudoku(grid)

    print("\n\n")
    if solution_found:
        print(f"Solution found in {time.time() - start:1.1f}s")
        print_grid(grid)
    else:
        print("No possible solutions")

basic_g4g_test()
random_grid_test()