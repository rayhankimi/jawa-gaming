from marloth import playerattr as pa, playerstat as ps


def provoke(base=30) -> int:
    vitMul = ps.vitality() * 0.1
    strnMul = ps.strength() * 0.05
    damage = base + (base * vitMul) + (base * strnMul) + (pa.patk() * 0.3)
    return damage


def rendersword(base=70) -> int:
    strnMul = ps.strength() * 0.1
    damage = base + (base * strnMul) + (pa.patk() * 0.5)
    return damage


def combosword(base=100) -> int:
    strnMul = ps.strength() * 0.1
    damage = base + (base * strnMul) + (pa.patk() * 0.5)
    return damage


def cutthrough(base=100) -> int:
    strnMul = ps.strength() * 0.15
    damage = base + (base * strnMul) + (pa.patk() * 0.3)
    return damage


def burningoath(base=100) -> int:
    vitMul = ps.vitality() * 0.1
    strnMul = ps.strength() * 0.05
    damage = base + (base * vitMul) + (base * strnMul) + (pa.hp() * 0.01)
    return damage
