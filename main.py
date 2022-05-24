import logging
from pprint import pprint, pformat

from src.modele import Model
from src.bruteforce import BruteForce
from src.depthforsearch import DepthForSearch


# model
model = Model()

# Brut
depth = DepthForSearch(model, optimize="time")
depth.run()


# def main(optimize):
#     """ """

#     # model
#     model = Model()

#     # Brut
#     brut = BruteForce(model, optimize=optimize)
#     brut.run()

#     # all_towns
#     logging.debug(pformat(brut.all_towns))
#     logging.warning(f"len all_towns is {len(brut.all_towns)} ")

#     # all_strategies
#     logging.debug(pformat(brut.all_strategies))
#     logging.warning(f"len all_strategies is {len(brut.all_strategies)} ")

#     # valid_strategies
#     logging.debug(pformat(brut.valid_strategies))
#     logging.warning(f"len valid_strategies is {len(brut.valid_strategies)} ")

#     # modelized_strategies
#     logging.info(pformat(brut.modelized_strategies))
#     logging.warning(f"len modelized_strategies is {len(brut.modelized_strategies)} ")

#     # best_strategies
#     logging.info(pformat(brut.best_strategies))
#     logging.warning(f"len best_strategies is {len(brut.best_strategies)} ")

#     return brut.best_strategies


# if __name__ == "__main__":

#     for opt in ["time", "cost", "both"]:
#         logging.warning(f"\n\n\ncost to optpimize is -- {opt.upper()} --\n{'-'*54}")
#         print(f"best for {opt} --> {main(optimize=opt)}")
