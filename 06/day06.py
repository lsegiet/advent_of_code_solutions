data = open("06.in").read().strip().split("\n")
data = [line.split(",") for line in data]
data = [(int(line[0]), int(line[1])) for line in data]
centers = []

def dist(point1, point2):
	return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

for x, y in data:
	centers.append((x,y))

max_x = max([x for (x, _) in centers])
min_x = min([x for (x, _) in centers])
max_y = max([y for (_, y) in centers])
min_y = min([y for (_, y) in centers])

dict_of_centers = { p : set() for p in centers }
	
# Part 1:
for x in range(min_x, max_x + 1):
	for y in range(min_y, max_y + 1):
		point = (x, y)
		closest_centers = []
		for center in dict_of_centers.keys():
			if not closest_centers or dist(point, center) == dist(point, closest_centers[0]):
				closest_centers.append(center)
			elif dist(point, center) < dist(point, closest_centers[0]) :
				closest_centers = [center]
		if len(closest_centers) == 1:	
			dict_of_centers[closest_centers[0]].add(point)
			if x in [min_x, max_x] or y in [min_y, max_y]:
				dict_of_centers[closest_centers[0]].add(True)

areas = [len(value) for value in dict_of_centers.values() if True not in value]
print(max(areas))

# Part 2:
area = 0
for x in range(min_x, max_x + 1):
	for y in range(min_y, max_y + 1):
		point = (x, y)
		distance = 0
		for center in dict_of_centers.keys():
			distance += dist(point, center)
		if distance < 10000:
			area += 1
print(area)
