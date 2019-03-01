from random import randint


class NQPosition:
    def __init__(self, N):
        # choose some internal representation of the NxN board
        # put queens on it

        self.N = N
        self.board = []

        for i in range(0, N):
            j = randint(1, N)
            self.board.append(j)

        print(self.board)

    def value(self):
        # calculate number of conflicts (queens that can capture each other)
        value = 0

        # check row conflicts
        for i in range(0, self.N):
            for j in range(0, self.N):
                if i != j:
                    if self.board[i] == self.board[j]:
                        value += 1

        # check left and right diagonal conflicts
        for i in range(0, self.N):
            for x in range(1, self.N + 1):
                x0 = i + 1
                y0 = self.board[i]

                y_left = x - x0 + y0
                y_right = (x0 + y0) - x

                if 0 < y_left < self.N + 1:
                    if (x - 1 != i and y_left != self.board[i]) and (self.board[x - 1] == y_left):
                        value += 1

                if 0 < y_right < self.N + 1:
                    if (x - 1 != i and y_right != self.board[i]) and (self.board[x - 1] == y_right):
                        value += 1

        return value

    def make_move(self, move):
        # actually execute a move (change the board)
        x = move[0]
        y_new = move[1]
        self.board[x - 1] = y_new

    def best_move(self):
        # find the best move and the value function after making that move
        value = NQPosition.value(self)
        print("New value: ", value)

        if value == 0:
            return None, value

        while True:
            x = randint(1, self.N)
            y_new = randint(1, self.N)
            move = (x, y_new)

            NQPosition.make_move(self, move)
            best_value = NQPosition.value(self)

            if best_value <= value:
                value = best_value
                break

        print(self.board)

        return move, value
