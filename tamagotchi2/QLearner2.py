from tamagotchi.QTable import QTable
class QLearner:
    def __init__(self, num_states, num_actions):
        self.qtable = QTable(num_states, num_actions, start_state=0)

    def act_and_learn(self, new_state, reward):
        return self.qtable.sense_act_learn(new_state, reward)

    @property
    def last_action(self):
        return self.qtable.last_action