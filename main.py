import logging
from pprint import pprint, pformat

from src.model import *
from src.search.bruteforce import BruteForce
from src.search.depthfirstsearch import DepthFirstSearch
from src.search.breadthfirstsearch import BreadthFirstSearch
from src.search.uniformcostsearch import UniformCostSearch


def ucs(optimize="time"):
    """ """

    try:
        model = Model(**course_model)
        search = UniformCostSearch(model, optimize=optimize)
        search.run()
    except Exception as e:
        logging.critical(e)

    return search.evaluated_strategies


def bfs():
    """ """

    try:
        model = Model(**course_model)
        search = BreadthFirstSearch(model, optimize="trips")
        search.run()
    except Exception as e:
        logging.critical(e)

    return search.evaluated_strategies


def dfs():
    """ """

    try:
        model = Model(**course_model)
        search = DepthFirstSearch(model, optimize="trips")
        search.run()
    except Exception as e:
        logging.critical(e)

    return search.evaluated_strategies


def bf():
    """ """

    pass


def compute_heuristic():
    """compute heuristic for every goal """

    model = Model(**perso_model)
    for dep in model.all_towns:

        result_list = []
        for optimize in ["trips", "time", "cost"]:

            # Model
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

    # result = ucs()
    # print(result)
    pass
