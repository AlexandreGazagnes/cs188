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
    "dest": "g",
    "ans": {
        "depth": [
            "s",
            "s--d",
            "s--d--b",
            "s--d--b--a",
            "s--d--c",
            "s--d--c--a",
            "s--d--e",
            "s--d--e--h",
            "s--d--e--h--p",
            "s--d--e--h--p--q",
            "s--d--e--h--q",
            "s--d--e--r",
            "s--d--e--r--f",
            "s--d--e--r--f--c",
            "s--d--e--r--f--c--a",
            "s--d--e--r--f--g",
        ],
        "breadth": [
            "s",
            "s--d",
            "s--e",
            "s--p",
            "s--d--b",
            "s--d--c",
            "s--d--e",
            "s--e--h",
            "s--e--r",
            "s--p--q",
            "s--d--b--a",
            "s--d--c--a",
            "s--d--e--h",
            "s--d--e--r",
            # A FINIR !!!!!!
        ],
    }
    # shortest_path = 3
    # longest_path = 7
    # valid_strategies = 7
}
