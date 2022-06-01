course_model = {
    "name": "course",
    "trips": {
        # (DEP,DEST) : (STEPS, TIME, COST)
        # level 1
        ("s", "d"): (3, 3, 3),
        ("s", "e"): (9, 9, 9),
        ("s", "p"): (1, 1, 1),
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
        ("f", "g"): (2, 2, 2),
    },
    "heuristic": {},
    "dep": "s",
    "dest": "g"
    # shortest_path = 3
    # longest_path = 7
    # valid_strategies = 7
}
