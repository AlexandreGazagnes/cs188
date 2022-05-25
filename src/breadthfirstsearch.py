import logging
from pprint import *
from src.utils import *

from src.treesearch import TreeSearch


class BreadthFirstSearch(TreeSearch):
    """ """

    def __init__(self, model, optimize):
        """ """

        TreeSearch.__init__(self, model, optimize)

    def update_queue(self):
        """ """

        print("update_queue")

        LI = []
        for strat in self.queued_strategies:
            possible_dest = self.find_possible_dests(strat[-1])
            update = lambda i: (strat, [i])
            li = [update(i) for i in possible_dest]
            li = [tuple(flatten(i)) for i in li]
            LI.extend(li)

        self.queued_strategies = LI

    def extract_first_queue_to_active(self):
        """ """

        pprint("-- extract_first_queue_to_active --")
        pprint("BEFORE")
        pprint(self.queued_strategies)
        self.active_strategy = self.queued_strategies[0]
        pprint(self.active_strategy)

        if len(self.queued_strategies) >= 1:
            self.queued_strategies = self.queued_strategies[1:]

        pprint("AFTER")
        pprint(self.queued_strategies)

    def run(self):
        """ """

        # Level 1
        self.current_depth = 1
        self.extract_first_queue_to_active()
        self.eval_strategy()

        if self.found * self.confirmed:
            raise ArithmeticError("solution found ")
        li = [i for i in self.evaluated_strategies if len(i) == self.current_depth]
        self.queued_strategies = li
        self.log()

        # level 1
        while not (self.found * self.confirmed):
            self.update_queue()
            self.current_depth += 1
            print(f"BEFORE LOOOP FOR self.self.current_depth  = {self.current_depth }")
            print(f"BEFORE LOOOP FOR self.queued_strategies = {self.queued_strategies}")
            for s in self.queued_strategies:
                self.active_strategy = s
                self.eval_strategy()
                # self.log()
                if self.found * self.confirmed:
                    raise ArithmeticError("solution found ")

            li = [i for i in self.evaluated_strategies if len(i) == self.current_depth]
            print(f"IN LOOP FOR evalueated srategies : {self.evaluated_strategies}")
            print(f"IN LOOOP FOR li = {li}")

            self.queued_strategies = li
            self.log()
            if self.current_depth > 10:
                break