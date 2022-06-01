from dataclasses import dataclass

import pydot


from .course.course_model import *
from .perso.perso_model import *


class Model:
    """ """

    def __init__(
        self,
        name="BaseModel",
        trips={},
        heuristic={},
        dep="",
        dest="",
        longest_path=-1,
        valid_strategies=-1,
    ):
        """ """

        self.name = name
        self.trips = trips
        self.heuristic = heuristic
        self.dep = dep
        self.dest = dest
        self.longest_path = longest_path
        self.valid_strategies = valid_strategies

    @property
    def all_towns(self):
        """read the modele and extract all unique towns """

        cands = [(i, j) for i, j in self.trips.keys()]

        all_towns = []

        for i, j in [(i, j) for i, j in self.trips.keys()]:
            all_towns.append(i)
            all_towns.append(j)

        return list(set(all_towns))

    def graph(self):
        """build dot graph  """

        # init
        graph = pydot.Dot(self.name, graph_type="graph", bgcolor="white")

        # root
        graph.add_node(pydot.Node(self.dep))

        # all node
        _ = [graph.add_node(pydot.Node(i)) for i in self.all_towns]

        # all edges
        _ = [graph.add_edge(pydot.Edge(i, j)) for i, j in self.trips.keys()]

        # export
        graph.write_png(self.name + ".png")


if __name__ == "__main__":

    import pydot

    self = Model(**perso_model)
    self.all_towns
    self.graph()