import enemyattr as ena

def claw(base = 100) -> int:
    damage = base * (ena.enemyatk() * 0.2)
    return damage
