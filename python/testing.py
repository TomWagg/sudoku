from validate import grid_is_valid
from utils import generate_valid_grid, print_grid

grid = generate_valid_grid(10)
print_grid(grid)
print(grid_is_valid(grid, verbose=True))
