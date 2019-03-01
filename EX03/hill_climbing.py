from EX03.nq_position import NQPosition


def hill_climbing(pos):
    curr_value = pos.value()
    while True:
        move, new_value = pos.best_move()
        if new_value == curr_value == 0:
            # no improvement, give up
            return pos, curr_value
        else:
            # position improves, keep searching
            curr_value = new_value
            pos.make_move(move)


if __name__ == '__main__':
    pos = NQPosition(8)  # test with the tiny 4x4 board first
    print("Initial position value", pos.value())

    best_pos, best_value = hill_climbing(pos)
    print("Final value", best_value)
    # if best_value is 0, we solved the problem
