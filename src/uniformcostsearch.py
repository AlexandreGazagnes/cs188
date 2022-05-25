import logging
from pprint import *
from src.utils import *

from src.treesearch import TreeSearch


class UniformCostSearch(TreeSearch):
    """ """

    def __init__(self, model, optimize):
        """ """

        TreeSearch.__init__(self, model, optimize)

        self.reference_cost = 0

    def update_queue(self):
        """ """

        # possible_dest
        possible_dest = self.find_possible_dests(self.active_strategy[-1])

        # new strats
        update = lambda i: (self.active_strategy, [i])
        new_strats = [update(i) for i in possible_dest]
        new_strats = [tuple(flatten(i)) for i in new_strats]

        # update the queue
        if len(new_strats) >= 1:
            self.queued_strategies = new_strats + self.queued_strategies

        # cost_strat_pairs
        cost_strat_pairs = [(self.modelize(i), i) for i in self.queued_strategies]
        pprint(cost_strat_pairs)
        cost_strat_pairs = sorted(cost_strat_pairs, key=lambda i: i[0], reverse=False)
        sorted_new_start = [j for i, j in cost_strat_pairs]

        self.queued_strategies = sorted_new_start

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

        # level 1
        while not (self.found * self.confirmed):
            self.update_queue()
            self.extract_first_queue_to_active()
            self.eval_strategy()
            self.log()
            if self.found * self.confirmed:
                raise ArithmeticError("solution found ")
