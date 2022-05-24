# modele = {
#     # level 1
#     ("rouen", "paris"): 1,
#     ("rouen", "versailles"): 1,
#     ("paris", "versailles"): 0.6,
#     # level 2
#     ("paris", "bonniere"): 2,
#     ("versailles", "bonniere"): 1.5,
# }


modele = {
    # (DEP,DEST) : (TIME, COST)
    # level 1
    ("rouen", "paris"): (1, 10),
    ("rouen", "versailles"): (1, 10),
    ("rouen", "lyon"): (6, 50),
    ("rouen", "dieppe"): (1, 10),
    ("paris", "versailles"): (0.6, 0),
    # level 2
    ("paris", "bonniere"): (2, 10),
    ("versailles", "bonniere"): (1.5, 10),
    ("lyon", "bonniere"): (5, 35),
    ("paris", "montargis"): (1.5, 0),
    ("versailles", "montargis"): (1.2, 0),
    # level 3
    ("montargis", "bonniere"): (0.35, 0),
}


dep = "rouen"
dest = "bonniere"