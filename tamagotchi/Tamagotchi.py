import pygame
from QLearner import QLearner
from environment import TamagotchiEnv
# use tarakotchi sprites

def start_screen(window):
    window_size = window.get_size()
    pygame.display.set_caption("Self Learning Tamagotchi")
    texts = [
        ("Self Learning Tamagotchi", 'ravie', 37, "lightpink2"),
        ("You have a new tamagotchi friend!", 'lucidasanstypewriter', 16, "lightpink2"),
        ("Once you start it up, it will start learning how to care for itself!", 'lucidasanstypewriter', 16, "lightpink2"),
        ("If it does well it will get a reward", 'lucidasanstypewriter', 16, "lightpink2"),
        ("If it does poorly it will get a punishment", 'lucidasanstypewriter', 16, "lightpink2"),
        #dramatic spacing
        ("", 'lucidasanstypewriter', 16, "lightpink2"),
        ("Watch it learn and enjoy your new friend, completely independent!", 'lucidasanstypewriter', 16, "lightpink2"),
        ("Press enter/return to start", 'copperplategothic', 20, "pink")
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
    font_name = pygame.font.match_font('copperplategothic')
    font = pygame.font.Font(font_name, 30)
    hungrytama_img = pygame.transform.scale(
        pygame.image.load("hungrytama.png").convert_alpha(), (110, 140)
    )
    energytama_img = pygame.transform.scale(
        pygame.image.load("energetictama.png").convert_alpha(), (110, 140)
    )
    sleepytama_img = pygame.transform.scale(
        pygame.image.load("sleepytama.png").convert_alpha(), (110, 140)
    )
    tama_img = pygame.transform.scale(
        pygame.image.load("pinktamagotchi.png").convert_alpha(), (400, 550)
    )
    #image-state correlation
    state_images = {
        0: hungrytama_img,
        1: energytama_img,
        2: sleepytama_img
    }
    #locate images
    img_rect = hungrytama_img.get_rect(
        center=(window_size[0] // 2, window_size[1] // 2.35)
    )
    tama_rect = tama_img.get_rect(
        center=(window_size[0] // 2, window_size[1] // 2.57)
    )
    state = env.reset()
    reward = 0
    reward_total = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        #start Qlearning
        action = agent.act_and_learn(state, reward)
        next_state, reward = env.step(action)
        reward_total += reward
        #tracks matching for visuals
        if reward > 0:
            match_str = "Correct match!"
        else:
            match_str = "Wrong match!"
        window.fill("maroon4")
        #displays updating images
        window.blit(tama_img, tama_rect)
        window.blit(state_images[state], img_rect)
        state_text = font.render(
            f"State: {env.states[state]}", True, "lightpink2"
        )
        action_text = font.render(
            f"Action: {env.actions[action]}", True, "lightpink2"
        )
        reward_text = font.render(
            f"Reward: {reward_total}", True, "lightpink2"
        )
        match_text = font.render(
            match_str, True, "lightpink2"
        )
        #display updating data
        window.blit(state_text, (245, 570))
        window.blit(action_text, (245, 600))
        window.blit(reward_text, (245, 630))
        window.blit(match_text, (245, 660))
        pygame.display.flip()
        #switch to another random state
        state = next_state
        clock.tick(2)


def main():
    pygame.init()
    window = pygame.display.set_mode((700, 700))
    env = TamagotchiEnv()
    agent = QLearner(env.num_states, env.num_actions)
    start_screen(window)
    sim_screen(window, env, agent)


if __name__ == "__main__":
    main()
