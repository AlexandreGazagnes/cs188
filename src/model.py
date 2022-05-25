from dataclasses import dataclass

from treelib import Node, Tree


class ModelCourse:
    """ """

    def __init__(self):

        self.trips = {
            # (DEP,DEST) : (STEPS, TIME, COST)
            # level 1
            ("start", "d"): (3, 3, 3),
            ("start", "e"): (9, 9, 9),
            ("start", "p"): (1, 1, 1),
            # level 2
            ("d", "b"): (1, 1, 1),
            ("d", "c"): (8, 8, 8),
            ("d", "e"): (2, 2, 2),
            ("e", "r"): (2, 2, 2),
            ("e", "h"): (8, 8, 8),
            ("p", "q"): (15, 15, 15),
            # level 3
            ("b", "a"): (2, 2, 2),
            ("c", "a"): (2, 2, 2),
            ("r", "f"): (2, 2, 2),
            ("f", "c"): (3, 3, 3),
            ("h", "q"): (4, 4, 4),
            ("h", "p"): (4, 4, 4),
            # level 4
            ("f", "goal"): (2, 2, 2),
        }

        self.heuristic = {}
        self.dep = "start"
        self.dest = "goal"
        # shortest_path = 3
        # longest_path = 7
        # valid_strategies = 7

    def display_tree(self):

        tree = Tree()
        tree.create_node(self.dep, self.dep)  # root node
        for i, j in self.trips.keys():

            tree.create_node(i, i, parent=j)
        tree.show()


class ModelPerso:
    """ """

    def __init__(self):

        self.trips = {
            # (DEP,DEST) : (STEPS, TIME, COST)
            # level 1
            ("rouen", "paris"): (1, 1, 10),
            ("rouen", "versailles"): (1, 1, 10),
            ("rouen", "lyon"): (1, 6, 50),
            ("rouen", "dieppe"): (1, 1, 10),
            ("paris", "versailles"): (1, 0.6, 0),
            # level 2
            ("paris", "nogent"): (1, 2, 10),
            ("versailles", "nogent"): (1, 1.5, 10),
            ("lyon", "saint-maurice"): (1, 5, 35),
            ("paris", "montargis"): (1, 1.5, 0),
            ("versailles", "montargis"): (1, 1.2, 0),
            # level 3
            ("montargis", "nogent"): (1, 0.35, 0),
            # level 4
            ("nogent", "chatillon"): (1, 0.1, 0),
            ("chatillon", "bonniere"): (1, 0.1, 0),
            ("saint-maurice", "bonniere"): (1, 0.15, 0),
        }

        self.heuristic = {
            # TOWN : (STEPS, TIME, COST)
            "rouen": (3, 2.7, 10),
            #
            "lyon": (2, 5.15, 35),
            "saint-maurice": (1, 0.15, 0),
            #
            "paris": (3, 2.05, 0),
            "versailles": (3, 1.7, 0),
            #
            "montargis": (3, 0.55, 0),
            "nogent": (2, 0.2, 0),
            "chatillon": (1, 0.1, 0),
            #
            "bonniere": (0, 0, 0),
            "dieppe": (1_000_000, 1_000_000, 1_000_000),
        }

        self.dep = "rouen"
        self.dest = "bonniere"
        # shortest_path = 3
        self.longest_path = 7
        self.valid_strategies = 7

    def display_tree(self):

        tree = Tree()
        tree.create_node(self.dep, self.dep)  # root node
        for i, j in self.trips.keys():
            print(f"parent j {j} chid i {i}")

            try:
                tree.create_node(j, j, parent=i)
            except Exception as e:
                print("error")

        tree.show()


if __name__ == "__main__":
    self = ModelPerso()
    model.display_tree()
