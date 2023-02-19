import random
import itertools


players = int(input("Enter the numbers of players: "))
dices = int(input("Enter the numbers of dices: "))

score = {}
evaluation = {}
dice_player = []
numbers_of_dice = [1, 2, 3, 4, 5, 6]
# Create players
for player in range(players):
    score["Player#{0}".format(player+1)] = 0
    evaluation["Player#{0}".format(player+1)] = []
for i in range(players):
    dice_player.append(dices)

for x in itertools.count():
    print("Giliran "+ str(x+1) +" lempar dadu :")
    for index, player_dice in enumerate(dice_player, start=1):
        for x in range(player_dice):
            number_of_dice = random.choice(numbers_of_dice)
            evaluation["Player#{0}".format(index)].append(number_of_dice)
    give_to_next = []
    give_now = []
    give = False
    for index, player_dice in enumerate(dice_player, start=1):
        get_by_player = evaluation["Player#"+str(index)]
        get_by_player_eva = get_by_player.copy()
        print("Player#"+str(index)+": "+str(get_by_player))
        if len(get_by_player) == 0:
            continue
        else:
            for index_number, number in enumerate(get_by_player, start=1):
                if number == 6:
                    get_by_player_eva.remove(number)
                    # index_number = 0
                    dice_player[index-1] = dice_player[index-1] -1
                    score["Player#"+str(index)] = score["Player#"+str(index)] + 1
                elif number == 1:
                    get_by_player_eva.remove(number)
                    give_to_next.append(1)
                    dice_player[index-1] = dice_player[index-1] -1

            if give == True:
                for i in give_now:
                    get_by_player_eva.append(i)
                    dice_player[index-1] = dice_player[index-1] + 1
                give_now.clear()
                give = False

            if len(give_to_next) != 0:
                if index == len(dice_player):
                    for i in give_to_next:
                        for j in itertools.count():
                            first_player = j + 1
                            if len(evaluation["Player#"+str(first_player)]) == 0:
                                continue
                            else:
                                evaluation["Player#"+str(first_player)].append(i)
                                break
                        dice_player[0] = dice_player[0] + 1
                else:
                    give = True
                    give_now = give_to_next.copy()
                give_to_next.clear()

            evaluation["Player#"+str(index)] = get_by_player_eva
    print("Setelah evaluasi :")
    player_win = 0
    for key, value  in evaluation.items():
        if len(value) == 0:
            player_win = player_win+1
        print(key+": "+str(value))
        evaluation[key].clear()
    print("Score: "+str(score))
    print("======================")
    print("")
    if player_win == players-1:
        break

print("Game has been ended :")
for key, value  in score.items():
    print(key+": "+str(value))
max_value = max(score, key=score.get)
print("The winer is: "+ str(max_value))
print("with score: "+ str(score[max_value]))
