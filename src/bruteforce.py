from itertools import product

# from src.modele import *


class BruteForce:
    """ """

    def __init__(self, model, optimize):
        """ """

        # args
        self.model = model
        self.optimize = optimize

        # default attrs
        self.all_towns = []
        self.all_strategies = []
        self.valid_strategies = []
        self.modelized_strategies = []
        self.best_strategies = []

    def extract_all_town(self):
        """read the modele and extract all unique towns """

        cands = [(i, j) for i, j in self.model.trips.keys()]

        all_towns = []

        for i, j in [(i, j) for i, j in self.model.trips.keys()]:
            all_towns.append(i)
            all_towns.append(j)

        self.all_towns = list(set(all_towns))

        return all_towns

    def cardinalize_one_depth_strategies(self, depth=2):
        """give all strategies for a certain depht (ie the number of cities visited)
        compute cardinal product"""

        strat_list = [
            self.all_towns,
        ] * depth

        all_strategies = list(product(*strat_list))

        # filter first and last
        all_strategies = [s for s in all_strategies if s[0] == self.model.dep]
        all_strategies = [s for s in all_strategies if s[-1] == self.model.dest]

        all_strategies = list(set(all_strategies))
        self.all_strategies = all_strategies

        return all_strategies

    def cardinalize_all_depth_strategies(self):
        """compute carninal all possible strageiges for various depths """

        depth_list = range(2, self.model.longest_path + 1)

        all_strategies = []
        for depth in depth_list:
            all_strategies.extend(self.cardinalize_one_depth_strategies(depth))

        all_strategies = list(set(all_strategies))
        self.all_strategies = all_strategies

        return all_strategies

    def modelize_2(self, strategy) -> int:
        """give a strategy compute the score """

        ans = self.model.trips.get(strategy, -1)
        if ans == -1:
            return -1

        if self.optimize == "time":
            return ans[0]
        if self.optimize == "cost":
            return ans[1]

        return sum(ans)

    def find_possible_dests(self, dep):
        """given a departure give all the possible destinations """

        trips = [(i, j) for i, j in self.model.trips.keys()]
        trips = [j for i, j in trips if i == dep]

        return trips

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

    def select_only_valid_strategies(self) -> list:
        """given a list of various strategies select permited by the model possible strategies  """

        ok_strategies = [
            strategy for strategy in self.all_strategies if self.modelize(strategy) >= 0
        ]

        self.valid_strategies = ok_strategies
        return ok_strategies

    def modelize_strategies(self):
        """given a list of validated stragies compute sthe score for each one """

        scores = [self.modelize(s) for s in self.valid_strategies]
        scores = [round(i, 4) for i in scores]

        modelized_strategies = list(zip(scores, self.valid_strategies))
        modelized_strategies = sorted(modelized_strategies)
        self.modelized_strategies = modelized_strategies

        return modelized_strategies

    def find_best_strategies(self):
        """give the modelized_strategies select only those (one ore more) with the lowest score """

        cost_min = 1_000_000_000
        best_strategies = list()
        for cost, strat in self.modelized_strategies:
            if cost <= cost_min:
                cost_min = cost
                best_strategies.append([cost, strat])

        self.best_strategies = best_strategies

        return best_strategies

    def run(self):
        """ """

        _ = self.extract_all_town()
        _ = self.cardinalize_all_depth_strategies()
        _ = self.select_only_valid_strategies()
        _ = self.modelize_strategies()
        _ = self.find_best_strategies()

        return None
