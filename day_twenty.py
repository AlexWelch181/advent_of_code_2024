
from collections import deque, defaultdict

grid = [list(d) for d in open('day_twenty_in.txt').read().split('\n')]

ROWS, COLS = len(grid), len(grid[0])

for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == 'S':
            sr, sc = r, c


q = deque([(sr,sc,0)])
path = {(sr,sc):0}
while q:
    r, c, steps= q.popleft()
    for rr, cc in [(r-1,c),(r,c+1),(r+1,c),(r,c-1)]:
        if 0<=rr<ROWS and 0<=cc<COLS:
            if grid[rr][cc] == '#' or (rr,cc) in path: continue
            path[(rr,cc)] = path[(r,c)]+1
            q.append((rr,cc,steps+1))

def get_num_cheats(diff, radius):
    count = 0
    for r in range(ROWS):
        for c in range(COLS):
            if (r,c) not in path: continue
            for radi in range(2, radius+1):
                for dr in range(radi+1):
                    dc = radi - dr
                    for nr, nc in {(r+dr,c+dc),(r+dr,c-dc),(r-dr,c+dc),(r-dr,c-dc)}:
                        if 0<=nr<ROWS and 0<=nc<COLS:
                            if (nr,nc) not in path: continue
                            if path[(r,c)] - path[(nr,nc)] >= diff + radi: count += 1
    return count

print(get_num_cheats(100, 2))
print(get_num_cheats(100, 20))
