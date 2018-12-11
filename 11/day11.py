serial_number = 4151


def power_level(x, y):
    rackID = x + 10
    result = rackID * y
    result += serial_number
    result *= rackID
    result /= 100
    result %= 10
    result -= 5
    return result


max_pow = -100
for i in range(1, 298):
    for j in range(1, 298):
        pow = 0
        for k in range(3):
            for l in range(3):
                pow += power_level(i+k, j+l)
        if pow > max_pow:
            max_pow = pow
            max_coords = [i, j]
print(max_pow, max_coords)


max_pow = -100
table = [[{1: power_level(j+1, i+1)} for i in range(300)] for j in range(300)]
for size in range(2, 30):
    for i in range(0, 301-size):
        for j in range(0, 301-size):
            table[i][j][size] = table[i][j][size-1]
            for param in range(size-1):
                table[i][j][size] += table[i+size-1][j+param][1]
                table[i][j][size] += table[i+param][j+size-1][1]
            table[i][j][size] += table[i+size-1][j+size-1][1]
            print([size, i, j])
            if table[i][j][size] > max_pow:
                max_coords = [i+1, j+1, size]
                max_pow = table[i][j][size]

print(max_coords)
