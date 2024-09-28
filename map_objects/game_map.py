""" Holds 2d array of tiles and methods for setting up and interacting """
from map_objects.tile import Tile


class GameMap:
    """Class for handling the map and tiles"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        """Function initializing the tiles in the map"""
        tiles = [[Tile(False) for y in range(self.height)] for x in range(self.width)]

        tiles[30][22].blocked = True
        tiles[30][22].block_sight = True
        tiles[31][22].blocked = True
        tiles[31][22].block_sight = True
        tiles[32][22].blocked = True
        tiles[32][22].block_sight = True

        return tiles

    def is_blocked(self, x, y):
        """ Function to determine if a tile is blocked """
        if self.tiles[x][y].blocked:
            return True

        return False
