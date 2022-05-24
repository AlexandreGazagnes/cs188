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
        self.studied_strategies = []
        self.active_strategy = []
        self.queued_strategies = []
        self.winning_strategies = []

        self.current_depth = -1

        self.found = 0
        self.confirmed = 0

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

    def run(self):
        """ """

        # build 1st list of strat
        possible_dest = self.find_possible_dests(self.dep)

        self.queued_strategies = [(self.dep, i) for i in possible_dest]
        self.queued_strategies = sorted(self.queued_strategies, key=len, reverse=True)
        print(self.queued_strategies)

        # check if OK
        if self.queued_strategies[-1] == self.dest:
            self.found = 1
            self.confirmed = 1

        self.active_strategy = self.queued_strategies[0]
        self.queued_strategies = self.queued_strategies[1:]

        # build 2nd
        possible_dest = self.find_possible_dests(self.active_strategy[-1])
