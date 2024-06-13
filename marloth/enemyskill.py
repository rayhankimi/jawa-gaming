from marloth import enemyattr as ena


def claw(base=10) -> int:
    damage = base * (ena.enemyatk() * 0.2)
    return damage


def roar(base=12) -> int:
    damage = base * (ena.enemyatk() * 0.15)
    return damage


def throw(base=10) -> int:
    damage = base * (ena.enemyatk() * 0.3)
    return damage


def plunge(base=7) -> int:
    damage = base * (ena.enemyatk() * 0.4)
    return damage


def slash(base=10) -> int:
    damage = base * (ena.enemyatk() * 0.5)
    return damage


def chomp(base=15) -> int:
    damage = base * (ena.enemyatk() * 0.3)
    return damage
