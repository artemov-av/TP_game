import pytest
import sys
from pathlib import Path
sys.path.append('../')
from UnitImageMapper import *
from Unit import *


def test_if_exist_british_swordsman():
    image_file = Path("img/british_swordsman.png")
    assert image_file.exists()


def test_if_exist_british_archer():
    image_file = Path("img/british_archer.png")
    assert image_file.exists()


def test_if_exist_british_horseman():
    image_file = Path("img/british_horseman.png")
    assert image_file.exists()


def test_if_exist_french_swordsman():
    image_file = Path("img/french_swordsman.png")
    assert image_file.exists()


def test_if_exist_french_archer():
    image_file = Path("img/french_archer.png")
    assert image_file.exists()


def test_if_exist_french_horseman():
    image_file = Path("img/french_horseman.png")
    assert image_file.exists()


def test_if_exist_swordsman_stroke():
    image_file = Path("img/swordsman_stroke.png")
    assert image_file.exists()


def test_if_exist_horseman_stroke():
    image_file = Path("img/horseman_stroke.png")
    assert image_file.exists()


def test_if_exist_archer_stroke():
    image_file = Path("img/archer_stroke.png")
    assert image_file.exists()


def test_get_path1():
    unit = BritishSwordsman()
    mapper = UnitImageMapper()
    assert mapper.get_path_to_stroke_image(unit) == "img/swordsman_stroke.png"


def test_get_path2():
    unit = BritishSwordsman()
    mapper = UnitImageMapper()
    assert mapper.get_path_to_image(unit) == "img/british_swordsman.png"
