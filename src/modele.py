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
}


dep = "rouen"
dest = "bonniere"