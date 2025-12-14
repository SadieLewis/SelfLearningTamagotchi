class QTable:
    def __init__(self, states, actions, start_state, target_visits=10, rate_constant=10, discount=0.9):
        self.q = [[0.0 for _ in range(actions)] for _ in range(states)]
        self.visits = [[0 for _ in range(actions)] for _ in range(states)]
        self.target_visits = target_visits
        self.rate_constant = rate_constant
        self.discount = discount
        self.last_state = start_state
        self.last_action = 0

    # learning rate
    def get_learning_rate(self, state, action):
        total_visits = self.visits[state][action]
        return 1 / (1 + (total_visits / self.rate_constant))

    # exploit
    def get_best_action(self, state):
        return max(range(len(self.q[state])), key=lambda a: self.q[state][a])

    def is_exploring(self, state):
        return any(v < self.target_visits for v in self.visits[state])

    # explore
    def least_visited_action(self, state):
        return min(range(len(self.visits[state])),
                   key=lambda a: self.visits[state][a])

    # sense, act, learn
    def sense_act_learn(self, new_state, reward):
        lr = self.get_learning_rate(self.last_state, self.last_action)
        best_next_action = self.get_best_action(new_state)
        max_next_q = self.q[new_state][best_next_action]
        current_q = self.q[self.last_state][self.last_action]
        new_q = (1 - lr) * current_q + lr * (reward + self.discount * max_next_q)
        self.q[self.last_state][self.last_action] = new_q
        self.visits[self.last_state][self.last_action] += 1
        if self.is_exploring(new_state):
            action = self.least_visited_action(new_state)
        else:
            action = self.get_best_action(new_state)
        self.last_state = new_state
        self.last_action = action
        return action