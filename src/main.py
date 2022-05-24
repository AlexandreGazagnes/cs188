from pprint import pprint, pformat
import logging

from src.modele import modele
from src.utils import *


LOG_LEVEL = logging.INFO


logging.basicConfig(filename="example.log", level=LOG_LEVEL, filemode="w+")


def main():
    """ """

    all_towns = extract_all_town(modele)
    logging.info(pformat(all_towns))

    all_strategies = cardinalize_various_depth_strategies(all_towns, [2, 3, 4, 6])
    logging.info(pformat(all_strategies))

    valid_strategies = select_only_valid_strategies(
        all_strategies,
    )
    logging.info(pformat(valid_strategies))

    best_strategies = find_best_strat(valid_strategies)
    logging.info(pformat(best_strategies))

    pprint(best_strategies)


main()