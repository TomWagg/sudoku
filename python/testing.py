from validate import grid_is_valid
from utils import print_grid, empty_k_grid_spots, parse_grid
from solve import solve_sudoku, generate_solvable_grid
import numpy as np
import time
import matplotlib.pyplot as plt


def basic_g4g_test():
    """ Copied this test from Geeks for Geeks """
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    grid = np.array(grid)

    # grid = parse_grid("3.65.84..|52.......|.87....31|..3.1..8.|9..863..5|.5..9.6..|13....25.|.......74|..52.63..")

    start = time.time()
    print_grid(grid)
    grid, solution_found = solve_sudoku(grid)
    assert solution_found, "This should definitely be solvable!"

    print()
    print()
    print(f"Solution found in {time.time() - start:1.1f}s")
    print_grid(grid)


def create_base_tests(size=100):
    """Create a bunch of base tests that can be used for all sorts

    Grids are saved to `../test_grids` folders for use by all languages (if I ever do that)

    Parameters
    ----------
    size : `int`, optional
        How many tests to create, by default 100
    """
    for i in range(size):
        grid = generate_solvable_grid(81)
        np.save(f"../test_grids/grid_{i:01d}.npy", grid)


def perform_base_tests(n_filled_range=np.arange(40, 50), n_tests=100):
    """Perform tests on the base grids with a range of different numbers of filled squares

    Parameters
    ----------
    n_filled_range : `np.ndarray`, optional
        Array of n_filled values for grids, by default np.arange(40, 50)
    n_tests : `int`, optional
        How many base tests to use, by default 100

    Returns
    -------
    completion_times : `np.ndarray`
        2d array of time it took to solve in seconds
    """
    n_removes = 81 - n_filled_range
    completion_times = np.zeros(shape=(len(n_removes), n_tests))
    grids = [np.load(f"../test_grids/grid_{i}.npy") for i in range(n_tests)]
    for i in range(len(n_removes)):
        for j in range(n_tests):
            reduced_grid = empty_k_grid_spots(grids[j], n_removes[i])
            start = time.time()
            solved_grid, worked = solve_sudoku(reduced_grid)
            tot_time = time.time() - start
            if worked:
                completion_times[i, j] = tot_time
                print(n_removes[i], j, f"Time: {tot_time:1.2f}s")
            else:
                print("TEST FAILED!!")
                print_grid(grids[j])
                print()
                print_grid(solved_grid)
    return completion_times


def perform_random_tests(size=10):
    n_filleds = np.random.randint(20, 50, size=size)
    time_to_solves = np.zeros(size)
    for i in range(size):
        grid = generate_solvable_grid(n_filleds[i])

        start = time.time()
        grid, solution_found = solve_sudoku(grid)
        time_to_solve = time.time() - start
        if solution_found:
            time_to_solves[i] = time_to_solve
        else:
            print("TEST FAILED!")
            print_grid(grid)
            print(grid_is_valid(grid), solution_found)
    return n_filleds, time_to_solves


def plot_solver_times():
    n_filled_range = np.arange(1, 81)
    try:
        completion_times = np.load("completion_times_buffer.npy")
    except FileNotFoundError:
        completion_times = perform_base_tests(n_filled_range=n_filled_range)
        np.save("completion_times_buffer.npy", completion_times)

    plt.errorbar(n_filled_range, completion_times.mean(axis=1), yerr=completion_times.std(axis=1),
                label=r"Mean and 1$\sigma$ errors" + "\non 100 random grids")
    # plt.plot(n_filled_range, (81 - n_filled_range).astype("float") / 2500)
    plt.yscale("log")
    plt.xlabel("Number of Empty Squares")
    plt.ylabel("Runtime [seconds]")
    plt.legend(loc="lower left")
    plt.title("Sudoku Solver Runtime")
    plt.savefig("time_to_solve.pdf", format="pdf", bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    basic_g4g_test()
    # perform_random_tests()

    # create_base_tests()
    # perform_base_tests()
    plot_solver_times()
