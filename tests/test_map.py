import pytest
import sys
sys.path.append('../')
from GameMap import *
from Unit import *


def test_add_unit():
    game_map = GameMap(10, 10)
    unit = BritishSwordsman()
    game_map.add_unit(unit, 5, 5)

    assert game_map.get_unit(5, 5) is unit


def test_add_place():
    game_map = GameMap(10, 10)
    unit = BritishSwordsman()
    game_map.add_unit(unit, 5, 5)

    assert game_map.can_unit_be_placed(5, 5) is not True


def test_remove_unit():
    game_map = GameMap(10, 10)
    unit = BritishSwordsman()
    game_map.add_unit(unit, 5, 5)
    game_map.remove_unit(5, 5)

    assert game_map.get_unit(5, 5) is None


def test_move_unit1():
    game_map = GameMap(10, 10)
    unit = BritishSwordsman()
    game_map.add_unit(unit, 5, 5)
    game_map.move_unit(5, 5, 6, 6)

    assert game_map.get_unit(5, 5) is None


def test_move_unit2():
    game_map = GameMap(10, 10)
    unit = BritishSwordsman()
    game_map.add_unit(unit, 5, 5)
    game_map.move_unit(5, 5, 6, 6)

    assert game_map.get_unit(6, 6) is unit


def test_tile1():
    game_map = GameMap(10, 10)
    assert game_map.is_there_tile(20, 20) is not True


def test_tile2():
    game_map = GameMap(10, 10)
    assert game_map.is_there_tile(-1, 20) is not True


def test_adj_tiles():
    game_map = GameMap(10, 10)
    adj_tiles = game_map.adjacent_tiles(0,0)
    tile1 = (0, 1)
    tile2 = (1, 0)
    tile3 = (1, 1)
    tiles = [tile1, tile2, tile3]

    assert tiles == adj_tiles


def test_passable_tile():
    game_map = GameMap(10, 10)
    unit = BritishSwordsman()
    game_map.add_unit(unit, 5, 5)

    assert game_map.is_tile_passable(5, 5) is not True


def test_no_path():
    game_map = GameMap(2, 10)
    unit1 = BritishSwordsman()
    unit2 = BritishSwordsman()
    game_map.add_unit(unit1, 0, 1)
    game_map.add_unit(unit2, 1, 1)

    assert game_map.get_walking_path(0, 0, 1, 5) is None


def test_attacking_distace():
    game_map = GameMap(10, 10)

    assert game_map.get_attacking_distance(0, 0, 2, 2) == 3
