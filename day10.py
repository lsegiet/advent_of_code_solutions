import re


class point:

    def __init__(self, numbers):
        self.x = numbers[0]
        self.y = numbers[1]
        self.vx = numbers[2]
        self.vy = numbers[3]

    def position(self, time=0):
        x_now = self.x + self.vx * time
        y_now = self.y + self.vy * time
        return [x_now, y_now]


def distance(p1, p2, time=0):
    pos1 = p1.position(time)
    pos2 = p2.position(time)
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])


with open("input10", "r") as f:
    input = f.readlines()
input = [line.strip() for line in input]

i = 0
points = []
for line in input:
    numbers = re.findall("-?\d+", line)
    numbers = [int(x) for x in numbers]
    points += [point(numbers)]

for t in range(10629, 10632):
    max_dist = 0
    for i in range(len(points)-1):
        for j in range(i, len(points)):
            if distance(points[i], points[j], t) > max_dist:
                max_dist = distance(points[i], points[j], t)
    print(t, max_dist)

for TIME in range(10629, 10631):
    print(TIME)
    xx = [p.position(TIME)[0] for p in points]
    yy = [p.position(TIME)[1] for p in points]
    x_max = max(xx)
    x_min = min(xx)
    y_max = max(yy)
    y_min = min(yy)
    table = list([list(['.'])*(x_max+1-x_min)]) * (y_max + 1 - y_min)
    table = [['.' for j in range(x_max+1-x_min)]
             for i in range(y_max + 1 - y_min)]
    for p in points:
        x_now, y_now = p.position(TIME)
        x_now -= x_min
        y_now -= y_min
        table[y_now][x_now] = '#'
    table = [''.join(row) for row in table]
    for line in table:
        print(line)
