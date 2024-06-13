import random as rd

from marloth.skill import warriorskill
from marloth.enemy import enemyattr as en
from marloth.player import playerattr as pa
from marloth.enemy import enemyskill as es

def enemyMechanics(enemyhp, damage=0):
    enemyfinalhp = enemyhp - damage
    return enemyfinalhp


def playerMechanics(playerhp, damage=0):
    playerfinalhp = playerhp - damage
    return playerfinalhp


def skillSelect(enemyhp, skill=None):
    while skill is None:
        try:
            skill = int(input("Your choice :  "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if skill == 1:
            damage = warriorskill.provoke()
            enemyhp = enemyMechanics(enemyhp, damage)
            print(f"Provoke Damage : {damage} | Enemy Hp {enemyhp}")

        elif skill == 2:
            damage = warriorskill.rendersword()
            enemyhp = enemyMechanics(enemyhp, damage)
            print(f"Render Sword Damage : {damage} | Enemy Hp {enemyhp}")

        elif skill == 3:
            damage = warriorskill.combosword()
            enemyhp = enemyMechanics(enemyhp, damage)
            print(f"Combo Sword Damage : {damage} | Enemy Hp {enemyhp}")

        elif skill == 4:
            damage = warriorskill.cutthrough()
            enemyhp = enemyMechanics(enemyhp, damage)
            print(f"Cut Through Damage : {damage} | Enemy Hp {enemyhp}")

        elif skill == 0:
            print("You did nothing!")

        else:
            print("Invalid choice, please try again.")
            skill = None  # Reset skill to None to re-enter the loop

    return enemyhp  # Return the updated enemy HP

def enemySkill():
    enemyDo = rd.randint(1,6)

def main():
    print("Choose your skill : ")
    print("1. Provoke      2. Render Sword")
    print("3. Combo Sword  4. Cut Through")
    print("0. Do Nothing")
    enemyhp = en.enemyhp()
    playerhp = pa.hp()

    while True:
        enemyhp = skillSelect(enemyhp)

        if enemyhp <= 0:
            print("You won")
            break


if __name__ == '__main__':
    main()
