perso_model = {
    "name": "perso",
    "trips": {
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
    },
    "heuristic": {
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
    },
    "dep": "rouen",
    "dest": "bonniere",
    # shortest_path : 3
    "longest_path": 7,
    "valid_strategies": 7,
}
