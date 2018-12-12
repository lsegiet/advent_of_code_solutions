import operator
from datetime import datetime
with open("input04") as f:
    data = f.readlines()


class WatchRecord:
    def __init__(self, line):
        year = int(line[1:5])
        month = int(line[6:8])
        day = int(line[9:11])
        hour = int(line[12:14])
        minute = int(line[15:17])

        self.timestamp = datetime(year, month, day, hour, minute)
        action = line[19:]
        if action[0] != "w" and action[0] != "f":
            self.action = int(action[7:].split()[0])
        else:
            self.action = action[:5]

    def __lt__(self, other):
        return self.timestamp < other.timestamp


class ElfRecords:
    def __init__(self, id):
        self.id = id
        self.total_sleep = 0
        self.sleep_minutes = [0 for i in range(60)]

    def record(self, sleep_time, awake_time):
        for i in range(sleep_time.minute, awake_time.minute):
            self.sleep_minutes[i] += 1

    def __total_sleep__(self):
        return sum(self.sleep_minutes)

# For Part 1:
    def __lt__(self, other):
        return sum(self.sleep_minutes) < sum(other.sleep_minutes)

# For Part 2:
    def maximum(self):
        return max(self.sleep_minutes)


records = []
for line in data:
    records.append(WatchRecord(line))
records.sort()

elves = {}
for record in records:
    if type(record.action) is int:
        current_elf = record.action
        if current_elf not in elves.keys():
            elves[current_elf] = ElfRecords(current_elf)
    elif record.action[0] == "f":
        current_sleep = record.timestamp
    elif record.action[0] == "w":
        current_awake = record.timestamp
        elves[current_elf].record(current_sleep, current_awake)
elves = [elf for elf in elves.values()]

# Part 1:
elves.sort()
minutes = elves[-1].sleep_minutes
print(elves[-1].id * minutes.index(max(minutes)))

# Part 2:
elves.sort(key=operator.methodcaller('maximum'))
minutes = elves[-1].sleep_minutes
print(elves[-1].id * minutes.index(max(minutes)))
