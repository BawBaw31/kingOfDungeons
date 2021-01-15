import pygame
from GameManager import GameManager
from Thing.Player import Player
from Room import Room

pygame.init()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("King of Dungeons")
pygame.mouse.set_cursor(*pygame.cursors.diamond)

player = Player(window)
actual_room = Room(window)
run = True

game_manager = GameManager(window, player, actual_room)

while run:
    pygame.time.Clock()

    game_manager.state_manager()

    run = game_manager.run

pygame.quit()
