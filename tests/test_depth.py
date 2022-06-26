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
        logging.critical(e)

    ans = search.evaluated_strategies
    ans = ["--".join(i) for i in ans]
    print(model.ans["depth"])
    print(ans)
    assert model.ans["depth"] == ans
