import logging
from pprint import pprint, pformat

from src.modele import Model
from src.bruteforce import BruteForce
from src.depthfirstsearch import DepthFirstSearch
from src.breadthfirstsearch import BreadthFirstSearch


def main(optimize):

    # Model
    model = Model()

    # Depth
    depth = BruteForce(model, optimize=optimize)
    depth.run()


if __name__ == "__main__":

    for opt in ["trips", "time", "cost", "trips-time", "trips-cost", "time-cost", "all"]:
        logging.warning(f"\n\n\ncost to optpimize is -- {opt.upper()} --\n{'-'*54}")
        print(f"best for {opt} --> {main(optimize=opt)}")
