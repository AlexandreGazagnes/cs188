import logging
from pprint import *
from src.utils import *


class DepthForSearch:
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

        self.current_depth = -1

        self.found = 0
        self.confirmed = 0

    # def modelize_2(self, strategy) -> int:
    #     """give a strategy compute the score """

    #     ans = self.model.trips.get(strategy, -1)
    #     if ans == -1:
    #         return -1

    #     if self.optimize == "time":
    #         return ans[0]
    #     if self.optimize == "cost":
    #         return ans[1]

    #     return sum(ans)

    def find_possible_dests(self, dep):
        """given a departure give all the possible destinations """

        trips = [(i, j) for i, j in self.model.trips.keys()]
        trips = [j for i, j in trips if i == dep]

        return sorted(trips)

    def eval_strategy(self):
        """ """

        strat = self.active_strategy
        print(f"evaluating {strat}")

        self.evaluated_strategies.append(strat)

        if len(strat) == 1:
            return 0

        if strat[-1] == self.dest:
            self.winning_strategies.append(strat)
            self.found = 1
            self.confirmed = 1

            return 1

        return 0

    def update_queue(self):
        """ """

        possible_dest = self.find_possible_dests(self.active_strategy[-1])
        update = lambda i: (self.active_strategy, [i])
        li = [update(i) for i in possible_dest]
        li = [tuple(flatten(i)) for i in li]
        li = sorted(li, key=len, reverse=True)

        self.queued_strategies = li

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

    def extract_first_queue_to_active(self):
        """ """

        self.active_strategy = self.queued_strategies[0]
        if len(self.queued_strategies) >= 1:
            self.queued_strategies = self.queued_strategies[1:]

    def run(self):
        """ """

        # Level 0
        self.extract_first_queue_to_active()
        self.eval_strategy()
        self.log()
        if self.found * self.confirmed:
            raise ArithmeticError("solution found ")

        while not (self.found * self.confirmed):
            self.update_queue()
            self.extract_first_queue_to_active()
            self.eval_strategy()
            self.log()
            if self.found * self.confirmed:
                raise ArithmeticError("solution found ")
