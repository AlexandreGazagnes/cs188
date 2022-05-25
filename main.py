import logging
from pprint import pprint, pformat

from src.modele import Model
from src.bruteforce import BruteForce
from src.depthfirstsearch import DepthFirstSearch
from src.breadthfirstsearch import BreadthFirstSearch


def main():

    try:
        model = Model()
        depth = DepthFirstSearch(model, optimize="trips")
        depth.run()
    except Exception as e:
        logging.critical(e)

    return depth.evaluated_strategies


def compute_heuristic():
    """compute heuristic for every goal """

    for dep in (
        "rouen",
        "lyon",
        "paris",
        "versailles",
        "montargis",
        "nogent",
        "chatillon",
        "saint-maurice",
    ):

        result_list = []
        for optimize in ["trips", "time", "cost"]:

            # Model
            model = Model()
            model.dep = dep

            # BruteForce
            brute = BruteForce(model, optimize=optimize)

            # run
            brute.run()

            # reuslt
            result_list.append(brute.best_score)

        print(f"dep : {dep} - heuristic : {result_list}")

    return None


if __name__ == "__main__":

    print(main())