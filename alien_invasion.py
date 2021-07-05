import sys
import pygame
from settings import Settings
define run_game():
  pygame.init()
  ai_settings = Settings()
  screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
  pygame.display.set_caption("Alien Invasion")
  bg_color = (230, 230, 230)

  while True:
    for event in pygame.event.get():
      if event.type == pygme.QUIT:
        sys.exit()
    screen.fill(ai_settings.bg_clor)
    pygame.display.flip()   
run_game()
  