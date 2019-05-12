import pytest
import sys
sys.path.append('../')
from UnitState import *
from GameMap import *
from Unit import *


def test_remove_unit():
    game_map = GameMap(10, 10)
    unit1 = BritishSwordsman()
    game_map.add_unit(unit1, 0, 1)

    turn_units_state = TurnUnitsState(game_map)
    turn_units_state.remove_unit(0, 1)

    assert turn_units_state.attacked_[0][1] is None


def test_move_points1():
    game_map = GameMap(10, 10)
    unit1 = BritishSwordsman()
    game_map.add_unit(unit1, 0, 1)

    turn_units_state = TurnUnitsState(game_map)

    assert turn_units_state.update_move_points(0, 1, 9, 9) is False


def test_move_points2():
    game_map = GameMap(10, 10)
    unit1 = BritishSwordsman()
    game_map.add_unit(unit1, 0, 1)

    turn_units_state = TurnUnitsState(game_map)

    assert turn_units_state.update_move_points(0, 1, 0, 2) is True


def test_move_points3():
    game_map = GameMap(10, 10)
    unit1 = BritishSwordsman()
    game_map.add_unit(unit1, 0, 1)

    turn_units_state = TurnUnitsState(game_map)

    turn_units_state.update_move_points(0, 1, 0, 2)

    assert turn_units_state.move_points_spent_[0][2] == 1


def test_move_points4():
    game_map = GameMap(10, 10)
    unit1 = BritishSwordsman()
    game_map.add_unit(unit1, 0, 1)

    turn_units_state = TurnUnitsState(game_map)

    turn_units_state.update_move_points(0, 1, 0, 2)

    assert turn_units_state.move_points_spent_[0][1] is None


def test_refresh():
    game_map = GameMap(10, 10)
    unit1 = BritishSwordsman()
    game_map.add_unit(unit1, 0, 1)

    turn_units_state = TurnUnitsState(game_map)

    turn_units_state.update_move_points(0, 1, 0, 2)
    game_map.move_unit(0, 1, 0, 2)
    turn_units_state.refresh()

    assert turn_units_state.move_points_spent_[0][2] is 0
