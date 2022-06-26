import logging
from pprint import *
from src.utils import *


class TreeSearch:
    """ """

    def __init__(self, model, optimize):
        """ """

        # args
        self.model = model
        self.optimize = optimize
        self.dep = model.dep
        self.dest = model.dest

        # default attrs
        # self.studied_strategies = []
        self.queued_strategies = [(self.dep,)]
        self.active_strategy = []
        self.evaluated_strategies = []
        self.winning_strategies = []

        self.current_depth = 1

        self.found = 0
        self.confirmed = 0

    def find_possible_dests(self, dep):
        """given a departure give all the possible destinations """

        trips = [(i, j) for i, j in self.model.trips.keys()]
        trips = [j for i, j in trips if i == dep]

        return sorted(trips)

    def eval_strategy(self):
        """ """

        strat = self.active_strategy
        # print(f"evaluating {strat}")

        self.evaluated_strategies.append(strat)

        if len(strat) == 1:
            return 0

        if strat[-1] == self.dest:
            self.winning_strategies.append(strat)
            self.found = 1
            self.confirmed = 1

            return 1

        return 0

    def log(self):
        """ """

        for attr in [
            "active_strategy",
            "queued_strategies",
            "evaluated_strategies",
            "winning_strategies",
        ]:

            logging.debug(f"\n----{attr.upper()}---- ")
            li = getattr(self, attr)
            logging.debug(pformat(li))
            logging.warning(f"len active_strategy is {len(li)} ")

        logging.warning("\n\n\n\n")

    def modelize_2(self, strategy) -> int:
        """give a strategy compute the score """

        ans = self.model.trips.get(strategy, -1)
        if ans == -1:
            return -1

        if self.optimize == "trips":
            return ans[0]
        if self.optimize == "time":
            return ans[1]
        if self.optimize == "cost":
            return ans[2]
        if self.optimize == "trips-time":
            return ans[0] + ans[1]
        if self.optimize == "trips-cost":
            return ans[0] + ans[2]
        if self.optimize == "time-cost":
            return ans[1] + ans[2]
        if self.optimize == "all":
            return sum(ans)

        raise AttributeError("optimize funct not allowed")

    def explode_strategy_in_pairs(self, strategy):
        """transform [paris, rouen, lyon] in [(paris, rouen), (rouen,lyon )] """

        return [(strategy[i], strategy[i + 1]) for i in range(len(strategy) - 1)]

    def modelize(self, strategy: list) -> int:
        """given a strategy with various towns, explode in pairs on town to town, then compute the score """

        # check
        assert len(strategy) > 1

        # if 2
        if len(strategy) == 2:
            return self.modelize_2(strategy)

        # else
        strategy_pairs = self.explode_strategy_in_pairs(strategy)
        strategy_results = [self.modelize_2(s) for s in strategy_pairs]

        if -1 in strategy_results:
            return -1

        return sum(strategy_results)