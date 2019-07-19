"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""
from random_tests import random_test

basic_tests = [
    [
        [['A', 'B'], ['B', 'C']],
        [1],
        ['A  ',
         ' B ',
         '  C']
    ],
    [
        [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['A', 'F'], ['F', 'G'], ['G', 'H']],
        [2, 1],
        ['ABCDE',
         'FGH  ']
    ],
    [
        [['A', 'B'], ['A', 'C'], ['B', 'D'], ['C', 'D']],
        [2],
        ['  A  ',
         '     ',
         'B   C',
         '     ',
         '  D  ']
    ],
    [
        [['A', 'B'], ['B', 'C'], ['A', 'D'], ['C', 'E'],
         ['D', 'F'], ['E', 'G'], ['F', 'H'], ['G', 'J'],
         ['H', 'I'], ['I', 'J']],
        [3, 1],
        ['ABC  ',
         'D  E ',
         ' F  G',
         '  HIJ']
    ],
    [
        [['A', 'B'], ['B', 'C'], ['A', 'D'], ['B', 'E']],
        [1, 0],
        ['A B C',
         ' D E ']
    ],
    [
        [['A', 'B'], ['A', 'C'], ['C', 'D'], ['C', 'E'], ['E', 'F'], ['F', 'G'], ['F', 'H']],
        [1, 1, 0],
        ['AB   ',
         ' CD  ',
         '  EFG',
         '  H  ']
    ],
    [
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['A', 'E'],
         ['C', 'F'], ['C', 'G'], ['E', 'H'], ['E', 'I'],
         ['F', 'J'], ['F', 'K'], ['H', 'L'], ['L', 'M']],
        [2, 1, 0],
        [' A   ',
         'BCDE ',
         ' FGHI',
         ' JKL ',
         '   M ']
    ],
]
extra_tests = [
    [
        [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['F', 'G'], ['G', 'H'],
         ['H', 'I'], ['I', 'J'], ['K', 'L'], ['L', 'M'], ['M', 'N'], ['N', 'O'],
         ['P', 'Q'], ['Q', 'R'], ['R', 'S'], ['S', 'T'], ['U', 'V'], ['V', 'W'],
         ['W', 'X'], ['X', 'Y'], ['A', 'F'], ['B', 'G'], ['C', 'H'], ['D', 'I'],
         ['E', 'J'], ['F', 'K'], ['G', 'L'], ['H', 'M'], ['I', 'N'], ['J', 'O'],
         ['K', 'P'], ['L', 'Q'], ['M', 'R'], ['N', 'S'], ['O', 'T'], ['P', 'U'],
         ['Q', 'V'], ['R', 'W'], ['S', 'X'], ['T', 'Y']],
        [4],
        ['ABCDE',
         'FGHIJ',
         'KLMNO',
         'PQRST',
         'UVWXY']
    ],
    [
        [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['F', 'G'], ['G', 'H'],
         ['H', 'I'], ['I', 'J'], ['K', 'L'], ['L', 'M'], ['M', 'N'], ['N', 'O'],
         ['P', 'Q'], ['Q', 'R'], ['R', 'S'], ['S', 'T'], ['U', 'V'], ['V', 'W'],
         ['W', 'X'], ['X', 'Y'], ['A', 'F'], ['B', 'G'], ['C', 'H'], ['D', 'I'],
         ['E', 'J'], ['F', 'K'], ['G', 'L'], ['H', 'M'], ['I', 'N'], ['J', 'O'],
         ['K', 'P'], ['L', 'Q'], ['M', 'R'], ['N', 'S'], ['O', 'T'], ['P', 'U'],
         ['Q', 'V'], ['R', 'W'], ['S', 'X'], ['T', 'Y']],
        [3, 3],
        ['ABCDE',
         'FGHIJ',
         'KLMNO',
         'PQRST',
         'UVWXY']
    ],
    [
        [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['F', 'G'], ['G', 'H'],
         ['H', 'I'], ['I', 'J'], ['K', 'L'], ['L', 'M'], ['M', 'N'], ['N', 'O'],
         ['P', 'Q'], ['Q', 'R'], ['R', 'S'], ['S', 'T'], ['U', 'V'], ['V', 'W'],
         ['W', 'X'], ['X', 'Y'], ['A', 'F'], ['B', 'G'], ['C', 'H'], ['D', 'I'],
         ['E', 'J'], ['F', 'K'], ['G', 'L'], ['H', 'M'], ['I', 'N'], ['J', 'O'],
         ['K', 'P'], ['L', 'Q'], ['M', 'R'], ['N', 'S'], ['O', 'T'], ['P', 'U'],
         ['Q', 'V'], ['R', 'W'], ['S', 'X'], ['T', 'Y']],
        [3, 1, 1],
        ['ABCDE',
         'FGHIJ',
         'KLMNO',
         'PQRST',
         'UVWXY']
    ],
    [
        [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['F', 'G'], ['G', 'H'],
         ['H', 'I'], ['I', 'J'], ['K', 'L'], ['L', 'M'], ['M', 'N'], ['N', 'O'],
         ['P', 'Q'], ['Q', 'R'], ['R', 'S'], ['S', 'T'], ['U', 'V'], ['V', 'W'],
         ['W', 'X'], ['X', 'Y'], ['A', 'F'], ['B', 'G'], ['C', 'H'], ['D', 'I'],
         ['E', 'J'], ['F', 'K'], ['G', 'L'], ['H', 'M'], ['I', 'N'], ['J', 'O'],
         ['K', 'P'], ['L', 'Q'], ['M', 'R'], ['N', 'S'], ['O', 'T'], ['P', 'U'],
         ['Q', 'V'], ['R', 'W'], ['S', 'X'], ['T', 'Y']],
        [2, 2, 1, 1],
        ['ABCDE',
         'FGHIJ',
         'KLMNO',
         'PQRST',
         'UVWXY']
    ],
    [
        [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['F', 'G'], ['G', 'H'],
         ['H', 'I'], ['I', 'J'], ['K', 'L'], ['L', 'M'], ['M', 'N'], ['N', 'O'],
         ['P', 'Q'], ['Q', 'R'], ['R', 'S'], ['S', 'T'], ['U', 'V'], ['V', 'W'],
         ['W', 'X'], ['X', 'Y'], ['A', 'F'], ['B', 'G'], ['C', 'H'], ['D', 'I'],
         ['E', 'J'], ['F', 'K'], ['G', 'L'], ['H', 'M'], ['I', 'N'], ['J', 'O'],
         ['K', 'P'], ['L', 'Q'], ['M', 'R'], ['N', 'S'], ['O', 'T'], ['P', 'U'],
         ['Q', 'V'], ['R', 'W'], ['S', 'X'], ['T', 'Y']],
        [2, 1, 1, 1, 1],
        ['ABCDE',
         'FGHIJ',
         'KLMNO',
         'PQRST',
         'UVWXY']
    ],
]


def make_tests(tests):
    return [{'input': bt[0:2],
             'answer': bt[0:2],
             'explanation': bt[2]} for bt in tests]


shapes = [(5, 5), (5, 6), (5, 7), (6, 6), (8, 5),
          (7, 6), (5, 9), (6, 8), (7, 7), (10, 5)]

TESTS = {
    "Basics": make_tests(basic_tests),
    "Extra": make_tests(extra_tests),
    "Random": list(map(random_test, shapes)),
}
