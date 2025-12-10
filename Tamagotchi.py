import pygame

##use tarakotchi sprites

def start_screen(window):
    window_size = window.get_size()
    pygame.display.set_caption("Self Learning Tamagotchi")
    text_story1 = "You have a new tamagotchi friend!"
    text_story2 = "Once you start it up, it will start learning how to care for itself!"
    text_story3 = "If it does well it will get a reward"
    text_story4 = "If it does poorly it will get a punishment"
    text_story5 = "Watch as it learns and starts to care for itself!"
    text_story6 = "Enjoy your new friend, completely independent!"
    font_name1 = pygame.font.match_font('ravie')
    font_name2 = pygame.font.match_font('lucidasanstypewriter')
    font1 = pygame.font.Font(font_name1, 37)
    font2 = pygame.font.Font(font_name2, 16)
    text_title_font = font1.render("Self Learning Tamagotchi", True, "lightpink2")
    text1_story = font2.render(text_story1, True, "lightpink2")
    text2_story = font2.render(text_story2, True, "lightpink2")
    text3_story = font2.render(text_story3, True, "lightpink2")
    text4_story = font2.render(text_story4, True, "lightpink2")
    text5_story = font2.render(text_story5, True, "lightpink2")
    text6_story = font2.render(text_story6, True, "lightpink2")
    text_title_spot = text_title_font.get_rect(center=(window_size[0] // 2, window_size[1] // 8))
    text1_story_spot = text1_story.get_rect(center=(window_size[0] // 2, window_size[1] // 4.5))
    text2_story_spot = text2_story.get_rect(center=(window_size[0] // 2, window_size[1] // 3.8))
    text3_story_spot = text3_story.get_rect(center=(window_size[0] // 2, window_size[1] // 3.25))
    text4_story_spot = text4_story.get_rect(center=(window_size[0] // 2, window_size[1] // 2.85))
    text5_story_spot = text5_story.get_rect(center=(window_size[0] // 2, window_size[1] // 2.55))
    text6_story_spot = text6_story.get_rect(center=(window_size[0] // 2, window_size[1] // 2.3))
    window.fill("maroon4")
    window.blit(text_title_font, text_title_spot)
    window.blit(text1_story, text1_story_spot)
    window.blit(text2_story, text2_story_spot)
    window.blit(text3_story, text3_story_spot)
    window.blit(text4_story, text4_story_spot)
    window.blit(text5_story, text5_story_spot)
    window.blit(text6_story, text6_story_spot)
    print(pygame.font.get_fonts())
    pygame.display.flip()
    go = True
    while go:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    go = False



def main():
    pygame.init()
    surface = pygame.display.set_mode((700, 700))
    start_screen(surface)
    pygame.quit()

if __name__ == "__main__":
    main()