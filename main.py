import random

cpu_deck = ['rock', 'scissor', 'paper']
player_score = 0
cpu_score = 0
entry = ['r', 'rock', 's', 'scissor', 'p', 'paper']
flag = True
while flag:
    round_string = input(print("how many wins to finish the game? "))
    try:
        rounds = int(round_string)
        flag = False
    except (TypeError, ValueError):
        print("This is not an integer number. Please enter a valid number")

while 1:
    player = input(print('type "r" or Rock, "s" or scissor , p or "paper"')).lower()
    if player not in entry:
        continue
    random.shuffle(cpu_deck)
    if player == 'r' or player == 'rock':
        if cpu_deck[0] == 'scissor':
            print("player wins, rock is player  and {} is cpu ".format(cpu_deck[0]))
            player_score += 1

    if player == 'r' or player == 'rock':
        if cpu_deck[0] == 'paper':
            print("CPU wins, rock is player  and {} is cpu ".format(cpu_deck[0]))
            cpu_score += 1

    if player == 's' or player == 'scissor':
        if cpu_deck[0] == 'paper':
            print("player wins, scissor is player  and {} is cpu ".format(cpu_deck[0]))
            player_score += 1
    if player == 's' or player == 'scissor':
        if cpu_deck[0] == 'r':
            print("CPU wins, scissor is player  and {} is cpu ".format(cpu_deck[0]))
            cpu_score += 1

    if player == 'p' or player == 'paper':
        if cpu_deck[0] == 'rock':
            print("player wins, paper is player  and {} is cpu ".format(cpu_deck[0]))
            player_score += 1
    if player == 'p' or player == 'paper':
        if cpu_deck[0] == 'scissor':
            print("CPU wins, scissor is player  and {} is cpu ".format(cpu_deck[0]))
            cpu_score += 1

    if player == cpu_deck[0]:
        print("Tie !, {} is player  and {} is cpu ".format(player, cpu_deck[0]))

    print(player_score, cpu_score)

    if cpu_score == rounds:
        print("cpu won the game")
        break
    if player_score == rounds:
        print("player won the game")
