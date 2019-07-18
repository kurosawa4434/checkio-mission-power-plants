from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.referees import cover_codes
from tests import TESTS
from collections import defaultdict, Counter


def checker(inputs, user_answer):

    network, plants = inputs
    net_dic = defaultdict(set)
    all_cities = set()
    for a, b in network:
        net_dic[a].add(b)
        net_dic[b].add(a)
        all_cities |= {a, b}

    # value check
    if (not isinstance(user_answer, dict) or
            set(user_answer) - all_cities or
            Counter(user_answer.values()) - Counter(plants)):
        return False, (user_answer, 'Fail')

    # power supply check
    powered_cities = set()
    for c, p in user_answer.items():
        next_cities = {c}
        done_cities = {c}
        for _ in range(p):
            for nx in set(next_cities):
                next_cities |= net_dic[nx]
            next_cities -= done_cities
            done_cities |= next_cities
        powered_cities |= done_cities
    return not all_cities - powered_cities, (user_answer, 'Success')


cover = '''
def cover(func, args):
    network, ranges = args
    network = set(map(tuple, network))
    return func(network, ranges)
'''

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        checker=checker,
        function_name={
            "python": "power_plants",
            "js": "powerPlants"
        },
        cover_code={
            'python-3': cover,
            'js-node': cover_codes.js_unwrap_args
        }
    ).on_ready)
