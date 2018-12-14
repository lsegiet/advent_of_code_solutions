data = open("input13").read().split("\n")

board_elements = ["+", r"\ "[0], "/"]

directions = ["<","v",">","^"]
directions_flipped1 = ["v","<","^",">"] # for /
directions_flipped2 = ["^",">","v","<"] # for \
flip = { "/" : { before : after for before, after in zip(directions,directions_flipped1)},
 	r"\ "[0] : { before : after for before, after in zip(directions,directions_flipped2)}}
class Cart:
	def __init__(self, x, y, direction):
		self.x = x
		self.y = y
		self.direction = direction
		self.move_index = 0
	
	def move(self):
		x = self.x
		y = self.y
		if self.direction == ">":
			self.x += 1
		elif self.direction == "<":
			self.x -= 1
		elif self.direction == "v":
			self.y += 1
		else:
			self.y -= 1
		if data[self.y][self.x] in board_elements:
			if data[self.y][self.x] == "+":
				self.__turn__()
			elif data[self.y][self.x] in board_elements:
				self.direction = flip[data[self.y][self.x]][self.direction]
			elif  data[self.y][self.x] in board_elements == " ":
				print("error", self.x, self.y)
		return str(max(self.x, x)) + "," + str(min(self.x, x)) + "," + str(max(self.y, y)) + "," + str(min(self.y, y))

	def __turn__(self):
		for i, d in enumerate(directions):
			if d == self.direction:
				ind = i
		if self.move_index % 3 == 1: #straight
			self.direction = directions[ind]
		elif self.move_index % 3 == 0: # left
			self.direction = directions[(ind + 1) % 4]
		else:	# right
			self.direction = directions[(ind - 1) % 4]
		self.move_index = (self.move_index + 1) % 3

	def __lt__(self, other):
		if self.y == other.y:
			return self.x < other.x
		return self.y < other.y

def check_if_crash(Cart1, Cart2):
	if Cart1.x == Cart2.x and Cart1.y == Cart2.y:
		return True
	return False
def dist(Cart1, Cart2):
	return abs(Cart1.x - Cart2.x) + abs(Cart1.y - Cart2.y)

# Load board:
carts_start = []
for y in range(len(data)):
	for x in range(len(data[y])):
		if data[y][x] in directions:
			carts_start.append((x,y,data[y][x]))
			if data[y][x] in ["<", ">"]:
				data[y] = data[y][:x] + '-' + data[y][x+1:]
			else:	
				data[y] = data[y][:x] + '|' + data[y][x+1:]
# Part 1:
carts = [Cart(x, y, direction) for x, y, direction in carts_start]
crashed = False
while (not crashed):
	temp_board = list(data)
	carts.sort()
	for i, cart in enumerate(carts):
		cart.move()
		for j in range(len(carts)):
			if i != j and  dist(carts[i],carts[j]) == 0:
				crash_position = str(carts[i].x) + "," + str(carts[j].y)
				crashed = True

print(crash_position)
# Part 2:
carts = [Cart(x, y, direction) for x, y, direction in carts_start]
while len(carts) > 1:
	live_carts = [True for ind in range(len(carts))]
	carts.sort()
	for i, cart in enumerate(carts):
		cart.move()
		for j in range(len(carts)):
			if i != j and  dist(carts[i],carts[j]) == 0:
				live_carts[i] = False
				live_carts[j] = False
	carts = [cart for cart, live in zip(carts,live_carts) if live]
print(str(carts[0].x) + "," + str(carts[0].y))

