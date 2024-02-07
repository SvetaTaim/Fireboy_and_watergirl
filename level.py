import pygame
import pytmx

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 640, 640
FPS = 15
MAPS_DIR = "maps"
TILE_SIZE = 32


class Fireboy_and_Watergirl:
    def __init__(self, filename, free_tiles, finish_tile):
        self.map = pytmx.load_pygame(f"{MAPS_DIR}/{filename}")
        self.height = self.map.height
        self.width = self.map.width
        self.tile_size = self.map.tilewidth
        self.free_tiles = free_tiles
        self.finish_tile = finish_tile

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                image = self.map.get_tile_image(x, y, 0)
                screen.blit(image, (x * self.tile_size, y * self.tile_size))

    def get_tile_id(self, position):
        return self.map.tiledgidmap[self.map.get_tile_gid(*position, 0)]


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    fb_wg = Fireboy_and_Watergirl("map1.tmx", [10, 46], 20)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        fb_wg.render(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
