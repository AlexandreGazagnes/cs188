from pprint import pprint, pformat
import logging

from src.modele import modele
from src.utils import *


LOG_LEVEL = logging.INFO


logging.basicConfig(filename="example.log", level=LOG_LEVEL, filemode="w")


def main(optimize="time", max_depth=5):
    """ """

    all_towns = extract_all_town(modele)
    logging.debug(pformat(all_towns))
    logging.warning(f"len all_towns is {len(all_towns)} ")

    all_strategies = cardinalize_various_depth_strategies(
        all_towns, range(2, max_depth + 1)
    )
    logging.debug(pformat(all_strategies))
    logging.warning(f"len all_strategies is {len(all_strategies)} ")

    valid_strategies = select_only_valid_strategies(
        all_strategies,
    )
    logging.debug(pformat(valid_strategies))
    logging.warning(f"len valid_strategies is {len(valid_strategies)} ")

    modelized_strategies = modelize_strategies(valid_strategies, optimize=optimize)
    logging.info(pformat(modelized_strategies))
    logging.warning(f"len modelized_strategies is {len(modelized_strategies)} ")

    best_strategies = find_best_strategies(modelized_strategies)
    logging.info(pformat(best_strategies))
    logging.warning(f"len best_strategies is {len(best_strategies)} ")

    return best_strategies


if __name__ == "__main__":

    for opt in ["time", "cost", "both"]:
        logging.warning(f"\n\n\ncost to optpimize is -- {opt.upper()} --\n{'-'*12}")

        print(f"best for {opt} --> {main(optimize=opt)}")
