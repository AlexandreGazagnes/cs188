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
    # level 1
    ("rouen", "paris"): 1,
    ("rouen", "versailles"): 1,
    ("rouen", "lyon"): 6,
    ("rouen", "dieppe"): 1,
    ("paris", "versailles"): 0.6,
    # level 2
    ("paris", "bonniere"): 2,
    ("versailles", "bonniere"): 1.5,
    ("lyon", "bonniere"): 5,
    ("paris", "montargis"): 1.5,
    ("versailles", "montargis"): 1.2,
    # level 3
    ("montargis", "bonniere"): 0.35,
}


dep = "rouen"
dest = "bonniere"