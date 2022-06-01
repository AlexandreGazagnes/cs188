import pytest
import logging

from src.model import *
from src.search import *


model_list = [course_model, perso_model]


@pytest.mark.parametrize("model", model_list)
def test_deph(model):
    """ """

    try:
        model = Model(**model)
        search = DepthFirstSearch(model, optimize="trips")
        search.run()
    except Exception as e:
        raise logging.critical(e)

        return search.evaluated_strategies


ans = [
    ["s"],
    ["s", "d"],
    # s d b
    ["s", "d", "b"],
    ["s", "d", "b", "a"],
    # s d c
    ["s", "d", "c"],
    ["s", "d", "c", "a"],
    # s d e
    ["s", "d", "e"],
    ["s", "d", "e", "h"],
    ["s", "d", "e", "h", "p"],
    ["s", "d", "e", "h", "p", "q"],
    ["s", "d", "e", "h", "q"],
    ["s", "d", "e", "r"],
    ["s", "d", "e", "r", "f"],
    ["s", "d", "e", "r", "f", "c"],
    ["s", "d", "e", "r", "f", "c", "a"],
    ["s", "d", "e", "r", "f", "g"],
]
