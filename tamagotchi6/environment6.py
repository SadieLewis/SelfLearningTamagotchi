import random
class TamagotchiEnv:
    def __init__(self):
        self.states = ["hungry", "energetic", "sleepy", "angry", "dizzy", "scared"]
        self.actions = ["eat", "play", "rest", "calm", "catch", "hug"]
        self.correct_pairs = {
            #hungry & eat
            0:0,
            #energetic & play
            1:1,
            #sleepy & rest
            2:2,
            #angry & calm
            3:3,
            #dizzy & catch
            4:4,
            #scared & hug
            5:5
        }
        self.num_states = len(self.states)
        self.num_actions = len(self.actions)
        self.state = None

    def reset(self):
        self.state = random.randint(0, self.num_states - 1)
        return self.state

    def step(self, action):
        if action == self.correct_pairs[self.state]:
            reward = 10
        else:
            reward = -5
        self.state = random.randint(0, self.num_states - 1)
        return self.state, reward