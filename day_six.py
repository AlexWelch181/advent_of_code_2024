with open('day_six_in.txt') as file:
    grid = []
    for line in file.readlines():
        grid.append(list(line.strip('\n')))

def find_origin_and_direction(grid):
    for idx in range(len(dir_sym)):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == dir_sym[idx]:
                    return ((row, col), dir_val[idx])

dir_sym = ['^', '>', 'V', '<']
dir_val = [(-1,0), (0,1), (1,0), (0,-1)]
seen = set()

def right_turn(x, y):
    idx = dir_val.index((x, y))
    idx = (idx + 1) % 4
    return dir_val[idx]


def count_spaces():
    out = 1
    ROWS, COLS = len(grid), len(grid[0])
    cords, direction = find_origin_and_direction(grid)
    x, y = cords
    seen.add((x,y))
    dx, dy = direction
    while 0 <= x+dx < ROWS and 0 <= y+dy < COLS:
        if grid[x+dx][y+dy] == '#':
            dx, dy = right_turn(dx, dy)
        else:
            x, y = x+dx, y+dy
            if (x,y) not in seen:
                out += 1
                seen.add((x,y))
    return out

def is_looping(origin, direction):
    ROWS, COLS = len(grid), len(grid[0])
    x, y = origin
    dx, dy = direction
    visited = set()
    while 0 <= x+dx < ROWS and 0 <= y+dy < COLS:
        if grid[x+dx][y+dy] == '#':
            dx, dy = right_turn(dx, dy)
        else:
            x, y = x+dx, y+dy
            if (x,y,dx,dy) in visited:
                return True
            visited.add((x,y,dx,dy))
    return False


def check_loops():
    cords, direction = find_origin_and_direction(grid)
    out = 0
    availble = {(x, y) for x, y in seen if (x, y) != cords}
    for x, y in availble:
        grid[x][y] = '#'
        if is_looping(cords, direction):
            out += 1
        grid[x][y] = '.'
    return(out)

print(count_spaces())
print(check_loops())
