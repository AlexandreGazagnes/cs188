from dataclasses import dataclass


@dataclass
class Model:
    """ """

    trips = {
        # (DEP,DEST) : (TIME, COST)
        # level 1
        ("rouen", "paris"): (1, 10),
        ("rouen", "versailles"): (1, 10),
        ("rouen", "lyon"): (6, 50),
        ("rouen", "dieppe"): (1, 10),
        ("paris", "versailles"): (0.6, 0),
        # level 2
        ("paris", "nogent"): (2, 10),
        ("versailles", "nogent"): (1.5, 10),
        ("lyon", "saint-maurice"): (5, 35),
        ("paris", "montargis"): (1.5, 0),
        ("versailles", "montargis"): (1.2, 0),
        # level 3
        ("montargis", "nogent"): (0.35, 0),
        # level 4
        ("nogent", "chatillon"): (0.1, 0),
        ("chatillon", "bonniere"): (0.1, 0),
        ("saint-maurice", "chatillon"): (0.15, 0),
    }

    dep = "rouen"
    dest = "bonniere"
    shortest_path = 3
    longest_path = 5
