from collections import deque

cords = []

with open('day_eighteen_in.txt') as file:
    for line in file.readlines():
        x, y = line.strip('\n').split(',')
        cords.append((int(x),int(y)))

i = 1024
grid = [['#' if (x,y) in cords[:i] else '.' for x in range(71)] for y in range(71)]

ROWS, COLS = len(grid), len(grid[0])
seen = set()
finalPath = []
def bfs():
    q = deque([(0,0,0, [(0,0)])])
    while q:
        s, r, c, path = q.popleft()
        for dr, dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            rr, cc = r+dr, c+dc
            if 0<=rr<ROWS and 0<=cc<COLS and grid[rr][cc] != '#' and (rr,cc) not in seen:
                if (rr,cc) == (ROWS-1, COLS-1):
                    global finalPath 
                    finalPath = path
                    return s+1
                seen.add((rr,cc))
                q.append((s+1, rr, cc, path+[(rr,cc)]))
    return None

print(bfs())

for v in range(i, len(cords)):
    x, y = cords[v]
    grid[y][x] = '#'
    if (y, x) in finalPath:
        seen = set()
        finalPath = []
        if bfs() is None:
            print('{0},{1}'.format(x,y))
            break
