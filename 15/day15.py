import collections
data = open("input15").read().strip().split("\n")
global board
board = data
global attack_power
attack_power = 3

class Unit:
	global other_team
	other_team = {"E" : "G", "G": "E"}
	def __init__(self, x, y, team):
		self.x = x
		self.y = y
		self.team = team
		self.HP = 200

	def position(self):
		print(self.x, self.y)
	
	def dist(self, other):
		return abs(self.x - other.x) + abs(self.y - other.y)

	def attack(self, units):
		min_HP = 1000
		min_ind = 0
		attack = False
		for ind, u in enumerate([ u for u in units ]):
			if self.dist(u) == 1 and self.team == other_team[u.team]:
				if u.HP < min_HP:
					attack = True
					min_HP = u.HP
					min_ind = ind
		if attack:
			if self.team == "E":
				units[min_ind].HP -= attack_power
			else:
				units[min_ind].HP -= 3


	def find_neighbour_enemies(self, units):
		neighbours = []
		for u in units:
			if self.dist(u) == 1 and self.team == other_team[u.team]:
				neighbours.append(u)
		return neighbours

	def move(self):
		self.root = ",".join([str(self.x), str(self.y), self.team])

		queue = collections.deque([self.root])
		visited = set()

		meta = dict()
		meta[self.root] = None
		while queue:
			#print(len(queue))
			subtree_root = queue.popleft()
			coords_sub = subtree_root.split(',')[:-1]
			[sub_x, sub_y] = [int(c) for c in coords_sub]
			# Condition to find the enemy
			if subtree_root[-1] == other_team[self.team]:
				board[self.y] = board[self.y][:self.x] + '.' + board[self.y][self.x+1:]
				self.x, self.y = self.__find_a_move__(subtree_root, meta)
				board[self.y] = board[self.y][:self.x] + self.team + board[self.y][self.x+1:]
				#print("ya gotta move, ya gotta move")
				return True
				
			neighbours = [(sub_x , sub_y - 1), (sub_x - 1, sub_y), 
				(sub_x + 1 , sub_y), (sub_x, sub_y + 1)] 
			available_neighbours = [(x, y, board[y][x]) for (x, y) in neighbours if board[y][x] != "#" and board[y][x] != self.team]
			for child in available_neighbours :
				child = [str(s) for s in child]
				child = ",".join(child)
				if child in visited:
					continue 
				if child not in queue:
					meta[child] = subtree_root
					queue.append(child)
			#		print(queue)
			visited.add(subtree_root)
			#print("visited:",visited)

	def __find_a_move__(self, state, meta):
		if meta[state] == self.root:
			return [self.x, self.y]
		while meta[state] is not self.root:
			state = meta[state]
		coords =  state.split(",")[:-1]
		[x, y] = [int(c) for c in coords]
		return [x, y]

	def __lt__(self, other):
		if self.y == other.y:
			return self.x < other.x
		return self.y < other.y

def print_board():
	for line in board:
		print(line)

def clear_board(units):
	for v in units:
		if v.HP <= 0:
			board[v.y] = board[v.y][:v.x] + '.' + board[v.y][v.x+1:]


# Part 1:
attack_power = 3
units = []
board = [s for s in data]
for y in range(len(board)):
	for x in range(len(board[y])):	
		if board[y][x] == 'E' or board[y][x] == 'G':
			units.append(Unit(x, y, board[y][x]))
Elves = [u for u in units if u.team == 'E']
Goblins = [u for u in units if u.team == 'G']

full_rounds = 0
while(Elves and Goblins):
	full_rounds += 1
	units.sort()
	for u in units:
		u.moved = False
	for u in units:
		clear_board(units)
		units = [u for u in units if u.HP > 0]
		if u.HP > 0:
			if not u.moved:
				u.move()
				u.moved = True
				units.sort()
				u.attack(units)
	Elves = [u for u in units if u.team == 'E']
	Goblins = [u for u in units if u.team == 'G']

print_board()
print("Number of rounds:", full_rounds)
print("Part 1:")
print(sum([u.HP for u in units]) * (full_rounds - 1))

# Part 2:
for attack_power in range(4,200):
	units = []
	board = [s for s in data]
	for y in range(len(board)):
		for x in range(len(board[y])):	
			if board[y][x] == 'E' or board[y][x] == 'G':
				units.append(Unit(x, y, board[y][x]))
	Elves = [u for u in units if u.team == 'E']
	Goblins = [u for u in units if u.team == 'G']

	num_elves = len(Elves)
	full_rounds = 0
	while(Elves and Goblins):
		full_rounds += 1
		units.sort()
		for u in units:
			u.moved = False
		for u in units:
			clear_board(units)
			units = [u for u in units if u.HP > 0]
			if u.HP > 0:
				if not u.moved:
					u.move()
					u.moved = True
					units.sort()
					u.attack(units)

		Elves = [u for u in units if u.team == 'E']
		Goblins = [u for u in units if u.team == 'G']
	if len(Elves) == num_elves:
		break

print_board()
print("Number of rounds:", full_rounds-1)
print("Attack power:", attack_power)
print("Part 2:")
print(sum([u.HP for u in units]) * (full_rounds - 1))
