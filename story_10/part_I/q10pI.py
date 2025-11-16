#########################################
#  ___                  _       _  ___  #
# / _ \ _   _  ___  ___| |_    / |/ _ \ #
#| | | | | | |/ _ \/ __| __|   | | | | |#
#| |_| | |_| |  __/\__ \ |_    | | |_| |#
# \__\_\\__,_|\___||___/\__|___|_|\___/ #
#                         |_____|       #
#########################################
# -------------------PART I-----------------------------------------
'''
quest 10 ni , dia mcm board beso, dlm board ade:
    D = dragon
    S = sheep
    . = empty
Contoh:
...SSS.......
.S......S.SS.
..S....S...S.
..........SS.
..SSSS...S...
.....SS..S..S
SS....D.S....
S.S..S..S....
....S.......S
.SSS..SS.....
.........S...
.......S....S
SS.....S..S..
cara settle dia mcm pakai iterative loop based on ape yang aku baca
(for this one , seems so so lah nk faham)
'''
from collections import deque

moves = [
    (2,1),(2,-1),(-2,1),(-2,-1),
    (1,2),(1,-2),(-1,2),(-1,-2)
]

def solve(grid, K):
    R = len(grid)
    C = len(grid[0])

    # ---find dragon = D--------
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'D':
                start = (r, c)

    visited = [[False]*C for _ in range(R)]
    q = deque()
    q.append((start[0], start[1], 0))
    visited[start[0]][start[1]] = True

    sheep = 0

    while q:
        r, c, d = q.popleft()

        if d > 0 and grid[r][c] == 'S':
            sheep += 1

        if d == K:
            continue

        for dr, dc in moves:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc, d+1))

    return sheep
'''
raw = """
...SSS.......
.S......S.SS.
..S....S...S.
..........SS.
..SSSS...S...
.....SS..S..S
SS....D.S....
S.S..S..S....
....S.......S
.SSS..SS.....
.........S...
.......S....S
SS.....S..S..
"""
'''
raw = """
S.SS.SSSSS.SSS.SSSSSS
.SS.SSSSSSSSS.SSSSS..
..SSSSSSSS.SSSSSSSSS.
SS...S.SSSSSS.SSSSSSS
.SSSS.SSS.SSSSSSS.SS.
SSS.SSSSSS...SS.SSSS.
SSS.SSS.S.SSS.SSSS...
SS.SS.S..SSSS.SSSSSSS
S.SS.S..SSSSSSSSSSSSS
S.SS.SSSSS.SS..S.....
S..SSS..SSDS.S.SSSSSS
SSSS.SSSSS.S.S.SSSS..
S...SS.SSS.SSSSSSS.SS
.S.SSSS..SSS...SSSSSS
SS.SSSSS.SSSS...S.SSS
SSS.SS..S.S...S.SS..S
..S.S.SSSSS.....S.SS.
SS.SSSSS..SSSS.SSS.SS
SS.SS.S.S.SSS.SSSSS.S
SSSSSSSSSSSSSSSSSS..S
.S.SS..S.SS..S.SS...S
"""
grid = [line for line in raw.strip().splitlines()]

# print(solve(grid, 3)) ---ni untuk contog , range 3
print(solve(grid, 4))
i
