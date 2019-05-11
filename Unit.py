from abc import ABC, abstractmethod
from UnitFraction import UnitFraction


class Unit(ABC):
    def __init__(self):
        self.alive_ = True
        self.fraction_ = None

    def attack(self, attacked_unit):
        if self.alive_:
            attacked_unit.receive_damage(self.damage_)

    def receive_damage(self, damage):
        if damage < self.hp_:
            self.hp_ -= damage
        else:
            self.hp_ = 0
            self.die()

    def die(self):
        self.alive_ = False

    def is_alive(self):
        return self.alive_

    def get_price(self):
        return self.price_

    def get_move_points(self):
        return self.move_points_

    def get_range(self):
        return self.range_

    def get_hp(self):
        return self.hp_

    def get_max_hp(self):
        return self.max_hp_

    def heal(self):
        if self.alive_:
            self.hp_ = min(self.max_hp_, self.hp_ + self.heal_points_)

    def get_fraction(self):
        return self.fraction_


class Swordsman(Unit, ABC):
    def __init__(self):
        super().__init__()
        self.range_ = 1
        self.move_points_ = 2
        self.heal_points_ = 5
        self.price_ = 150


class FrenchSwordsman(Swordsman):
    def __init__(self):
        super().__init__()
        self.max_hp_ = self.hp_ = 75
        self.damage_ = 25
        self.fraction_ = UnitFraction.FRANCE


class BritishSwordsman(Swordsman):
    def __init__(self):
        super().__init__()
        self.max_hp_ = self.hp_ = 75
        self.damage_ = 25
        self.fraction_ = UnitFraction.BRITAIN


class Cavalry(Unit):
    def __init__(self):
        super().__init__()
        self.range_ = 1
        self.move_points_ = 3
        self.heal_points_ = 7
        self.price_ = 300


class FrenchCavalry(Cavalry):
    def __init__(self):
        super().__init__()
        self.max_hp_ = self.hp_ = 100
        self.damage_ = 35
        self.fraction_ = UnitFraction.FRANCE


class BritishCavalry(Cavalry):
    def __init__(self):
        super().__init__()
        self.max_hp_ = self.hp_ = 90
        self.damage_ = 30
        self.fraction_ = UnitFraction.BRITAIN


class Archer(Unit):
    def __init__(self):
        super().__init__()
        self.range_ = 4
        self.move_points_ = 2
        self.heal_points_ = 8
        self.price_ = 150
        

class FrenchArcher(Archer):
    def __init__(self):
        super().__init__()
        self.max_hp_ = self.hp_ = 50
        self.damage_ = 20
        self.fraction_ = UnitFraction.FRANCE


class BritishArcher(Archer):
    def __init__(self):
        super().__init__()
        self.max_hp_ = self.hp_ = 60
        self.damage_ = 30
        self.fraction_ = UnitFraction.BRITAIN


class UnitFactory(ABC):
    @abstractmethod
    def create_swordsman(self):
        return Swordsman

    @abstractmethod
    def create_archer(self):
        return Archer

    @abstractmethod
    def create_cavalry(self):
        return Cavalry


class FrenchUnitFactory(UnitFactory):
    def create_swordsman(self):
        return FrenchSwordsman()

    def create_archer(self):
        return FrenchArcher()

    def create_cavalry(self):
        return FrenchCavalry()


class BritishUnitFactory(UnitFactory):
    def create_swordsman(self):
        return BritishSwordsman()

    def create_archer(self):
        return BritishArcher()

    def create_cavalry(self):
        return BritishCavalry()
