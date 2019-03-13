NO_PLAYER = 0
PLAYER_X = 1
PLAYER_O = 2

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


def getAvailableMoves():
    available_moves = []

    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == NO_PLAYER:
                available_moves.append((i, j))

    return available_moves


def hasWinner(player):
    # check left diagonal
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] == player:
        return True

    # check right diagonal
    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] == player:
        return True

    # check rows and columns
    for i in range(0, len(board)):
        if (board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] == player) \
                or (board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] == player):
            return True

    return False


def getBoard():
    for row in board:
        print(str(row[0]) + '\t' + str(row[1]) + '\t' + str(row[2]))
    print('\n')


def inputValue():
    value = input("Input value (x, y): ")
    value_as_list = [int(n) for n in value.split(',')]
    point = tuple(value_as_list)

    x = point[0]
    y = point[1]

    board[x][y] = PLAYER_O
    getBoard()


def dummy_ai():
    available_moves = getAvailableMoves()

    if not available_moves:
        print('Game over')
    else:
        point = available_moves[0]
        x = point[0]
        y = point[1]

        board[x][y] = PLAYER_X

        print(getBoard())


def minimax_ai(turn):
    # this is the top level of search
    # we search all possible moves
    # (PASS and ROLL in case of the Pig game)
    # and pick the one that returns the highest minimax estimate
    best_move = None
    best_value = -2
    available_moves = getAvailableMoves()
    for move in available_moves:
        x = move[0]
        y = move[1]
        board[x][y] = turn

        v = minimax(-turn, 4)
        if v > best_value:
            best_value = v
            best_move = move

        board[x][y] = NO_PLAYER

    print('Chosen point: ', best_move)
    return best_move


def minimax(turn, depth):
    depth = depth - 1

    # case 1a: somebody won, stop searching
    # return a high value if AI wins, low if it loses.
    if hasWinner(PLAYER_X):
        return 1
    if hasWinner(PLAYER_O):
        return -1

    available_moves = getAvailableMoves()

    # end of search tree
    if not available_moves:
        return 0

    # case 1b: out of depth, stop searching
    # return game state eval (should be between win and loss)
    if depth < 1:
        return 0

    # case 2: AI's turn (and NOT a chance node):
    # return max value of possible moves (recursively)
    if turn == PLAYER_X:
        best_value = -2

        for move in available_moves:
            x = move[0]
            y = move[1]
            board[x][y] = PLAYER_X

            v = minimax(-turn, depth)

            if v > best_value:
                best_value = v
            print('For ', move, 'score is: ', best_value)
            getBoard()

            board[x][y] = NO_PLAYER

        return best_value
    # case 3: player's turn:
    # return min value (assume optimal action from player)
    else:  # turn != ai_side
        best_value = 2
        for move in available_moves:
            x = move[0]
            y = move[1]
            board[x][y] = PLAYER_O

            v = minimax(-turn, depth)
            if v < best_value:
                best_value = v

            board[x][y] = NO_PLAYER

        return best_value


def game():
    while getAvailableMoves():
        inputValue()
        if hasWinner(PLAYER_O):
            print('Player O has winner')
            break

        best_move = minimax_ai(PLAYER_X)
        board[best_move[0]][best_move[1]] = PLAYER_X
        print(getBoard())
        if hasWinner(PLAYER_X):
            print('Player X has winner')
            break


if __name__ == '__main__':
    game()
