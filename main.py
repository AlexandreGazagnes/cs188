import logging
from pprint import pprint, pformat

from src.modele import Model
from src.bruteforce import BruteForce
from src.depthforsearch import DepthForSearch


def main(optimize):
    # Model
    model = Model()

    # Depth
    depth = BruteForce(model, optimize=optimize)
    depth.run()


if __name__ == "__main__":

    for opt in ["time", "cost", "both"]:
        logging.warning(f"\n\n\ncost to optpimize is -- {opt.upper()} --\n{'-'*54}")
        print(f"best for {opt} --> {main(optimize=opt)}")
