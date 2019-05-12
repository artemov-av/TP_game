from collections import deque


class Tile:
	pass


class GameMap:
	def __init__(self, width, height):
		self.tile_map_ = [[Tile() for x in range(width)] for x in range(height)]
		self.unit_map_ = [[None for x in range(width)] for x in range(height)]

	def add_unit(self, unit, x, y):
		self.unit_map_[x][y] = unit

	def get_unit(self, x, y):
		return self.unit_map_[x][y]

	def can_unit_be_placed(self, x, y):
		return self.is_there_tile(x, y) and self.unit_map_[x][y] is None

	def is_there_tile(self, x, y):
		if x < 0 or y < 0 or x >= self.get_height() or y >= self.get_width():
			return False
		return self.tile_map_[x][y] is not None

	def is_tile_passable(self, x, y):
		return self.unit_map_[x][y] is None

	def remove_unit(self, x, y):
		self.unit_map_[x][y] = None

	def move_unit(self, x1, y1, x2, y2):
		self.unit_map_[x2][y2] = self.unit_map_[x1][y1]
		self.unit_map_[x1][y1] = None

	def get_width(self):
		return len(self.tile_map_[0])

	def get_height(self):
		return len(self.tile_map_)

	def adjacent_tiles(self, x, y):
		adj = []
		if self.is_there_tile(x-1, y):
			adj.append((x-1, y))
		if self.is_there_tile(x, y-1):
			adj.append((x, y-1))
		if self.is_there_tile(x, y+1):
			adj.append((x, y+1))
		if self.is_there_tile(x+1, y):
			adj.append((x+1, y))

		t = y + 1 if x % 2 == 0 else y - 1

		if self.is_there_tile(x+1, t):
			adj.append((x+1, t))
		if self.is_there_tile(x-1, t):
			adj.append((x-1, t))

		return adj

	def get_walking_path(self, x1, y1, x2, y2):
		return self.find_path(x1, y1, x2, y2, check_on_passability=True)

	def get_attacking_distance(self, x1, y1, x2, y2):
		path = self.find_path(x1, y1, x2, y2)
		return len(path) - 1 if path is not None else None

	def find_path(self, x1, y1, x2, y2, check_on_passability=False):
		path = []
		parent = [[None for x in range(self.get_width())] for x in range(self.get_height())]
		bfs_q = deque()
		bfs_q.append((x1, y1))

		while len(bfs_q) > 0:
			cur_tile = bfs_q.popleft()
			if cur_tile == (x2, y2):
				while not cur_tile == (x1, y1):
					path.append(cur_tile)
					cur_tile = parent[cur_tile[0]][cur_tile[1]]
				path.append(cur_tile)
				path.reverse()
				return path

			adj = self.adjacent_tiles(cur_tile[0], cur_tile[1])
			for tile in adj:
				if not check_on_passability or self.is_tile_passable(tile[0], tile[1]):
					if parent[tile[0]][tile[1]] is None:
						parent[tile[0]][tile[1]] = cur_tile
						bfs_q.append(tile)

		return None

