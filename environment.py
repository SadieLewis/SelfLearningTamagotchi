import random
class TamagotchiEnv:
    def __init__(self):
        self.state = None
        self.states = ["hungry", "energetic", "sleepy"]
        self.actions = ["eat", "play", "rest"]
        self.correct_pairs = {
            "hungry": "eat",
            "energetic": "play",
            "sleepy": "rest"
        }
        self.reset()

    def reset(self):
        self.state = random.choice(self.states)
        return self.state

    def step(self, action):
        # Takes an action and returns next_state, reward
        if action == self.correct_pairs[self.state]:
            reward = 10
        else:
            reward = -5
        self.state = random.choice(self.states)
        return self.state, reward