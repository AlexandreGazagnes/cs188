from itertools import product
from src.modele import *


def extract_all_town(modele):
    """read the modele and extract all unique towns """

    cands = [(i, j) for i, j in modele.keys()]

    all_towns = []

    for i, j in [(i, j) for i, j in modele.keys()]:
        all_towns.append(i)
        all_towns.append(j)

    all_towns = list(set(all_towns))

    return all_towns


def cardinalize_one_depth_strategies(all_towns, depth=2):
    """give all strategies for a certain depht (ie the number of cities visited)
    compute cardinal product"""

    depth_max = 7
    assert depth in range(2, depth_max)

    depth_list = {
        i: [
            all_towns,
        ]
        * i
        for i in range(2, depth_max)
    }

    all_strategies = list(product(*depth_list[depth]))

    # filter first and last
    all_strategies = [s for s in all_strategies if s[0] == dep]
    all_strategies = [s for s in all_strategies if s[-1] == dest]

    return list(set(all_strategies))


def cardinalize_various_depth_strategies(all_towns, depth_list):
    """ """

    all_strategies = []
    for depth in depth_list:
        all_strategies.extend(cardinalize_one_depth_strategies(all_towns, depth))

    return list(set(all_strategies))


def modelize_2(strategy: list) -> int:
    return modele.get(strategy, -1)


def explode_strategy_in_pairs(strategy):
    """transform [paris, rouen, lyon] in [(paris, rouen), (rouen,lyon )] """

    return [(strategy[i], strategy[i + 1]) for i in range(len(strategy) - 1)]


def modelize_more(strategy: list) -> int:
    """ """

    # check
    assert len(strategy) > 1

    # if 2
    if len(strategy) == 2:
        return modelize_2(strategy)

    # else
    strategy_pairs = explode_strategy_in_pairs(strategy)
    strategy_results = [modelize_2(s) for s in strategy_pairs]

    if -1 in strategy_results:
        return -1

    return sum(strategy_results)


def select_only_valid_strategies(strategies_list: list) -> list:
    """ """

    ok_strategies = [
        strategy for strategy in strategies_list if modelize_more(strategy) > 0
    ]

    return ok_strategies


def find_best_strat(strategies_list):
    """ """

    scores = [modelize_more((s)) for s in strategies_list]
    best_strategies = list(zip(scores, strategies_list))

    return sorted(best_strategies)