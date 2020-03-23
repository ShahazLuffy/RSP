import random

cpu_deck = ['r', 's', 'p']
player_score = 0
cpu_score = 0
rounds = input(print("how many wins to finish the game? "))
while 1:

    # cpu = random.randint(1,3)
    player = input(print('type "r" for Rock, "s" for scissor , p for "paper"')).lower()
    random.shuffle(cpu_deck)
    if player == 'r':
        if cpu_deck[0] == 's':
            print("player wins, {} is player  and {} is cpu ".format(player, cpu_deck[0]))
            player_score +=1

    if player == 'r':
        if cpu_deck[0] == 'p':
            print("CPU wins, {} is player  and {} is cpu ".format(player, cpu_deck[0]))
            cpu_score+=1

    if player == 's':
        if cpu_deck[0] == 'p':
            print("player wins, {} is player  and {} is cpu ".format(player, cpu_deck[0]))
            player_score += 1
    if player == 's':
        if cpu_deck[0] == 'r':
            print("CPU wins, {} is player  and {} is cpu ".format(player, cpu_deck[0]))
            cpu_score +=1

    if player == cpu_deck[0]:
        print("Tie !, {} is player  and {} is cpu ".format(player, cpu_deck[0]))

    print(player_score, cpu_score)

    if cpu_score == rounds:
        print("cpu won the game")
        break
    if player_score == rounds:
        print("player won the game")
