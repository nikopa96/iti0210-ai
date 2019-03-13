import random

AI = 0
PLAYER = 1

ROLL = 0
PASS = 1


def pig_game(ai_func):
    rolled = 0
    turn = PLAYER
    player_points = ai_points = 0

    while player_points < 100 and ai_points < 100:
        print("Your points", player_points,  "AI points", ai_points, "holding", rolled)

        if turn == PLAYER:
            decision = ROLL
            if rolled > 0:
                s = input("Do you want to keep rolling (Y/n)? ")
                if len(s) > 0 and s[0].lower() == "n":
                    decision = PASS

            if decision == PASS:
                rolled = 0
                turn = AI
            else:
                dieroll = random.randint(1, 6)
                print("You rolled...", dieroll)
                if dieroll == 1:
                    player_points -= rolled # lose all points again
                    rolled = 0
                    turn = AI
                else:
                    rolled += dieroll
                    player_points += dieroll

        else:
            decision = ai_func(turn, rolled, ai_points, player_points)
            if decision == PASS:
                print("-- AI decides to pass.")
                rolled = 0
                turn = PLAYER
            else:
                dieroll = random.randint(1, 6)
                print("-- AI rolled...", dieroll)
                if dieroll == 1:
                    ai_points -= rolled # lose all points again
                    rolled = 0
                    turn = PLAYER
                else:
                    rolled += dieroll
                    ai_points += dieroll

    if player_points >= 100:
        print("You won!")
    elif ai_points >= 100:
        print("AI won.")


def dummy_ai(turn, rolled, my_points, opp_points):
    if rolled < 21:
        return ROLL
    else:
        return PASS


def minimax_ai(turn, rolled, my_points, opp_points):
    new_value = exp_minimax(turn, False, rolled, my_points, opp_points, 4)
    print('================ NEW VALUE', new_value)

    if new_value <= 0.10:
        return ROLL
    else:
        return PASS


def exp_minimax(turn, chance, rolled, my_points, opp_points, depth):
    a = 0

    # case 1a: somebody won, stop searching
    # return a high value if AI wins, low if it loses.
    if my_points + rolled >= 100:
        return 1
    if opp_points >= 100:
        return -1

    # case 1b: out of depth, stop searching
    # return game state eval (should be between win and loss)
    if depth < 1:
        return (my_points + rolled - opp_points) / 100

    # case 2: AI's turn (and NOT a chance node):
    # return max value of possible moves (recursively)
    if turn == AI and not chance:
        # max value of possible moves (recursively)
        max_value = -100000

        max_value = max(max_value, exp_minimax(AI, True, rolled, my_points, opp_points, depth - 1))
        max_value = max(max_value, exp_minimax(PLAYER, False, rolled, opp_points, my_points, depth - 1))
        a = max_value
    # case 3: player's turn:
    # return min value (assume optimal action from player)
    elif turn == PLAYER and not chance:
        # min value (assume optimal action from player)
        min_value = 100000

        min_value = min(min_value, exp_minimax(PLAYER, True, rolled, my_points, opp_points, depth - 1))
        min_value = min(min_value, exp_minimax(AI, False, rolled, opp_points, my_points, depth - 1))
        a = min_value
    # case 4: chance node:
    # return average of all dice rolls
    elif chance:
        # average of all dice rolls
        average = 0

        if turn == AI:
            average = average + (1/6 * exp_minimax(PLAYER, False, 0, opp_points, my_points, depth - 1))
            for i in range(2, 7):
                average = average + (1/6 * exp_minimax(AI, False, rolled + i, my_points, opp_points, depth - 1))
        else:
            average = average + (1/6 * exp_minimax(AI, False, 0, opp_points, my_points, depth - 1))
            for i in range(2, 7):
                average = average + (1/6 * exp_minimax(PLAYER, False, rolled + i, my_points, opp_points, depth - 1))

        a = average

    return a


if __name__ == '__main__':
    pig_game(minimax_ai)
