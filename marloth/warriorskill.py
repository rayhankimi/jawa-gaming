from marloth import playerattr as pa, playerstat as ps


def provoke(base=5) -> int:
    patk = pa.patk() * 0.05
    strnmul = ps.strength() * 0.05
    vitmul = ps.vitality() * 0.1
    agimul = ps.agility() * 0
    dexmul = ps.dexterity() * 0.05
    base = base + patk
    damage = base + (base * strnmul) + (base * vitmul) + (base + agimul) + (base + dexmul)

    return round(damage)


def rendersword(base=12) -> int:
    patk = pa.patk() * 0.1
    strnmul = ps.strength() * 0.08
    vitmul = ps.vitality() * 0.03
    agimul = ps.agility() * 0.03
    dexmul = ps.dexterity() * 0.03
    base = base + patk
    damage = base + (base * strnmul) + (base * vitmul) + (base + agimul) + (base + dexmul)

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
    patk = pa.patk() * 0.15
    strnmul = ps.strength() * 0.075
    vitmul = ps.vitality() * 0.025
    agimul = ps.agility() * 0.025
    dexmul = ps.dexterity() * 0.025
    base = base + patk
    damage = base + (base * strnmul) + (base * vitmul) + (base + agimul) + (base + dexmul)

    return round(damage)


def burningoath(base=15) -> int:
    patk = pa.patk() * 0.15
    strnmul = ps.strength() * 0.075
    vitmul = ps.vitality() * 0.025
    agimul = ps.agility() * 0.025
    dexmul = ps.dexterity() * 0.025
    base = base + patk
    damage = base + (base * strnmul) + (base * vitmul) + (base + agimul) + (base + dexmul)

    return round(damage)
