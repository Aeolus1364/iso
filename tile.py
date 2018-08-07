import pygame
import res
import cfg


class Tile(pygame.sprite.Sprite):
    def __init__(self, dim):
        super().__init__()
        self.image = res.tile
        self.rect = self.image.get_rect()
        self.rect.topleft = dim

    def draw(self, surf):
        surf.blit(self.image, self.rect)


class Grid:
    def __init__(self, dim):
        self.tiles = []
        self.dim = dim

        xc = cfg.zero

        for x in range(dim[0]):
            xc[0] += 16
            xc[1] -= 8
            yc = xc[:]
            for y in range(dim[1]):
                yc[0] += 16
                yc[1] += 8
                self.tiles.append(Tile(yc))

    def draw(self, surf):
        for tile in self.tiles:
            tile.draw(surf)


class Cube(pygame.sprite.Sprite):
    def __init__(self, dim):
        super().__init__()
        self.image = res.cube
        self.rect = self.image.get_rect()
        self.rect.bottomleft = dim
        self.x = dim[0]
        self.y = dim[1]

    def draw(self, surf):
        surf.blit(self.image, self.rect)

    def update(self, *args):
        if self.x > cfg.grid[0] - 1:
            self.x = cfg.grid[0] - 1
        elif self.x < 0:
            self.x = 0

        if self.y > cfg.grid[1] -1:
            self.y = cfg.grid[1] - 1
        elif self.y < 0:
            self.y = 0

        self.rect.bottomleft = cfg.zerob[0] + self.x * 16, cfg.zerob[1] + self.x * -8
        self.rect.left += self.y * 16
        self.rect.bottom += self.y * 8

        print(self.x, self.y)

    def move(self, x):
        self.rect.x += (x * 16)
        self.rect.y -= (x * 8)


class Renderer(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def draw(self, surface):
        ordered = sorted(self.sprites(), key=lambda x: x.rect.top)
        for i in ordered:
            surface.blit(i.image, i.rect)


