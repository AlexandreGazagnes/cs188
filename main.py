import logging
from pprint import pprint, pformat

from src.modele import Model
from src.bruteforce import BruteForce


def main(optimize="time"):
    """ """

    # model
    model = Model()

    # Brut
    brut = BruteForce(model, optimize=optimize)

    # all_towns
    all_towns = brut.extract_all_town()
    logging.debug(pformat(all_towns))
    logging.warning(f"len all_towns is {len(all_towns)} ")

    # all_strategies
    all_strategies = brut.cardinalize_all_depth_strategies()
    logging.debug(pformat(all_strategies))
    logging.warning(f"len all_strategies is {len(all_strategies)} ")

    # valid_strategies
    valid_strategies = brut.select_only_valid_strategies()
    logging.debug(pformat(valid_strategies))
    logging.warning(f"len valid_strategies is {len(valid_strategies)} ")

    # modelized_strategies
    modelized_strategies = brut.modelize_strategies()
    logging.info(pformat(modelized_strategies))
    logging.warning(f"len modelized_strategies is {len(modelized_strategies)} ")

    # best_strategies
    best_strategies = brut.find_best_strategies()
    logging.info(pformat(best_strategies))
    logging.warning(f"len best_strategies is {len(best_strategies)} ")

    return best_strategies


if __name__ == "__main__":

    for opt in ["time", "cost", "both"]:
        logging.warning(f"\n\n\ncost to optpimize is -- {opt.upper()} --\n{'-'*54}")
        print(f"best for {opt} --> {main(optimize=opt)}")
