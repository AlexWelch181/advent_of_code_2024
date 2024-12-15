from collections import deque

with open('day_fifteen_in.txt') as file:
    grid, instructions = file.read().split('\n\n')
    grid = [list(row) for row in grid.split('\n')]
    instructions = list(instructions.replace('\n', ''))

ROWS, COLS = len(grid), len(grid[0])
rpos, cpos = None, None

def pprint(grid):
    for row in grid:
        print(''.join(row))
    print()

def transform_grid(grid):
    trans_grid = []
    for r in range(ROWS):
        row = []
        for c in range(COLS):
            if grid[r][c] == '#':
                row.append('#')
                row.append('#')
            elif grid[r][c] == 'O':
                row.append('[')
                row.append(']')
            elif grid[r][c] == '.':
                row.append('.')
                row.append('.')
            elif grid[r][c] == '@':
                row.append('@')
                row.append('.')
        trans_grid.append(row)
    return trans_grid

grid2 = transform_grid(grid)
#pprint(grid2)
ROWS2, COLS2 = len(grid2), len(grid2[0])

def find_robot(grid):
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == '@':
                return r, c

direction = {'^':(-1,0), '>':(0,1), 'v':(1,0), '<':(0,-1)}

rpos, cpos = find_robot(grid)
for i in range(len(instructions)):
    dr, dc = direction[instructions[i]]
    xr, xc = rpos+dr, cpos+dc
    if grid[xr][xc] == '#':
        continue
    elif grid[xr][xc] == 'O':
        br, bc = xr+dr, xc+dc
        while grid[br][bc] == 'O':
            br, bc = br+dr, bc+dc
        if grid[br][bc] == '#':
            continue
        elif grid[br][bc] == '.':
            grid[xr][xc], grid[br][bc] = grid[br][bc], grid[xr][xc]
    grid[rpos][cpos], grid[xr][xc] = grid[xr][xc], grid[rpos][cpos]
    rpos, cpos = xr, xc

r, c = find_robot(grid2)
for instr in instructions:
    dr,dc = direction[instr]
    xr, xc = r+dr, c+dc
    if grid2[xr][xc] == '#':
        continue
    if grid2[xr][xc] == '.':
        r, c = xr, xc
    else:
        q = deque([(r,c)])
        seen = set()
        wall = False
        while q:
            rr, cc = q.popleft()
            if (rr, cc) in seen:
                continue
            seen.add((rr, cc))
            nr, nc = rr+dr, cc+dc
            if grid2[nr][nc] == '#':
                wall = True
                break
            elif grid2[nr][nc] == '[':
                q.append((nr,nc))
                q.append((nr,nc+1))
            elif grid2[nr][nc] == ']':
                q.append((nr,nc))
                q.append((nr,nc-1))
        if wall:
            continue
        while seen:
            for rr, cc in sorted(seen):
                nr, nc = rr+dr, cc+dc
                if (nr, nc) not in seen:
                    grid2[nr][nc], grid2[rr][cc] = grid2[rr][cc], grid2[nr][nc]
                    seen.remove((rr,cc))
        r, c = r+dr, c+dc

#pprint(grid2)


out = out2 = 0
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == 'O':
            out += r*100+c

for r in range(ROWS2):
    for c in range(COLS2):
        if grid2[r][c] == '[':
            out2 += r*100+c

print(out)
print(out2)

    
