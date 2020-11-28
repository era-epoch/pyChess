import pygame
from typing import List, Optional
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN,
                           QUIT, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION,
                           MOUSEWHEEL)
import random


class Piece(pygame.sprite.Sprite):
    """A piece for playing a game on a chess GameBoard.

    === Attributes ===
    position:
        A tuple referring to the row and column where the piece currently is
        (x, y).
    allowed_moves:
        A list of tuples containing all possible positions this piece could
        move to.
    name:
        A unique id for the piece in the game.
    """
    position: tuple
    allowed_moves: List[tuple]
    name: str
    player: str
    surf: pygame.Surface
    rect: pygame.Rect
    colour: tuple

    def __init__(self, start: tuple, name: str, player: str, size: int,
                 colour: tuple) -> None:
        """Initialize a piece at given start location, belonging to <player>,
        with unique id <name>, on a board with TILE_SIZE <size>."""
        super(Piece, self).__init__()
        self.position = start
        self.allowed_moves = []
        self.name = name
        self.player = player
        self.colour = colour
        self.surf = pygame.Surface((size - (size//5), size - (size//5)))
        self.surf.fill(self.colour)
        self.rect = self.surf.get_rect()

    def get_allowed_moves(self) -> List[tuple]:
        raise NotImplementedError


class Tile(pygame.sprite.Sprite):
    """A single tile on a board.

    == Attributes ==

    colour: the colour of the tile
    _occupied: whether or not there is a piece on the tile
    _position: the grid position of the tile in the board (x, y)
    piece: the piece occupying the tile

    """
    colour: tuple
    _occupied: bool
    position: tuple
    piece: Optional[Piece]
    size: int

    def __init__(self, colour: tuple, pos: tuple, size: int):
        super(Tile, self).__init__()
        self.colour = colour
        self.position = pos
        self.size = size
        self.piece = None
        self._occupied = False
        self.surf = pygame.Surface((size, size))
        self.surf.fill(self.colour)
        self.rect = self.surf.get_rect(
            topleft=(
                size * pos[0],
                size * pos[1]
            )
        )

    def occupy(self, piece: Piece):
        self.piece = piece
        self._occupied = True
        piece.rect = piece.surf.get_rect(
            topleft=(
                self.size//10,
                self.size//10
            )
        )
        piece.position = self.position
        self.surf.blit(piece.surf, piece.rect)

    def vacate(self):
        self.piece = None
        self._occupied = False
        self.surf.fill(self.colour)


class Board:
    """A board for playing chess."""
    tiles: List[Tile]
    map: dict

    def __init__(self, tiles: List[Tile]):
        self.tiles = tiles
        self.map = {}
        for til in tiles:
            self.map[til.position] = til

    def get_tile_at(self, position: tuple):
        xpos, ypos = position[0]//TILE_SIZE, position[1]//TILE_SIZE
        if xpos < 0 or ypos < 0 or xpos > SCREEN_WIDTH or ypos > SCREEN_HEIGHT:
            return None
        if (xpos, ypos) in self.map.keys():
            return self.map[(xpos, ypos)]
        return None


pygame.init()

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
BOARD_SIZE = 8
PLAYING_SPACE = min(SCREEN_HEIGHT, SCREEN_WIDTH)
TILE_SIZE = PLAYING_SPACE//BOARD_SIZE

# temps
TEMP_COLOUR_ONE = (255, 0, 0)
TEMP_COLOUR_TWO = (0, 255, 0)
TEMP_COLOUR_THREE = (0, 0, 255)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

tile_list = []


# Set up Tiles, alternating black and white
for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        if i % 2 == 0:
            if j % 2 == 0:
                new_tile = Tile((255, 255, 255), (i, j), TILE_SIZE)
            else:
                new_tile = Tile((0, 0, 0), (i, j), TILE_SIZE)
        else:
            if j % 2 == 0:
                new_tile = Tile((0, 0, 0), (i, j), TILE_SIZE)

            else:
                new_tile = Tile((255, 255, 255), (i, j), TILE_SIZE)
        tile_list.append(new_tile)

board = Board(tile_list)

# Populate board appropriately with pieces
for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        if j == 0 or j == 1:
            new_piece = Piece((0, 0), str(i) + str(j), 'black', TILE_SIZE,
                              TEMP_COLOUR_ONE)
            board.map[(i, j)].occupy(new_piece)
        elif j == BOARD_SIZE - 1 or j == BOARD_SIZE - 2:
            new_piece = Piece((0, 0), str(i) + str(j), 'white', TILE_SIZE,
                              TEMP_COLOUR_TWO)
            board.map[(i, j)].occupy(new_piece)

previous_hover_tile = None
moving = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            hover_tile = board.get_tile_at(pos)

            if hover_tile is not None:
                if hover_tile != previous_hover_tile:
                    if previous_hover_tile is not None:
                        previous_hover_tile.surf = saved_surf_state
                    saved_surf_state = hover_tile.surf.copy()
                    hover_tile.surf.fill((128, 128, 128))
                    previous_hover_tile = hover_tile

        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            selected_tile = board.get_tile_at(pos)
            if selected_tile is not None:
                if moving:
                    selected_tile.surf.fill(TEMP_COLOUR_TWO)
                    moving = False
                else:
                    selected_tile.surf.fill(TEMP_COLOUR_THREE)
                    moving = True

    screen.fill((0, 0, 0))

    for tile in board.tiles:
        screen.blit(tile.surf, tile.rect)

    pygame.display.flip()

pygame.quit()
