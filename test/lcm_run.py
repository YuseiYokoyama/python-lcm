from pprint import pprint as pp
from pprint import pformat as pf

import lcm

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser("Test lcm")
    args = parser.parse_args()

    data = [
            lcm.Itemset((         3,    5, 6, 7, 8,    10)),
            lcm.Itemset((      2, 3,    5,    7, 8,    10)),
            lcm.Itemset((0,       3,    5, 6,            )),
            lcm.Itemset((   1,          5, 6,       9, 10)),
            lcm.Itemset((   1,    3, 4, 5,       8,      )),
            ]
    result = lcm.run(data, 3)
    print('result') # debug
    pp(result) # debug

    correct_answer = [
            lcm.ItemsetPattern({5}, {0, 1, 2, 3, 4}),
            lcm.ItemsetPattern({3, 5}, {0, 1, 2, 4}),
            lcm.ItemsetPattern({5, 6}, {0, 2, 3}),
            lcm.ItemsetPattern({8, 3, 5}, {0, 1, 4}),
            lcm.ItemsetPattern({10, 5}, {0, 1, 3}),
            ]
    assert result == correct_answer

    print('\33[32m' + 'end' + '\033[0m')

