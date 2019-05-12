import pytest
import sys
sys.path.append('../')
from UnitCreatingController import *


def test_initial_type():
    controller = UnitCreatingController()
    assert controller.chosen_unit_type_ == UnitType.SWORDSMAN


def test_type_change():
    controller = UnitCreatingController()
    controller.changed_unit_type(UnitType.CAVALRY)
    assert controller.chosen_unit_type_ == UnitType.CAVALRY


def test_tile_clicked():
    controller = UnitCreatingController()
    controller.changed_unit_type(UnitType.CAVALRY)
    controller.tile_clicked(1, 1)

    assert controller.chosen_unit_type_ == UnitType.SWORDSMAN
