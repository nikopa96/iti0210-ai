class QLearner:
    def __init__(self):
        self.Q = {}
        self.gamma = 0.8    # discount factor
        self.alpha = 0.05   # learning rate

    def update(self, s, action, reward, s_prim):
        # s - old state (my points, opp points, rolled)
        # action - action taken from state s
        # reward - 0 usually, 100 if I won, -100 if I lost
        # s_prim - new state. What happened after my action was taken

        ROLL = 0
        PASS = 1

        if s in self.Q and s_prim in self.Q:
            max_Q = max(self.Q[s_prim][PASS], self.Q[s_prim][ROLL])
            self.Q[s][action] += self.alpha * (reward + self.gamma * max_Q - self.Q[s][action])
        else:
            self.Q[s] = {}
            self.Q[s][PASS] = 0
            self.Q[s][ROLL] = 0
            self.Q[s][action] = reward

    def get_Q(self):
        return self.Q
