from PyQt5.QtWidgets import QLabel, QGroupBox, QRadioButton, QPushButton, QVBoxLayout, QWidget
from Game import UnitType


class PlayerPanel(QWidget):
    def __init__(self, player):
        super().__init__()
        self.player_ = player
        self.setFixedWidth(200)


class UnitCreatingPanel(PlayerPanel):
    def __init__(self, player):
        super().__init__(player)
        layout = QVBoxLayout()
        self.add_labels(layout)
        self.add_creating_tools(layout)
        layout.addStretch()
        self.setLayout(layout)

    def add_labels(self, layout):
        self.player_lbl_ = QLabel(str(self.player_))
        self.money_lbl_ = QLabel(str(self.player_.get_money()) + " gold")
        layout.addWidget(self.player_lbl_)
        layout.addWidget(self.money_lbl_)

    def add_creating_tools(self, layout):
        self.swordsman_radio_ = QRadioButton("Swordsman")
        self.archer_radio_ = QRadioButton("Archer")
        self.cavalry_radio_ = QRadioButton("Cavalry")
        self.swordsman_radio_.setChecked(True)

        self.creating_tools_group_ = QGroupBox("Create unit:")
        group_layout = QVBoxLayout()
        group_layout.addWidget(self.swordsman_radio_)
        group_layout.addWidget(self.archer_radio_)
        group_layout.addWidget(self.cavalry_radio_)
        self.creating_tools_group_.setLayout(group_layout)

        self.end_placement_button_ = QPushButton("End placement")

        layout.addWidget(self.creating_tools_group_)
        layout.addWidget(self.end_placement_button_)

    def update_after_adding_unit(self):
        self.money_lbl_.setText(str(self.player_.get_money()) + " gold")
        self.swordsman_radio_.setChecked(True)

    def connect_radios(self, signal):
        signal.emit(UnitType.SWORDSMAN)
        self.swordsman_radio_.clicked.connect(lambda f: signal.emit(UnitType.SWORDSMAN))
        self.archer_radio_.clicked.connect(lambda f: signal.emit(UnitType.ARCHER))
        self.cavalry_radio_.clicked.connect(lambda f: signal.emit(UnitType.CAVALRY))

    def connect_end_placement_button(self, signal):
        self.end_placement_button_.clicked.connect(lambda f: signal.emit())


class BattlePanel(PlayerPanel):
    def __init__(self, player):
        super().__init__(player)
        layout = QVBoxLayout()
        self.add_label(layout)
        self.add_buttons(layout)
        layout.addStretch()
        self.setLayout(layout)

    def add_label(self, layout):
        self.player_lbl_ = QLabel(str(self.player_))
        layout.addWidget(self.player_lbl_)

    def add_buttons(self, layout):
        self.end_turn_button_ = QPushButton("End turn")
        layout.addWidget(self.end_turn_button_)

    def connect_end_turn_button(self, signal):
        self.end_turn_button_.clicked.connect(lambda f: signal.emit())
