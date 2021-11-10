import numpy as np
# from scipy.ndimage import binary_dilation
import random
import math
import string
# from my_solution import power_plants  # See the last comment below.


# def scope(shape, pos, r):
#     """ Get the grid (of given shape) of supplied cities by a power plant
#         at position pos of range r, in an elegant way. """
#     g = np.zeros(shape, int)
#     g[pos] = 1
#     return binary_dilation(g, iterations=r) if r else g

# This is IMO inelegant but efficient enough and does not require scipy,
# which is temporarily disabled on CheckiO at the time of this change.
def scope(shape, pos, r):
    return np.array([
        [abs(x - pos[0]) + abs(y - pos[1]) <= r for y in range(shape[1])]
        for x in range(shape[0])
    ])


def range_weight(r):
    # Decreasing weights to make the probability weak to choose big ones.
    # Small plants have big probability but are often useless then discarded.
    # So I have to force little ones in order to have them a bit in tests.
    return math.exp(-r)  # * math.sqrt(r + 1)


def count_zeros(grid):
    """ Count the number of zeros in the `numpy.ndarray` grid. """
    return sum(not x for x in grid.flat)


def random_test(shape):
    """ Create a random test of the given shape. """
    nb_rows, nb_cols = shape
    # Make explanation rectangle grid and network links.
    cities = iter(string.ascii_uppercase + string.ascii_lowercase)
    explanation = [''.join(next(cities) for _ in range(nb_cols))
                   for _ in range(nb_rows)]
    network = [(cell, explanation[i + di][j + dj])
               for i, row in enumerate(explanation)
               for j, cell in enumerate(row)
               for di, dj in ((1, 0), (0, 1))
               if i + di < nb_rows and j + dj < nb_cols]

    # Create a solution with random power plants.
    grid = np.zeros(shape, int)
    coords = {(i, j) for i in range(nb_rows) for j in range(nb_cols)}
    max_range = nb_rows//2 + nb_cols//2
    # A power plant of max range well placed can supply all cities.
    # But I don't want it so it will be < max_range.
    possible_ranges = range(max_range)
    weights = list(map(range_weight, possible_ranges))

    # Add random power plants until all cities are supplied.
    rand_solution = {}  # key = the position (not the city), value = the range.
    while not grid.all():
        r = random.choices(possible_ranges, weights)[0]
        pos = random.choice(list(coords - set(rand_solution)))
        new_grid = grid + scope(shape, pos, r)
        # This power plant is useless if it doesn't supply an unsupplied city.
        if count_zeros(new_grid) - count_zeros(grid):
            grid = new_grid
            rand_solution[pos] = r

    # All cities can be supplied, but maybe there are useless power plants.
    for pos, r in list(rand_solution.items()):
        new_grid = grid - scope(shape, pos, r)
        if new_grid.all():
            # Remove this useless power plant.
            del rand_solution[pos]
            grid = new_grid

    # We know we can supply all cities with these power plants but...
    # it may be possible to supply all cities without all given power plants.
    ranges = list(rand_solution.values())

    # I don't like to put a solution in a github repository.
    # I tried with mine, it can slow down the creation of some random tests.
    # But it can be useful to decrease the number of power plants.
    # On 1000 tests, my solution use all plants for only 15% of the tests.
    # my_result = power_plants(network, ranges)
    # ranges = list(my_result.values())

    args = [network, ranges]
    return {'input': args, 'answer': args, 'explanation': explanation}
