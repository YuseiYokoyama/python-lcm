from pprint import pprint as pp
from pprint import pformat as pf

import logging
logger = logging.getLogger()
#handler = logging.FileHandler(filename="log")
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)8s %(message)s'))
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

import random

import lcm

def make_random_data():
    data = []
    size = 10000
    u = list(range(2000))
    for _ in range(size):
        s = random.randint(500, 600)
        one = random.sample(u, s)
        data.append(set(one))
    return data

def test_run_auto():
    data = make_random_data()
    minsup, result = lcm.run_auto(data, timeout=7, try_count=5)
    print(f'minsup', minsup) # debug
    #print('result[:2]') # debug
    #pp(result[:2]) # debug


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser("Test lcm")
    args = parser.parse_args()

    test_run_auto()

    print('\33[32m' + 'end' + '\033[0m')

