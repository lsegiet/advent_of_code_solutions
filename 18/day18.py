filename = "18.in"

Open = "."
Trees = "|"
Lumberyard = "#"


class Landscape:

    def __init__(self, filename):
        self.data = open(filename).readlines()
        self.data = [[letter for letter in line.strip()] for line in self.data]

        additional_line = ["n" for _ in self.data[0]]
        self.data = [additional_line] + self.data + [additional_line]
        self.data = [["n"] + line + ["n"] for line in self.data]
        self.x_length = len(self.data)
        self.y_length = len(self.data[0])


    def show(self):
        self.content(show = True)

    def content(self, show = False):
        board = ""
        for i, line in enumerate(self.data):
            if i >= 1 and i <= len(self.data) - 2:
                board += "".join(line[1:-1])
                if show:
                    print("".join(line[1:-1]))
        return board


    def count_type(self, content_type):
        count = 0
        for line in self.data:
            for i in line:
                if i == content_type:
                    count += 1
        return count
       

    def count_neighbours(self, content, x, y):
        count = 0
        for i in range(x-1,x+2):
            for j in range(y-1, y+2):
                if i != x or j != y :
                    if self.data[i][j] == content:
                        count += 1
        return count

    def turn_trees(self, x, y):
        if self.data[x][y] == Open:
            if self.count_neighbours(Trees, x, y) >= 3:
                return True
        return False

    def turn_lumberyard(self, x, y):
        if self.data[x][y] == Trees:
            if self.count_neighbours(Lumberyard, x, y) >= 3:
                return True
        return False
 
    def turn_open(self, x, y):
        if self.data[x][y] == Lumberyard:
            if self.count_neighbours(Lumberyard, x, y) < 1 or self.count_neighbours(Trees, x, y) < 1:
                return True
        return False               


    def update(self):
        new_data = [[i for i in line] for line in self.data]
        for i in range(1,self.x_length):
            for j in range(1,self.y_length):
                if self.turn_trees(i, j):
                    new_data[i][j] = Trees
                if self.turn_lumberyard(i, j):
                    new_data[i][j] = Lumberyard
                if self.turn_open(i, j):
                    new_data[i][j] = Open
        self.data = new_data

    def resource_value(self):
        return self.count_type(Lumberyard) * landscape.count_type(Trees)


# Part 1:
landscape = Landscape(filename)
for i in range(10):
    landscape.update()
print("After 10 minutes:")
print(landscape.count_type(Lumberyard) * landscape.count_type(Trees))


# Part 2:
landscape = Landscape(filename)

landscapes_dict = {}
landscapes_array = []
counter = 0
while landscape.content() not in landscapes_dict.keys():
    content = landscape.content()
    landscapes_dict[content] = counter
    landscapes_array.append(landscape.resource_value())

    landscape.update()
    counter += 1

starts_repeating = landscapes_dict[landscape.content()]
repeating_length = len(landscapes_array) - starts_repeating

print("After 1000000000 minutes:")
print(landscapes_array[starts_repeating + (1000000000 - starts_repeating) % repeating_length])


