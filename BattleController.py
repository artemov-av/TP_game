from Game import Game
from abc import ABC


class ClickState(ABC):
	def __init__(self, context, clicked_tiles_list):
		self.context_ = context
		self.clicked_tiles_list_ = clicked_tiles_list

	def process_click(self):
		pass


class RootClickState(ClickState):
	def __init__(self, context, clicked_tiles_list):
		super().__init__(context, clicked_tiles_list)

	def process_click(self):
		x, y = self.clicked_tiles_list_[-1][0], self.clicked_tiles_list_[-1][1]
		unit = Game().get_unit_by_coords(x, y)
		if unit is not None and type(unit.get_fraction()) == type(Game().get_active_player().get_fraction()):
			self.context_.change_click_state(FriendUnitClickState(self.context_, self.clicked_tiles_list_))
		else:
			self.context_.change_click_state(RootClickState(self.context_, self.clicked_tiles_list_))


class FriendUnitClickState(ClickState):
	def __init__(self, context, clicked_tiles_list):
		super().__init__(context, clicked_tiles_list)

	def process_click(self):
		x1, y1 = self.clicked_tiles_list_[-1][0], self.clicked_tiles_list_[-1][1]
		x2, y2 = self.clicked_tiles_list_[-2][0], self.clicked_tiles_list_[-2][1]

		unit = Game().get_unit_by_coords(x1, y1)
		if unit is None:
			if Game().move_unit(x2, y2, x1, y1):
				self.context_.change_click_state(RootClickState(self.context_, self.clicked_tiles_list_))
			else:
				del self.clicked_tiles_list_[-1]
		elif type(unit.get_fraction()) == type(Game().get_active_player().get_fraction()):
			self.context_.change_click_state(FriendUnitClickState(self.context_, self.clicked_tiles_list_))
		else:
			if Game().attack_unit(x2, y2, x1, y1):
				self.context_.change_click_state(RootClickState(self.context_, self.clicked_tiles_list_))
			else:
				del self.clicked_tiles_list_[-1]


class BattleController:
	def __init__(self):
		self.clicked_tiles_list_ = []
		self.click_state_ = RootClickState(self, self.clicked_tiles_list_)
		self.click_states_list_ = [self.click_state_]

	def change_click_state(self, state):
		self.click_state_ = state
		if type(state) == RootClickState:
			del self.clicked_tiles_list_[:]
			del self.click_states_list_[:]
		self.click_states_list_.append(state)

	def tile_clicked(self, x, y):
		self.clicked_tiles_list_.append((x, y))
		self.click_state_.process_click()

	def end_turn_button_clicked(self):
		Game().end_turn()
