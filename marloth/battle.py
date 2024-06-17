import random as rd

from marloth import enemyattr as en, enemyskill as es, playerattr as pa, warriorskill

from marloth import status


def mechanics(hp, damage=0) -> int:
    reduction = en.enemyreductions()
    finaldamage = damage * ((100 - reduction) / 100)
    finalhp = hp - finaldamage
    return round(finalhp)


def skillSelect(enemyhp, skill=None) -> int:
    while skill is None:
        try:
            skill = int(input("Your choice :  "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if skill == 1:
            damage = warriorskill.provoke()
            enemyhp = mechanics(enemyhp, damage)
            print(f"Provoke Damage : {damage} | Enemy Hp {enemyhp}")

        elif skill == 2:
            damage = warriorskill.rendersword()
            enemyhp = mechanics(enemyhp, damage)
            print(f"Render Sword Damage : {damage} | Enemy Hp {enemyhp}")

        elif skill == 3:
            damage = warriorskill.combosword()
            enemyhp = mechanics(enemyhp, damage)
            print(f"Combo Sword Damage : {damage} | Enemy Hp {enemyhp}")

        elif skill == 4:
            damage = warriorskill.cutthrough()
            enemyhp = mechanics(enemyhp, damage)
            print(f"Cut Through Damage : {damage} | Enemy Hp {enemyhp}")

        elif skill == 5:
            damage = warriorskill.burningoath()
            enemyhp = mechanics(enemyhp, damage)
            print(f"Burning Oath Damage : {damage} | Enemy Hp {enemyhp}")

        elif skill == 0:
            print("You did nothing!")

        else:
            print("Invalid choice, please try again.")
            skill = None

    return enemyhp


def enemySkill(playerHp) -> int:
    enemyDo = rd.randint(1, 6)
    if enemyDo == 1:
        damageTaken = es.claw()
        playerHp = mechanics(playerHp, damageTaken)
        print(f"Enemy use claw and dealt {damageTaken} | Your Hp {playerHp}")

    elif enemyDo == 2:
        damageTaken = es.roar()
        playerHp = mechanics(playerHp, damageTaken)
        print(f"Enemy use roar and dealt {damageTaken} | Your Hp {playerHp}")

    elif enemyDo == 3:
        damageTaken = es.throw()
        playerHp = mechanics(playerHp, damageTaken)
        print(f"Enemy use throw and dealt {damageTaken} | Your Hp {playerHp}")

    elif enemyDo == 4:
        damageTaken = es.plunge()
        playerHp = mechanics(playerHp, damageTaken)
        print(f"Enemy use plunge and dealt {damageTaken} | Your Hp {playerHp}")

    elif enemyDo == 5:
        damageTaken = es.slash()
        playerHp = mechanics(playerHp, damageTaken)
        print(f"Enemy use slash and dealt {damageTaken} | Your Hp {playerHp}")

    elif enemyDo == 6:
        damageTaken = es.chomp()
        playerHp = mechanics(playerHp, damageTaken)
        print(f"Enemy use chomp and dealt : {damageTaken} | Your Hp {playerHp}")

    else:
        print("You evaded !")

    return playerHp


def turn(n) -> None:
    print("")
    print(f"========= TURN {n} =========")


def main() -> None:
    print("Choose your skill : ")
    print("1. Provoke      2. Render Sword")
    print("3. Combo Sword  4. Cut Through")
    print("5. Burning Oath 0. Do Nothing")

    enemyhp = en.enemyhp()
    playerhp = pa.hp()

    n = 1

    while True:
        turn(n)
        enemyhp = skillSelect(enemyhp)
        playerhp = enemySkill(playerhp)
        n = n + 1

        if enemyhp <= 0:
            print("You won my nigga")
            break
        if playerhp <= 0:
            print("You lost my nigga")
            break


if __name__ == '__main__':
    main()
