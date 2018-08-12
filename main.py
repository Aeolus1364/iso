import pygame
import tile
import cfg

pygame.init()
cfg.init()


class Main:
    def __init__(self):
        self.surf = pygame.display.set_mode((400, 400))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("ISO")
        self.fps = 30

        self.running = True

        self.test = tile.Grid(cfg.grid)
        self.cube = tile.Cube((2, 0))
        self.cube2 = tile.Cube((1, 1))
        self.group = tile.Renderer()
        self.group.add(self.cube, self.cube2)

        for i in range(cfg.grid[0]):
            for j in range(cfg.grid[1]):
                self.group.add(tile.Cube((i, j)))

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.cube.x += 1
                    if event.key == pygame.K_LEFT:
                        self.cube.x -= 1
                    if event.key == pygame.K_UP:
                        self.cube.y -= 1
                    if event.key == pygame.K_DOWN:
                        self.cube.y += 1

            # self.cube.update()
            # self.cube2.update()
            self.group.update()

            self.surf.fill((255, 255, 255))
            self.test.draw(self.surf)
            # self.cube.draw(self.surf)
            self.group.draw(self.surf)
            pygame.display.update()

            self.clock.tick(self.fps)


main = Main()
main.loop()