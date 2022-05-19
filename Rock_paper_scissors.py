import random

def play():
    user = input("'r' for rock, 'p' for paper and 's' for scissors")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'Its a draw.'
    if is_win(user, computer):
        return 'You win!'
    return 'you lose!'
    
def is_win(player, opponent):
    if player == 'r' and opponent == 's' or player == 's' and opponent == 'p' or player == 'r' and opponent == 's':
        return True

print(play())
    

