with open('day_ten_in.txt') as file:
    data = [list(row.strip('\n')) for row in file.readlines()]
    data = [[int(num) for num in row] for row in data]

ROWS, COLS = len(data), len(data[0])
score = 0
score2 = 0
connected = set()


def dfs(r, c, last, origin):
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    for dr, dc in directions:
        xr, xc = r+dr, c+dc
        if 0<=xr<ROWS and 0<=xc<COLS and data[xr][xc] == last+1:
            if data[xr][xc] == 9 and (origin, (xr, xc)) not in connected:
                global score 
                score += 1
                connected.add((origin, (xr,xc)))
            else:
                dfs(xr, xc, data[xr][xc], origin)

def dfs_p2(r, c, last):
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    for dr, dc in directions:
        xr, xc = r+dr, c+dc
        if 0<=xr<ROWS and 0<=xc<COLS and data[xr][xc] == last+1:
            if data[xr][xc] == 9:
                global score2 
                score2 += 1
            else:
                dfs_p2(xr, xc, data[xr][xc])

out = 0
out2 = 0
for r in range(ROWS):
    for c in range(COLS):
        if data[r][c] == 0:
            score = 0
            score2 = 0
            dfs(r, c, 0, (r,c))
            dfs_p2(r, c, 0)
            out += score
            out2 += score2

print(out)
print(out2)

    
