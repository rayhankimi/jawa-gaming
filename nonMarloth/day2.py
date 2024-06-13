import random as rd

strn = 100
vit = 40
patk = 400


def provoke(base=30) -> int:
    vitMul = vit * 0.1
    strnMul = strn * 0.05
    damage = base + (base * vitMul) + (base * strnMul) + (patk * 0.3)
    return damage


def rendersword(base=70) -> int:
    strnMul = strn * 0.1
    damage = base + (base * strnMul) + (patk * 0.5)
    return damage


def combosword(base=100) -> int:
    strnMul = strn * 0.1
    damage = base + (base * strnMul) + (patk * 0.5)
    return damage


def enemy(hp=1500, damage=0) -> int:
    finalHp = hp - damage
    return finalHp


def main():
    enemyHp = 1500
    while True:
        print("1. Provoke")
        print("2. Rendersword")
        print("3. Combosword")

        skillselect = None
        while skillselect is None:
            try:
                skillselect = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a valid number.")

        if skillselect == 1:
            damage = provoke()
            enemyHp = enemy(enemyHp, damage)
            print(f"Enemy Hp : {enemyHp}")
            print(f"You dealt {damage}")

        elif skillselect == 2:
            damage = rendersword()
            enemyHp = enemy(enemyHp, damage)
            print(f"Enemy Hp : {enemyHp}")
            print(f"You dealt {damage}")

        elif skillselect == 3:
            damage = combosword()
            enemyHp = enemy(enemyHp, damage)
            print(f"Enemy Hp : {enemyHp}")
            print(f"You dealt {damage}")

        else:
            print("You didnt do anything!")

        if enemyHp < 0:
            print("You defeated the enemies")
            break


if __name__ == "__main__":
    main()
