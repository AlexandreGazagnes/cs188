from src.modele import modele
from src.utils import *


def main():
    """ """

    all_towns = extract_all_town(modele)
    # print(all_towns)

    all_strategies = cardinalize_various_depth_strategies(all_towns, [2, 3, 4, 5])
    # print(all_strategies)

    valid_strategies = select_only_valid_strategies(
        all_strategies,
    )
    print(valid_strategies)

    best_strategies = find_best_strat(valid_strategies)
    print(best_strategies)