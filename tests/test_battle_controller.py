import pytest
import sys
sys.path.append('../')
from BattleController import *


def test_initial_state1():
    controller = BattleController()
    assert isinstance(controller.click_state_, RootClickState)


def test_initial_state2():
    controller = BattleController()
    assert len(controller.clicked_tiles_list_) == 0
