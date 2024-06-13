import random as rd

def comp(hand):
    return rd.choice(hand)


def player(hand) -> str:
    while True:
        player_hand = input("Rock, Paper , or Scissor? : ").lower()
        if player_hand in hand:
            return player_hand
        print("Invalid Input")


def winner(player, comp):
    if player == comp:
        return 'Draw'
    elif (player == 'rock' and comp == 'paper') or \
            (player == 'paper' and comp == 'rock') or \
            (player == 'scissor' and comp == 'rock'):
        return 'Win'
    else:
        return 'Lose'


def main():
    hand = ['rock', 'paper', 'scissor']
    while True:
        player_hand = player(hand)
        comp_hand = comp(hand)
        print('Computer', comp_hand)
        print('Player', player_hand)
        result = winner(player_hand, comp_hand)
        print(result)
        try_again = input("Do you want to play again? (y/n) ").lower()
        if try_again not in ['y', 'yes']:
            break


if __name__ == "__main__":
    main()
