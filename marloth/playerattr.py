from marloth import playerstat as ps


def patk() -> int:
    pattack = round(1300 + (ps.strength() * 2) + (ps.dexterity() * 1) + (ps.agility() * 0.5))
    return pattack


def hp() -> int:
    hp = 500 + ps.vitality() * 40
    return hp


def pdef() -> int:
    pdefense = round((ps.vitality() * 2) + (ps.strength() * 0.5))
    return pdefense


def mdef() -> int:
    mdefense = round((ps.vitality() * 2) + (ps.intelligence() * 0.5))
    return mdefense


def matk() -> int:
    mattack = round((ps.intelligence() * 2) + (ps.dexterity() * 1) + (ps.agility() * 0.5))
    return mattack


def printStats() -> None:
    print(f"Patk ={patk()}")
    print(f"Matk = {matk()}")
    print(f"HP = {hp()}")
    print(f"Defense = {pdef()}")
    print(f"MDefense = {mdef()}")


printStats()