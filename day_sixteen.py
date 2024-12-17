import heapq
from collections import defaultdict, deque

with open('day_sixteen_in.txt') as file:
    grid = [list(row.strip('\n')) for row in file.readlines()]

def pprint(grid):
    for row in grid:
        print(''.join(row))
    print()

directions = [[-1,0], [0,1], [1,0], [0,-1]]
ROWS, COLS = len(grid), len(grid[0])

def find(grid, target):
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == target:
                return r,c

r,c = find(grid, 'S')
heap = [(0,r,c,1, [(r,c)])]
heapq.heapify(heap)
lowestcost = dict()
end_states = set()
backtrack = defaultdict(set)
def find_lowestcost_path():
    best_cost = float('inf')
    while heap:
        cost, r, c, d, path = heapq.heappop(heap)
        for dr, dc in directions:
            rr, cc = r+dr, c+dc
            if grid[rr][cc] in '.E' and (rr,cc) not in set(path):
                ncost = cost +1
                nd = d
                if grid[rr][cc] == 'E':
                    if ncost > best_cost: break
                    best_cost = ncost
                    end_states.add((rr,cc,dr,dc))
                if directions[(d+1)%4] == [dr, dc]:
                    ncost += 1000
                    nd = (d+1)%4
                elif directions[(d-1)%4] == [dr, dc]:
                    ncost += 1000
                    nd = (d-1)%4
                lowest = lowestcost.get((rr,cc,dr,dc), float('inf'))
                if ncost > lowest: continue
                if ncost < lowest:
                    backtrack[(rr,cc,dr,dc)] = set()
                    lowestcost[(rr,cc,dr,dc)] = ncost
                odr, odc = directions[d]
                backtrack[(rr,cc,dr,dc)].add((r,c,odr,odc))
                heapq.heappush(heap, (ncost, rr, cc, nd, path + [(rr,cc)]))
    
    states = deque(end_states)
    seen = set(end_states)
    while states:
        key = states.popleft()
        for last in backtrack.get(key, []):
            if last in seen: continue
            seen.add(last)
            states.append(last)


    return best_cost, len({(r,c) for r,c,_,_ in seen})

print(find_lowestcost_path())