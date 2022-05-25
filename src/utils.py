def flatten(items):
    """ """

    L = list()
    for k in items:
        L.extend(tuple(k))

    return L