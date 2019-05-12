import pytest
import sys
sys.path.append('../')
from Unit import *
from UnitFraction import UnitFraction


def test_fraction_fr():
    test_unit_1 = FrenchSwordsman()

    assert test_unit_1.get_fraction() == UnitFraction.FRANCE


def test_fraction_br():
    test_unit_2 = BritishCavalry()

    assert test_unit_2.get_fraction() == UnitFraction.BRITAIN


def test_attack():
    test_unit_1 = FrenchSwordsman()
    test_unit_2 = BritishCavalry()
    test_unit_1.attack(test_unit_2)
    assert test_unit_2.hp_ == test_unit_2.max_hp_ - test_unit_1.damage_


def test_kill():
    test_unit_1 = FrenchSwordsman()
    test_unit_2 = BritishCavalry()
    for i in range(1, 5):
        test_unit_1.attack(test_unit_2)

    assert test_unit_2.is_alive() is False


def test_default_prices_sword():
    test_unit_1 = FrenchSwordsman()
    assert test_unit_1.price_ == 150


def test_default_prices_cavalry():
    test_unit_2 = BritishCavalry()
    assert test_unit_2.price_ == 300


def test_default_prices_archer():
    test_unit_3 = FrenchArcher()
    assert test_unit_3.price_ == 150
