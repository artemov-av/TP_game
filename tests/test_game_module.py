import pytest
import sys
sys.path.append('../')
from Game import *
from UnitFraction import *


def test_player_fraction():
    player = BritishPlayer()
    assert player.get_fraction() == UnitFraction.BRITAIN


def test_player_initial_army():
    player = BritishPlayer()
    assert player.get_army_size() == 0


def test_no_money():
    player = BritishPlayer()

    player.add_cavalry()
    player.add_cavalry()
    player.add_cavalry()

    assert player.add_cavalry() is None


def test_player_increase_army():
    game = Game()

    game.add_unit_in_map(UnitType.SWORDSMAN, 0, 0)

    assert game.british_player_.get_army_size() == 1


def test_player_change():
    game = Game()

    game.add_unit_in_map(UnitType.SWORDSMAN, 0, 0)

    assert isinstance(game.active_player_, FrenchPlayer)


def test_end_placement1():
    game = Game()

    game.add_unit_in_map(UnitType.SWORDSMAN, 0, 0)
    game.add_unit_in_map(UnitType.SWORDSMAN, 1, 1)

    game.end_placement()

    assert game.game_phase_ == GamePhase.PLACEMENT


def test_end_placement2():
    game = Game()

    game.add_unit_in_map(UnitType.SWORDSMAN, 0, 0)
    game.add_unit_in_map(UnitType.SWORDSMAN, 1, 1)

    game.end_placement()
    game.end_placement()

    assert game.game_phase_ == GamePhase.BATTLE


def test_get_rival():
    game = Game()

    assert isinstance(game.get_rival(), FrenchPlayer)


def test_attack():
    game = Game()

    game.add_unit_in_map(UnitType.SWORDSMAN, 0, 0)
    game.add_unit_in_map(UnitType.SWORDSMAN, 1, 1)

    game.end_placement()
    assert game.attack_unit(0, 0, 1, 1) is True


def test_kill():
    game = Game()

    game.add_unit_in_map(UnitType.SWORDSMAN, 0, 0)
    game.add_unit_in_map(UnitType.SWORDSMAN, 1, 1)

    game.end_placement()
    game.attack_unit(0, 0, 1, 1)
    game.end_turn()
    game.end_turn()
    game.attack_unit(0, 0, 1, 1)
    game.end_turn()
    game.end_turn()
    game.attack_unit(0, 0, 1, 1)
    game.end_turn()
    game.end_turn()
    game.attack_unit(0, 0, 1, 1)

    assert game.french_player_.get_army_size() == 0


def test_end_game():
    game = Game()

    game.add_unit_in_map(UnitType.SWORDSMAN, 0, 0)
    game.add_unit_in_map(UnitType.SWORDSMAN, 1, 1)

    game.end_placement()
    game.attack_unit(0, 0, 1, 1)
    game.end_turn()
    game.end_turn()
    game.attack_unit(0, 0, 1, 1)
    game.end_turn()
    game.end_turn()
    game.attack_unit(0, 0, 1, 1)
    game.end_turn()
    game.end_turn()
    game.attack_unit(0, 0, 1, 1)

    assert game.game_phase_ == GamePhase.END_GAME
