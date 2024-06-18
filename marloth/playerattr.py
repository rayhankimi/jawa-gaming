from marloth import playerstat as ps
import numpy as np


def patk() -> int:
    pattack = round(10 + (ps.strength() * 2) + (ps.dexterity() * 1) + (ps.agility() * 0.5))
    return pattack


def hp() -> int:
    health = 500 + ps.vitality() * 40
    return health


def pdef() -> int:
    pdefense = round((ps.vitality() * 2) + (ps.strength() * 0.5))
    return pdefense


def mdef() -> int:
    mdefense = round((ps.vitality() * 2) + (ps.intelligence() * 0.5))
    return mdefense


def matk() -> int:
    mattack = round((ps.intelligence() * 2) + (ps.dexterity() * 1) + (ps.agility() * 0.5))
    return mattack


def playerReductions() -> int:
    reduction = 11 / 9 * np.sqrt(pdef()) - pdef() / 911
    return round(reduction)


def printStats() -> None:
    print(f"Patk ={patk()}")
    print(f"Matk = {matk()}")
    print(f"HP = {hp()}")
    print(f"Defense = {pdef()}")
    print(f"MDefense = {mdef()}")


printStats()
