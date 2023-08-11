def sign(continents, treaty):
    """
    Sign a treaty with other continents.
    """
    for continent in continents:
        if continent == "Europe":
            print("Europe: Signing treaty %s" % treaty)
        else:
            print("Europe: Not signing treaty")