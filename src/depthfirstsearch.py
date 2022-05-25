import logging
from pprint import *
from src.utils import *

from src.treesearch import TreeSearch


class DepthFirstSearch(TreeSearch):
    """ """

    def __init__(self, model, optimize):
        """ """

        TreeSearch.__init__(self, model, optimize)

    def update_queue(self):
        """ """

        # print("update_queue")
        possible_dest = self.find_possible_dests(self.active_strategy[-1])
        update = lambda i: (self.active_strategy, [i])
        li = [update(i) for i in possible_dest]
        li = [tuple(flatten(i)) for i in li]
        li = sorted(li, key=len, reverse=True)

        if len(li) >= 1:
            self.queued_strategies = li + self.queued_strategies

    def extract_first_queue_to_active(self):
        """ """

        # pprint("-- extract_first_queue_to_active --")
        # pprint("BEFORE")
        # pprint(self.queued_strategies)
        self.active_strategy = self.queued_strategies[0]
        # pprint(self.active_strategy)

        if len(self.queued_strategies) >= 1:
            self.queued_strategies = self.queued_strategies[1:]

        # pprint("AFTER")
        # pprint(self.queued_strategies)

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
