from collections import deque, defaultdict

with open('day_twelve_in.txt') as file:
    data = [list(row.strip('\n')) for row in file.readlines()]

ROWS, COLS = len(data), len(data[0])
directions = [[0,1],[1,0],[0,-1],[-1,0]]
visited = set()

def bfs(r, c, type):
    perim_nodes = defaultdict(list)
    q = deque([(r,c)])
    visited.add((r,c))
    area = 1
    perimiter = 0
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            rr, cc = r+dr, c+dc
            if 0<=rr<ROWS and 0<=cc<COLS and data[rr][cc] == type:
                if (rr, cc) not in visited:
                    area += 1
                    visited.add((rr,cc))
                    q.append((rr,cc))
            else:
                perimiter += 1
                perim_nodes[(dr,dc)].append((rr,cc))

    sides = 0     
    for _, values in perim_nodes.items():
        seen_edges = set()
        for r, c in values:
            if (r,c) not in seen_edges:
                sides += 1
                q = deque([(r,c)])
                while q:
                    r1, c1 = q.popleft()
                    if (r1,c1) in seen_edges:
                        continue
                    else:
                        seen_edges.add((r1,c1))
                        for dr, dc in directions:
                            rr, cc = r1+dr, c1+dc
                            if (rr, cc) in values:
                                q.append((rr,cc))
    return area, perimiter, sides

out = out2 = 0
for r in range(ROWS):
    for c in range(COLS):
        if (r, c) not in visited:
            a, p, s = bfs(r, c, data[r][c])
            out += a * p
            out2 += a * s
print(out)
print(out2)
                