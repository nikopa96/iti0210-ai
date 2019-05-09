import random

from EX09.qlearner import QLearner

AI = 0
PLAYER = 1

ROLL = 0
PASS = 1


def pig_game(ai_func_1, ai_func_2, q_learner_elem):
    rolled = 0
    turn = PLAYER
    player_points = ai_points = 0

    while player_points < 100 and ai_points < 100:
        print("Your points", player_points,  "AI points", ai_points, "holding", rolled)

        if turn == PLAYER:
            decision = ai_func_2(turn, rolled, ai_points, player_points, q_learner_elem)

            if decision == PASS:
                print("-- PLAYER decides to pass.")
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
            old_state = state_idx(ai_points, player_points, rolled)
            decision = ai_func_1(turn, rolled, ai_points, player_points, q_learner_elem)
            if decision == PASS:
                print("-- AI decides to pass.")
                rolled = 0
                turn = PLAYER

                new_state = state_idx(ai_points, player_points, rolled)
                q_learner_elem.update(old_state, PASS, 0, new_state)
            else:
                dieroll = random.randint(1, 6)
                print("-- AI rolled...", dieroll)
                if dieroll == 1:
                    ai_points -= rolled # lose all points again
                    rolled = 0
                    turn = PLAYER

                    new_state = state_idx(ai_points, player_points, rolled)
                    q_learner_elem.update(old_state, ROLL, -100, new_state)
                else:
                    rolled += dieroll
                    ai_points += dieroll

                    new_state = state_idx(ai_points, player_points, rolled)
                    q_learner_elem.update(old_state, ROLL, +100, new_state)

    if player_points >= 100:
        print("You won!")
        return PLAYER
    elif ai_points >= 100:
        print("AI won.")
        return AI


def state_idx(ai_points, opp_points, rolled):
    ap = min(ai_points//10, 10)    # ai points: 0-9, 10-19, ..., 90-99, 100
    op = min(opp_points//10, 10)
    r = min(rolled//5, 10)         # rolled: 0-4, 5-9, ..., 45-49, 50+
    return ap, op, r


def dummy_ai_1(turn, rolled, my_points, opp_points, q_learner_elem):
    Q = q_learner_elem.get_Q()
    current_state = state_idx(my_points, opp_points, rolled)

    if current_state in Q:
        Q_pass = Q[current_state][PASS]
        Q_roll = Q[current_state][ROLL]
        max_Q = max(Q_pass, Q_roll)

        if max_Q == Q_pass:
            return PASS
        else:
            return ROLL


def dummy_ai_2(turn, rolled, my_points, opp_points, q_learner_elem):
    if rolled < 21:
        return ROLL
    else:
        return PASS


if __name__ == '__main__':
    q_learner = QLearner()
    player_wins = 0
    ai_wins = 0

    for i in range(0, 1000):
        winner = pig_game(dummy_ai_2, dummy_ai_2, q_learner)

    for i in range(0, 100):
        winner = pig_game(dummy_ai_1, dummy_ai_2, q_learner)

        if winner == PLAYER:
            player_wins += 1
        else:
            ai_wins += 1

    print('Player wins:', player_wins)
    print('AI wins', ai_wins)
