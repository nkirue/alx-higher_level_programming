#!/usr/bin/python3
if __name__ == "__main__":
    """This print all names defined by hidden_4 module."""
    import hidden_4
    mod_names = dir(hidden_4)
    for nom in sorted(mod_names):
        if nom[:2] != "__":
            print(nom)
