import warriorskill
from marloth import enemyattr as en


def mechanics(enemyhp, damage=0):
    enemyfinalhp = enemyhp - damage
    return enemyfinalhp


def main():
    print("Choose your skill : ")
    print("1. Provoke      2. Render Sword")
    print("3. Combo Sword  4. Cut Through")
    print("0. Do Nothing")
    enemyhp = en.enemyhp()

    while True:
        skill = None
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

            elif skill == 0:
                print("You did nothing!")

            else:
                print("Invalid choice, please try again.")
                skill = None  # Reset skill to None to re-enter the loop

        if enemyhp <= 0:
            print("You won, my nigga")
            break


if __name__ == '__main__':
    main()
