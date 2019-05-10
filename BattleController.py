from Game import Game
from abc import ABC


class ClickState(ABC):
	def __init__(self, context, prev_state):
		self.context_ = context
		self.prev_state_ = prev_state

	def process_click(self, x, y):
		pass


class RootClickState(ClickState):
	def __init__(self, context, prev_state):
		super().__init__(context, prev_state)

	def process_click(self, x, y):
		unit = Game().get_unit_by_coords(x, y)
		if unit is not None and type(unit.get_fraction()) == type(Game().get_active_player().get_fraction()):
			context.change_state(FriendUnitClickState(self.context_, self))
		else:
			pass


class FriendUnitClickState(ClickState):
	def __init__(self, context, prev_state):
		super().__init__(context, prev_state)

	def process_click(self, x, y):
		pass


class EnemyUnitClickState(ClickState):
	def __init__(self, context, prev_state):
		super().__init__(context, prev_state)

	def process_click(self, x, y):
		pass


class EmptyTileClickState(ClickState):
	def __init__(self, context, prev_state):
		super().__init__(context, prev_state)

	def process_click(self, x, y):
		pass


class BattleController:
	def __init__(self):
		self.clicked_tiles_list_ = []
		self.click_state_ = RootClickState(self, None)
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
		pass
