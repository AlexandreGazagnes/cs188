import logging
from pprint import *
from src.utils import *

from src.treesearch import TreeSearch


class BreadthFirstSearch(TreeSearch):
    """class Breadth First Search """

    def __init__(self, model: object, optimize: str):
        """init method"""

        TreeSearch.__init__(self, model, optimize)

    def update_queue(self):
        """ """

        # reload the empty queue for the past level of depht
        self.queued_strategies = [
            i for i in self.evaluated_strategies if len(i) == self.current_depth
        ]

        LI = []
        # for each strat of the "old" queue find all dest
        for strat in self.queued_strategies:
            possible_dest = self.find_possible_dests(strat[-1])
            update = lambda i: (strat, [i])
            li = [update(i) for i in possible_dest]
            li = [tuple(flatten(i)) for i in li]
            LI.extend(li)

        self.queued_strategies = LI

    def extract_first_queue_to_active(self):
        """ """

        self.active_strategy = self.queued_strategies[0]

        if len(self.queued_strategies) >= 1:
            self.queued_strategies = self.queued_strategies[1:]

    def run(self):
        """run a search """

        # Level 1
        self.current_depth = 1
        self.extract_first_queue_to_active()
        self.eval_strategy()
        if self.found * self.confirmed:
            raise ArithmeticError("solution found ")
        self.log()

        # level N
        while not (self.found * self.confirmed):
            self.update_queue()
            self.current_depth += 1

            for strat in self.queued_strategies:
                self.active_strategy = strat
                self.eval_strategy()

                if self.found * self.confirmed:
                    self.log()
                    raise ArithmeticError("solution found ")

            self.log()