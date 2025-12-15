import pygame
from QLearner6 import QLearner
from environment6 import TamagotchiEnv
# use tarakotchi sprites

def start_screen(window):
    window_size = window.get_size()
    pygame.display.set_caption("Self Learning Tamagotchi")
    texts = [
        ("Self Learning Tamagotchi", 'ravie', 37, "white"),
        ("You have a new tamagotchi friend!", 'lucidasanstypewriter', 16, "lightpink2"),
        ("Once you start it up, it will start learning how to care for itself!", 'lucidasanstypewriter', 16, "lightpink2"),
        ("If it does well it will get a reward", 'lucidasanstypewriter', 16, "lightpink2"),
        ("If it does poorly it will get a punishment", 'lucidasanstypewriter', 16, "lightpink2"),
        #dramatic spacing
        ("", 'lucidasanstypewriter', 16, "lightpink2"),
        ("Watch it learn and enjoy your new friend, completely independent!", 'lucidasanstypewriter', 16, "lightpink2"),
        ("Press enter/return to start", 'copperplategothic', 20, "white")
    ]
    text_positions = [
        (window_size[0] // 2, window_size[1] // 8),
        (window_size[0] // 2, window_size[1] // 4.5),
        (window_size[0] // 2, window_size[1] // 3.8),
        (window_size[0] // 2, window_size[1] // 3.25),
        (window_size[0] // 2, window_size[1] // 2.85),
        (window_size[0] // 2, window_size[1] // 2.55),
        (window_size[0] // 2, window_size[1] // 2.45),
        (window_size[0] // 2, window_size[1] // 1.03)
    ]
    rendered_texts = []
    #assign fonts, txt colors, size
    for txt, font_name, size, color in texts:
        font = pygame.font.Font(pygame.font.match_font(font_name), size)
        rendered_texts.append(font.render(txt, True, color))
    images = {
        "tamagotchi": ("pinktamagotchi.png", (250, 330), (window_size[0] // 2, window_size[1] // 1.48)),
        "happy": ("happytama.png", (90, 110), (window_size[0] // 2, window_size[1] // 1.43)),
    }
    rendered_images = {}
    #assign position and size
    for key, (file, size, pos) in images.items():
        img = pygame.image.load(file).convert_alpha()
        img = pygame.transform.scale(img, size)
        img_rect = img.get_rect(center=pos)
        rendered_images[key] = (img, img_rect)
    window.fill("maroon4")
    #display everything
    for txt, pos in zip(rendered_texts, text_positions):
        window.blit(txt, txt.get_rect(center=pos))
    for img, img_rect in rendered_images.values():
        window.blit(img, img_rect)
    pygame.display.flip()
    go = True
    while go:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    go = False
            elif event.type == pygame.QUIT:
                pygame.quit(); exit()

def sim_screen(window, env, agent):
    #for pacing
    clock = pygame.time.Clock()
    window_size = window.get_size()
    font = pygame.font.Font(pygame.font.match_font('copperplategothic'), 30)
    font1 = pygame.font.Font(pygame.font.match_font('copperplategothic'), 20)
    #image-state correlation
    state_images = {
        0: pygame.transform.scale(pygame.image.load("hungrytama.png"), (110, 140)),
        1: pygame.transform.scale(pygame.image.load("energetictama.png"), (110, 140)),
        2: pygame.transform.scale(pygame.image.load("sleepytama.png"), (110, 140)),
        3: pygame.transform.scale(pygame.image.load("angrytama.png"), (110, 140)),
        4: pygame.transform.scale(pygame.image.load("dizzytama.png"), (110, 140)),
        5: pygame.transform.scale(pygame.image.load("scaredtama.png"), (110, 140)),
    }
    tama_img = pygame.transform.scale(
        pygame.image.load("pinktamagotchi.png").convert_alpha(), (400, 550)
    )
    #locate images
    img_rect = list(state_images.values())[0].get_rect(
        center=(window_size[0] // 2, window_size[1] // 2.35)
    )
    tama_rect = tama_img.get_rect(
        center=(window_size[0] // 2, window_size[1] // 2.57)
    )
    state = env.reset()
    reward = 0
    reward_total = 0
    agent.act_and_learn(state, reward)
    iteration_count = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        #starts Qlearning
        action = agent.last_action
        next_state, reward = env.step(action)
        reward_total += reward
        iteration_count += 1
        #tracks matching for visuals
        if reward > 0:
            match_str = "Correct match!"
        else:
            match_str = "Wrong match!"
        window.fill("maroon4")
        # displays updating images
        window.blit(tama_img, tama_rect)
        window.blit(state_images.get(state, state_images[0]), img_rect)
        # display updating data#display updating data
        window.blit(font1.render(f"Iterations: {iteration_count}", True, "lightpink2"), (10,630))
        window.blit(font.render(f"State: {env.states[state]}", True, "lightpink2"), (245, 570))
        window.blit(font.render(f"Action: {env.actions[action]}", True, "lightpink2"), (245, 600))
        window.blit(font.render(f"Reward: {reward_total}", True, "lightpink2"), (245, 630))
        window.blit(font.render(match_str, True, "lightpink2"), (245, 660))
        pygame.display.flip()
        #switch state and next state
        agent.act_and_learn(next_state, reward)
        state = next_state
        #faster because it takes a long time
        clock.tick(10)


def main():
    pygame.init()
    window = pygame.display.set_mode((700, 700))
    env = TamagotchiEnv()
    agent = QLearner(env.num_states, env.num_actions)
    start_screen(window)
    sim_screen(window, env, agent)


if __name__ == "__main__":
    main()
