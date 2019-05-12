from Game import GamePhase
from UnitCreatingController import UnitCreatingController
from BattleController import BattleController


class ControllerManager:
	def __init__(self):
		self.game_model_ = None
		self.game_view_ = None
		self.game_scene_ = None
		self.placement_controller_ = UnitCreatingController()
		self.battle_controller_ = BattleController()
		self.controller_ = None

	def set_game_model(self, game_model):
		self.game_model_ = game_model
		self.game_model_.game_phase_changed.connect(self.change_controller)

	def set_game_view(self, game_view):
		self.game_view_ = game_view
		self.game_scene_ = self.game_view_.get_scene()

	def change_controller(self):
		if self.game_model_ is None or self.game_view_ is None:
			return

		self.disconnect_controller()

		game_phase = self.game_model_.get_phase()
		if game_phase == GamePhase.PLACEMENT:
			self.controller_ = self.placement_controller_
		elif game_phase == GamePhase.BATTLE:
			self.controller_ = self.battle_controller_

		self.connect_controller()

	def disconnect_controller(self):
		if self.controller_ is None:
			return

		if type(self.controller_) == UnitCreatingController:
			if self.game_view_ is not None:
				self.game_view_.unit_changed.disconnect(self.controller_.changed_unit_type)
				self.game_view_.end_placement_clicked.disconnect(self.controller_.end_placement_button_clicked)

			if self.game_scene_ is not None:
				self.game_scene_.tile_clicked.disconnect(self.controller_.tile_clicked)

	def connect_game_and_view(self):
		self.game_model_.unit_added_in_map.connect(self.game_view_.update_after_adding_unit)
		self.game_model_.turn_changed.connect(self.game_view_.update_after_turn_change)
		self.game_model_.game_phase_changed.connect(self.game_view_.change_phase)

		self.game_model_.unit_added_in_map.connect(self.game_scene_.add_unit_item)
		self.game_model_.unit_died.connect(self.game_scene_.remove_unit_item)
		self.game_model_.unit_updated.connect(self.game_scene_.update_unit_item)
		self.game_model_.unit_moved.connect(self.game_scene_.move_unit_item)
		self.game_model_.unit_clicked.connect(self.game_scene_.update_unit)
		self.game_model_.unit_unclicked.connect(self.game_scene_.update_last_unit)

	def connect_controller(self):
		if type(self.controller_) == UnitCreatingController:			
			self.game_view_.unit_changed.connect(self.controller_.changed_unit_type)
			self.game_view_.end_placement_clicked.connect(self.controller_.end_placement_button_clicked)
			self.game_scene_.tile_clicked.connect(self.controller_.tile_clicked)			
		elif type(self.controller_) == BattleController:
			self.game_view_.end_turn_clicked.connect(self.controller_.end_turn_button_clicked)
			self.game_scene_.tile_clicked.connect(self.controller_.tile_clicked)
