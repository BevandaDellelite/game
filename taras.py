import pygame
import pygame_menu
from game import game_func
pygame.init()

window = pygame.display.set_mode((500, 500))
font = pygame_menu.font.FONT_8BIT
my_theme = pygame_menu.Theme(widget_font=font,
                             background_color=(0, 0, 0),
                             widget_font_color=(255,255,255))


def start():
    game_func()






menu_rules = pygame_menu.Menu("Rules",500,500,
                        theme = my_theme)
text = "Game Rule:\n 1 Toma isn't \n niger"
menu_rules.add.label(text)

settings = pygame_menu.Menu("Rules",500,500,
                        theme = my_theme)
settings.add.label("Settings\n")
settings.add.selector("Difficulty:\n ", [("Easy",1),("Hard",2)])





menu = pygame_menu.Menu("Menu",500,500,
                        theme = my_theme)
menu.add.button("Start",start)
menu.add.button("settings",settings)
menu.add.button("Rule 34 ", menu_rules)
menu.add.button("Finish",pygame_menu.events.EXIT)

menu.mainloop(window)