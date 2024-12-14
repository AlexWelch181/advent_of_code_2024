import re
import numpy as np
import matplotlib.pyplot as plt

XSIZE = 101
YSIZE = 103
# 100 seconds for part 1, 10,000 seconds for part 2
SECONDS = 10000
grid  = [[0 for i in range(XSIZE)] for j in range(YSIZE)]
robots = []
variance = []
minvar =  float('inf')
minvaridx = -1

def print_grid(grid):
    mod_grid = [[str(num) if num != 0 else '.' for num in row] for row in grid]
    for row in mod_grid:
        print(''.join(row))

def calculate_variance(array):
    array = np.array(array)
    total_points = np.sum(array)
    x_coords, y_coords = np.indices(array.shape)
    mean_x = np.sum(x_coords * array) / total_points
    mean_y = np.sum(y_coords * array) / total_points
    variance = np.sum(array * ((x_coords - mean_x)**2 + (y_coords - mean_y)**2)) / total_points
    return variance

topleft = topright = botleft = botright = 0
with open('day_fourteen_in.txt') as file:
    for line in file.readlines():
        robots.append([int(num) for num in re.findall(r'-*\b\d+\b', line)])


for i in range(SECONDS):
    for r in range(len(robots)):
        x, y, dx, dy = robots[r]
        grid[y][x] = grid[y][x]-1 if grid[y][x] > 0 else 0
        x =  (x+dx) % XSIZE
        y = (y+dy) % YSIZE
        robots[r] = [x,y,dx,dy]
        grid[y][x] += 1
    var = calculate_variance(grid)
    if var < minvar:
        minvar = var
        minvaridx = i
    variance.append(var)

for y in range(YSIZE):
    for x in range(XSIZE):
        if grid[y][x] > 0:
            val = grid[y][x]
            halfx, halfy = XSIZE // 2, YSIZE // 2
            if x < halfx and y < halfy:
                topleft += val
            elif x > halfx and y < halfy:
                topright += val
            elif x < halfx and y > halfy:
                botleft += val
            elif x > halfx and y > halfy:
                botright += val

print(topleft * topright * botleft * botright)
print(minvaridx+1)

plt.plot(range(1, len(variance)+1), variance, marker='o', linestyle='-', color='b', label='Data')

plt.xlabel('Seconds')
plt.ylabel('Variance')
plt.legend()
plt.show()