import pytest
from src.model import *


li = [
    (Model(course_model), ["a", "b", "c"]),
    (Model(perso_model), ["a", "b", "c"]),
]


@pytest.mark.parametrize("model,ans", li)
def test_deph(model, ans):
    """ """

    return 1


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
