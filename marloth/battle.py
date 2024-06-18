import random as rd

from marloth import enemyattr as en, enemyskill as es, playerattr as pa, warriorskill

from marloth import status


def attackMechanics(hp, damage=0) -> int:
    reduction = en.enemyreductions()
    finaldamage = round(damage * ((100 - reduction) / 100))
    finalhp = round(hp - finaldamage)
    print(f"{finaldamage} , Enemy Hp : {finalhp}")
    return finalhp


def defenseMechanics(hp, damage=0) -> int:
    reduction = pa.playerReductions()
    finaldamage = round(damage * ((100 - reduction) / 100))
    finalhp = round(hp - finaldamage)
    print(f"{finaldamage} | Your Hp {hp}")
    return finalhp


def skillSelect(enemyhp, skill=None) -> int:
    while skill is None:
        try:
            skill = int(input("Your choice :  "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if skill == 1:
            damage = warriorskill.provoke()
            print("You cast Provoke and dealt :", end=" ")
            enemyhp = attackMechanics(enemyhp, damage)

        elif skill == 2:
            damage = warriorskill.rendersword()
            print("You cast Render Sword and dealt :", end=" ")
            enemyhp = attackMechanics(enemyhp, damage)

        elif skill == 3:
            damage = warriorskill.combosword()
            print("You cast Combo Sword and dealt :", end=" ")
            enemyhp = attackMechanics(enemyhp, damage)

        elif skill == 4:
            damage = warriorskill.cutthrough()
            print("You cast Cut Through and dealt :", end=" ")
            enemyhp = attackMechanics(enemyhp, damage)


        elif skill == 5:
            damage = warriorskill.burningoath()
            print("You cast Burning Oath and dealt :", end=" ")
            enemyhp = attackMechanics(enemyhp, damage)


        elif skill == 0:
            print("You did nothing!")

        else:
            print("Invalid choice, please try again.")
            skill = None

    return enemyhp


def enemySkill(hp) -> int:
    enemyDo = rd.randint(1, 6)
    if enemyDo == 1:
        damageTaken = es.claw()
        print(f"Enemy use claw and dealt :", end=" ")
        hp = defenseMechanics(hp, damageTaken)

    elif enemyDo == 2:
        damageTaken = es.roar()
        print(f"Enemy use roar and dealt :", end=" ")
        hp = defenseMechanics(hp, damageTaken)

    elif enemyDo == 3:
        damageTaken = es.throw()
        print(f"Enemy use throw and dealt :", end=" ")
        hp = defenseMechanics(hp, damageTaken)

    elif enemyDo == 4:
        damageTaken = es.plunge()
        print(f"Enemy use plunge and dealt :", end=" ")
        hp = defenseMechanics(hp, damageTaken)

    elif enemyDo == 5:
        damageTaken = es.slash()
        print(f"Enemy use slash and dealt :", end=" ")
        hp = defenseMechanics(hp, damageTaken)

    elif enemyDo == 6:
        damageTaken = es.chomp()
        print(f"Enemy use chomp and dealt :", end=" ")
        hp = defenseMechanics(hp, damageTaken)

    else:
        print("You evaded !")

    return hp


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
