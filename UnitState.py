class TurnUnitsState:
    def __init__(self, game_map):
        self.game_map_ = game_map
        self.attacked_ = [[None for x in range(game_map.get_width())] for x in range(game_map.get_height())]
        self.move_points_spent_ = [[None for x in range(game_map.get_width())] for x in range(game_map.get_height())]
        self.refresh()

    def refresh(self):
        for x in range(self.game_map_.get_height()):
            for y in range(self.game_map_.get_width()):
                unit = self.game_map_.get_unit(x, y)
                if unit is not None:
                    self.attacked_[x][y] = False
                    self.move_points_spent_[x][y] = 0

    def update_attack(self, x1, y1, x2, y2):
        if not self.attacked_[x1][y1]:
            distance = self.game_map_.get_attacking_distance(x1, y1, x2, y2)
            if distance <= self.game_map_.get_unit(x1, y1).get_range():
                self.attacked_[x1][y1] = True
                return True
        return False

    def update_move_points(self, x1, y1, x2, y2):
        path = self.game_map_.get_walking_path(x1, y1, x2, y2)
        if path is None:
            return False
        distance = len(path) - 1
        if self.move_points_spent_[x1][y1] + distance <= self.game_map_.get_unit(x1, y1).get_move_points():
            self.attacked_[x1][y1], self.attacked_[x2][y2] = self.attacked_[x2][y2], self.attacked_[x1][y1]
            self.move_points_spent_[x1][y1], self.move_points_spent_[x2][y2] \
                = self.move_points_spent_[x2][y2], self.move_points_spent_[x1][y1]
            self.move_points_spent_[x2][y2] += distance
            return True
        return False

    def remove_unit(self, x, y):
        self.attacked_[x][y] = self.move_points_spent_[x][y] = None
