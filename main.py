import logging
from pprint import pprint, pformat

from src.modele import Model
from src.bruteforce import BruteForce
from src.depthforsearch import DepthForSearch


def main():
    # Model
    model = Model()

    # Depth
    depth = DepthForSearch(model, optimize="time")
    depth.run()

    for attr in [
        "active_strategy",
        "queued_strategies",
        "evaluated_strategies",
        "winning_strategies",
    ]:

        logging.debug(f"\n\n\n----{attr.upper()}---- ")
        li = getattr(depth, attr)
        logging.debug(pformat(li))
        logging.warning(f"len active_strategy is {len(li)} ")


if __name__ == "__main__":

    main()

    # for opt in ["time", "cost", "both"]:
    #     logging.warning(f"\n\n\ncost to optpimize is -- {opt.upper()} --\n{'-'*54}")
    #     print(f"best for {opt} --> {main(optimize=opt)}")
