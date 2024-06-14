from marloth import playerattr as pa, playerstat as ps


def provoke(base=5) -> int:
    vitMul = ps.vitality() * 0.1
    strnMul = ps.strength() * 0.05
    damage = base + (base * vitMul) + (base * strnMul) + (pa.patk() * 0.3)
    return round(damage)


def rendersword(base=12) -> int:
    strnMul = ps.strength() * 0.1
    atkmul = pa.patk() * 0.15
    damage = base + (atkmul * strnMul)
    return round(damage)


def combosword(base=15) -> int:
    patk = pa.patk() * 0.15
    strnmul = ps.strength() * 0.1
    vitmul = ps.vitality() * 0.05
    agimul = ps.agility() * 0.05
    dexmul = ps.dexterity() * 0.05

    base = base + patk
    damage = base + (base * strnmul) + (base * vitmul) + (base + agimul) + (base + dexmul)
    return round(damage)


def cutthrough(base=10) -> int:
    strnMul = ps.strength() * 0.15
    damage = base + (base * strnMul) + (pa.patk() * 0.3)
    return round(damage)


def burningoath(base=15) -> int:
    vitMul = ps.vitality() * 0.1
    strnMul = ps.strength() * 0.05
    damage = base + (base * vitMul) + (base * strnMul) + (pa.hp() * 0.01)
    return round(damage)
