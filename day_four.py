with open('day_four_in.txt') as file:
    arr = [list(row.strip('\n')) for row in file.readlines()]

def brute_force(arr):
    target = 'MAS'
    out = 0
    ROWS, COLS = len(arr), len(arr[0])
    for r in range(ROWS):
        for c in range(COLS):
            if arr[r][c] == 'X':
                for dr, dc in [[0,1], [1,0], [-1,0], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]]:
                    xr, xc = r+dr, c+dc
                    idx = 0
                    while  0 <= xr < ROWS and 0 <= xc < COLS and arr[xr][xc] == target[idx]:
                        if idx == 2:
                            out += 1  
                            break
                        xr, xc = xr+dr, xc+dc
                        idx += 1
                    
    return out

def cross_mas(arr):
    out = 0
    ROWS, COLS = len(arr)-1, len(arr[0])-1
    for r in range(1, ROWS):
        for c in range(1, COLS):
            if arr[r][c] == 'A':
                count = 0
                for dr, dc, tr, tc in [[1,1,-1,-1], [1,-1,-1,1]]:
                    xr, xc = r+dr, c+dc
                    oxr, oxc = r+tr, c+tc
                    if (arr[xr][xc], arr[oxr][oxc]) == ('M', 'S') or (arr[xr][xc], arr[oxr][oxc]) == ('S', 'M'):
                        count += 1
                        if count == 2:
                            out += 1
    return out


print(brute_force(arr))
print(cross_mas(arr))