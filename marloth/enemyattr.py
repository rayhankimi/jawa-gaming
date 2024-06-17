import numpy as np


def enemyhp(_=2000) -> int:
    return _


def enemydef(_=1000) -> int:
    return _


def enemyatk(_=20) -> int:
    return _


def enemyreductions() -> int:
    reduction = 11 / 9 * np.sqrt(enemydef()) - enemydef() / 911
    return round(reduction)



