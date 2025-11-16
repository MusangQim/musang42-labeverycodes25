#########################################
#  ___                  _       _  ___  #
# / _ \ _   _  ___  ___| |_    / |/ _ \ #
#| | | | | | |/ _ \/ __| __|   | | | | |#
#| |_| | |_| |  __/\__ \ |_    | | |_| |#
# \__\_\\__,_|\___||___/\__|___|_|\___/ #
#                         |_____|       #
#########################################
#--------------------PART II-------------------------------------
from collections import deque

grid_input = """
....S..#.S#.S..SS.S..S.S...#S.SSS###SS.S.##...S.S#..##SS.SSS#..SS..#S##..#..S..#.#..#.S.S.SSS..S...SS
S#..#S.#SS#..S#S.###S..S..S.S.#..S.SS...#.....SS..#S.SS.#S.S....##S#..SS##.SS..###...#SS##....S.....S
.SS..#.SSS..S#..#SS#SS..S#S.#SSS#S.S..##..#.SSS...#S#.S#S..SSSS.##S.S##SS.##S.##.#.S#S#.S.S.SS.#..SS#
.S.##..S.S#...SS.#.#.#SS....S.#S.S....SSSS#S#S.SS.SS#S#.#S#.SSS.#S#..#S..SSS#S#####.SS#...........S#.
#..#....SS.....##SSSS.S#...##.#S##SSS.#S...#S.#S#S..S.#.#.S.....SS.#SS#.#S##..SSS#S#SSSS.S.S...S..S..
..S...#...SS.....S..S..S.S.S.S.S.S.#S#S.#SS.S####.S..S##......S#S#.S..S##S.S#..S#SS...#SS#.S..SS..S.S
##S#S#SS..#...#.S.#.S#..SS.......##.S#S#..S.SS.#SS..#SS##S.SSS#.#..#.#.#SS.#.S..#..#..#SS.SSSSS#SS#..
SS.SSS.SS.....S..SS...S##.#.S#.#S#...##.#S.##.SS.##..SS...#S...S.S.SS..S..S.SSSS#S.#S.##SSS.SS.....S.
S#.#....S.#S..SSSSSSS#SS...#S....#S.#.#SS.##..S#.#....#.SS.S#..S###.#S..SS....S.##.....#..SSSS...S#..
.#.SSSSSSSS#S.#.S.S#....SS#..#....#S.S#S.SSSSS.S.SS#...S#S#....SSSS#S.#S#..S#.#SS..SS#.#S##S#S.##...#
S#.SSS..SSSS..#.S.#S.S.#..S.##..#.#SS.S#.....S.S..#SSS...S.S.#.S..#SS.#..S..#.#SS#..SS...S.SS..S...SS
.#...#SS.#.SS#SS...S.S.SS..S.#.#..S.#SS.SS..S......#S......S#.S#SS.S.S#SS..#.SS.#SS..SSS##.SS##S.....
S.S.S#.S.S#..SS.S.S....S.SS...SS#.S#.#..#.S...S#..#.##.SSS#SS...S.S#...S.#..#.#..#...S#..S#S.......#.
.SS.S#.SS#..S.....S.S.#..S......#.##....#...S.S#S.#S#S#...S#.S.#S..#...S#..SS.#.S#..#S#.#.##..S..S#..
.S.#S.S..SSS..#.#S.##S.##.S.S.SS.SS.#SS#SS..#.S..#SS..S.S....S.SS..##......S.SSSSSS##S..SSSS.SS##S...
.#SS.S...SS.S.........S..S.S.#SSS.#S#.S.S#SS..#S..S##S.......S#..#S##S...S#.#.#..SSS...S#.SSS.#.#SS#S
.#SSS.#.#.#S..S.S...##.SSS..#.S#.S.S..S.##SS.S..#..S.....S.S.SSS.#S.##.SS.#.S#.S#.SS#.S.#SS.#..SS#.#S
.S.###.#.S.....S##.S.##S##SSS.S##.#S......S.##...S..S..#..SS.S..#S..SS....SS.#.#S...S.#...S.S..S.S.SS
#S.S..S#S.SSS..SSS..S#.S....S...S#.#S.S..S..#S.S.##.S..SSSS#....S...#S.S.#S..##..SSS.SSS......#....S.
..#.SS..S..S..#S#S......#.#...S.S##...#S..##SS#.#SS.....S..##S.S.S.SS#...S#S.#.##....#S.SSS..S..#S.#.
#S.S...S#SS...##...S.S#...#S...S.#S.#S#.S.S....SSS##..##.##.SS.#.#S#.S...#SS...#.S.SSSS#.S...S..#S.#.
..##S.SS.##..S.##S.S.SS#SS.S.#..S##S..SS.SS.S.S...S...#S#S.SS.##...S..#S.S.##SS##SS#.#..SS##....#S#.S
#S.....##S#S#S.S..S.#..SS.##S..S..##S..S....#..#S..S.S....##.S.SS.#.#..S.##S.#.S##S#.S##S#S...SS.....
.#S..S.S.S..S.SS#S..#.#...#.S.S####SSS.SS.S....SS#SS.#.#.##.S.#..S#S.S..SS...#S.S.S####..S.#..S#.S#..
..#.#.....SS#.S.#..S##.S.##..SSS..#SSSS.......##.S##SSSS#.S.#S..S#..S.###..S###.S.SS#S..S..S.S....S..
S.##.SSS#..SS.#S.S.S#..#..S#..S##S##SS.S...S###.S#.#.S##...SS.###S.#.#.#SS.S..S..SS#....S.#....#..S#S
#S...#.#..##..SS#SS.#.S.#.#S#S##SS.S#S...##S.S#SS##S.S.SSS..SS..#..#.SS#.S....S..SS.#.#S.##SS##....#.
S.#SS#..##..#S.#.SS.#S.S..S...S.S..###..S..S##.S#S..SS.S.......#.#.#.##..SS.SS.....#..SS#.S#####.#...
S#..S..#S#.#.S.#SSS#.#.......##..S#.S#S....#.#S#.S.SS.SS#....S#...SS......##.S..SS.S##...SS.S.S.S.##S
SSSSS..S#SS...##S..S..S###.SS.#.SS.S.#...SSS..S.S#.#S.SSSS.SSS...S.S........#S.###S.SS#SSSS#S#S....#S
#..SSS#..#SS.#S...SS#.#S....#.SS#SS.S#S#S..SS#.S#.SSSSS#S.SS#S.S#.##SSS....##SS.S.SS##S..S#SSSSS#.###
S#.S.#S.SS...##.#.SSS.#.S..SS...S.##SS..S.S..S.##.S.SS#.S.SS.S#S.S..#.S...S..#..S...#.#.#..#.#..#..SS
..#..SS..S##...SS#SS.#SS#S.#.#S.SS.#S.SSS..SS.#S.S#.S...#S###S..SS..SS.##.S#....S.SS#.SS...S.#..#..S.
#S.#.#S.S..SS..#S.S#S#.....##.SSSS##S.S.S.#..##.#S.S###SS.#SSS#SS.S.#..S.#.S#.....S#.S.##S.S.#..S.SSS
##...#S..#S..#SS#SS##S...S#..S#.#.#.#..SS#.S.#.#SS.S.#S##SSS#...S#S#.S...SS..SS#..#S##..S.#S..#SS.S.#
SS.S..#S......#..S#SSSS.S.#S.S...S.S..##.##SSS...S...S#S..S.S.S.....#S......S........#.SS#.SS.S#S#SSS
..S.S..S..SSS#S.S...#S.S.#.S.#.#S..#SSS#S#...#....S.S#.S.#..#..S....#S.#SS##..#....#.SSSSS#.#.SSSSSS#
#.#S#.S#..S.....##S#.S.S..#..S#.#..SSS##S.SSS#..SS#.S...#....SSS##...S.S#SS#.#SS#S#S#.#..S.S#SS.#...S
...#S..S.SS#SS#SS.S#.S.S##S#S#.S#.S.SSS.S...#S#S##SSS.#...SSS.#.#..S.SSS..SS#.#.#.SSS#...#.SS.#S..S.S
#S####..##SSS....S.#.SS..SS...#S.SS.......#.SS..S##.S#S.SS.S#SS.S..#.S.##.S#.S#.##.S.#.#.S.....SS.#.S
SSS..S##.#.S.#..#S##..##..SS...S#S#SS.S.S..S.....#..SS.#.#.SSS.#..#.SSS#.SSS.SSS.......#.#S.S..##S#..
S...S#..SSS.S.S#S#...S.S.S.SS...SS..#.SSSS#.#.....#S.S.S#SSS..SSS#S...SS...S.##..SS#.SS..S.S#.S#.#S.S
#..S.#.#.#S#.SS.S.SSS..#.S.S.S#S..#.#.S..S....SS..S.#.S.S..#SS#.S.S#...S#.S#.....##SSSS.S#.S.SS.S#.SS
#.#.S.S.#.SS.S...SS#.SS###S..SS##..#.##SS......S#S.#SS.S#...S.#....#S...SS.S....#####.S.#.SS..S#.#SS.
SS..SS#SSS#.#S#.S.#...#SS#.#...#.S#.#S.....S#.#S.SS.#...##..#.#S..#.SS#.S.#S....#..S..##SS.#.SSSS#..S
SS.#.#S.S#..##.S#..SS.#..S....SS##S.S..S.#....#...##.S.S#....S#S.SS.S#S.S#SSSS.#...#.....S#SS.#S..#..
..SSS##.SS.S#..##SSS#.SS#S#.S..S.SS.SS..S.S.#S.S.#...#...S.S..S..#S...SS#..#..S...S.S.S.S#.....#S####
..S.#..S#.S.SS........SSSS###..#.#S...S#...####...S.S#.#SSS##..S..SSS.S#S##..#S.#..#SS..S.S.#...SS#.S
....#S...#....S..#..SS#.SS...#SSS..S.S#S#S....#.###SS...S#.S.#...SS#...S###S..#SS.S..#SSS.#S.S..#.#S.
#..S###S.#.#SSSS..#S..#SS.#.S....S.SS.S.SS..#..#SSS.S#.SS.#..SSSSS##..#.S..S#S..S#SSS..S.SS.##.SS...S
.#S#.#...S..SS...S...#S.S..SSS....#.....#S.#.SSS..DSSS.S#..#S.S.S...##.##.#.#.S.S#S....SS.S.S.S##.S.#
#SS..##..S.#S#SS.#..SS##..#...#.S..#S...###...#...S.....S#...S....#..#S.#.#..#SSS#S...##.S#SSSSS...#S
.SSS.##S###S##.#S#..SS.S..##S##SSS#.S.S.##.#..SS...S.S#.S##SSS..#.S#S.SS..SSS.SS.....#.#..#.S.SSS...S
.S#..S..S..S...SS#..S#S..S.SS..SS.#.#.#.#..SSSS.SSSS.#S.#SS.##.SS.S.S.S.S....S#S.S...#.#SS..S#..S#S.#
#S#S#..####.S.SS.#.S.......#..SS#S...S.#S##.S.#.......S..SS..SSSSS#S.#....#...S.S..S#S.S.#S#..SSS.##S
...S.S#S#SS#S.#S..####..#S..#S...S..#S.#.#S.S#S...#SS..S.SS.##......S####S......#.##S..S.S##S...SSS.#
#.SS.#S..##....S.#.SS..SSSS.S...#.....SS.S#..SS.#S###..SS#S...S..#S#.S..#.S.SS.S.S.#..S.#S..##SSS.SS.
SSS##......#SSS....#S#....###S..S#.SS.#.....S..SS..##S##.SS...#..S#.S..SSSS..S.S.S#..SSSS.#S#S..SSSS.
##.#S#S..#..S.##...#S..##.S.S.#SSS.S..S.##SS.#S#.SS..S.##.#S..SS#S.##SS.S.S#SS.S.#.S...#S..S....#S.#.
S#..SS#S#S.S.#S.#S#S.#..S#.#SS.S.##...##.#.S.SS.#SS...S.S..S...#...S.SS###.....#.SSS....SS...#..#SS..
...S.SSS.S#S..#SS.#SS#..S..#...#..SS..SSS..SSSS...S##SS.S##S.#S#...S.##..#.S..SS.#..S#...#.SS.....S.S
#S....SS..SS..S#.##SS#S#.S....SS##S##..#S..S.##......SSSSSS#.S##SS#S#.S......S.#S..S.S.SS..####SS#S.S
SS.##.#.S.S#S.SSS#..SS.#S.SS..S.S##.##...S#.S....SS.#S.##S.#..##.##...####.#.#...S..SS..SSS.#.S#..#S.
..S..S.##.S.....SSS.SSSSS.SS.S#S#.S.SS#.#####......##....S#.###.#S###..SS###SS##SS#...SS.....S.#.##S.
.#S.SSS...SSS.#S#S###...#...#.##..S.S..S...#SS#SSS.##...SS##S#SS...S...S.S.....#S####..........SS.SSS
...#S#.S.#..SS.S.#SSSSSSS..S#.S#...#...S#SSS...SSSSSS.S.S..SS.##.SSS#S.SS#.SS.#..S.S.S..#S..SS.S#....
....S..SS.#S#SSSS.#..#..#.S.##..SS.#..#.S...S#SS...#.SS...###.S.#.#SS...S.S...S.#SS..S...SS...SS..S#.
.S#.#..##..SS.S#..##SS#.S.....#.##.#.#S.SS#...SS.SS...#...S.#S....S#S#.S..S#..#SSSS#.S####.#SS##S.###
..S#SS#SSS#.#.SS..SS.....S.#..#SS.SS.#.#S.#S...S...##S#SS..S#.S..S..#.###.S.S..S.S.SSSS##...SSS#S..#.
#.S#.S....S#S.###.........SS.S#..SS.#...#...S.#S.S.#.S.#..#S#SS...SS.....S..#.S#SSS.S.SS.S#.....S#..S
S.##SS..S#..SS#S....#SS#..S##.S#.S..##S.##..#..#SS.##.SS.##..SS.##.##S##SS..S###.#.#S.S.S.S.#SSSSS#.#
...#.#SSS..S#SS.SSS#..##...S#SS...#SS.S...#S#....#S##.##.#S.#S#.....S#S.SSS##..S#S#..SS##.S.S.#S#.S#S
S.#SS..#S.#SS#...SS#.S#S.S..SS.S....S..SS..S#S.#.S.S.#.#S#..SS.S.SS#S....S....##..##..SS.S.SS#SS.##..
.S....#S#.S.S.##..SSSSSS....S.#..S#.S###.S.S.SS..#SS.S.S#..#...#S..SS#....#....SSS.SSS#.SS.###.#SS..S
S#..SS.SS..S#SSS.##S.S.SS#.SS..SSS...#.SSS#SSSS..S.#.S.#S#.#.S##...SS##..#.S.#...##S#....S...S.SS#.#.
S...#S.SS..SSS##S...#SS.#S.#S#S.....#S#.S.S....S.....S#..#S.SS..S.S##..SS...S#...#.#...S####.#SS....#
.SS.SS#.SS.##....#.SSSS#.#....#S#.S..S.#SS..###.S.#....S#.S#..S..S##.S#.##.S.##SSS.#.#.....#S.SS.#.#S
.S.#S#S.#.#..S#S#SS..SSSS#S..SS.S..##..#S.SS#.S...S...S#..S.S.#.SSSS..##....#....SS.S.##...#S..#..#.#
#S.SSS#S...S#.#SS#..S#.S.S...S.S#.S...#SS.##.S.S#.#.SS.......SS.S.SSSSS...##..S.SSS...S.SS...S.SS..##
#S.S...SS#..SS#.S##......S.S.S.S.#S.SS.#.SS#S#SSS..S.##S.S#..SSSS..#S#..S.#S.SS..S.S.#SS#.SS.#S#.S.#.
...#S.#.S.#SSS....SSSS.S.SSS.SSSS#..##SS.S.#S....S.S.#SSS..SSS.#.#...S.#.#S.SS...SS.SS.S#.SSS#S#SS#.S
SS...SS...#.##S...S...#.SS.S#.S#...S.SS##.S#S.......#SSS##.#S..#S.S##SSS.##.#S#S.S.S.S..SS#S#..S##..S
...#SS#.SSS.SS..S.....SSSSS#...S.#SS..SSS.S.S.#SSSS..S.S.S.S#SS.#S.SS.#S...S..S..#S.S.#SS..S.S..S..SS
#S..#S.SS#.S.#S.SSSSS#.##S..S.S.S.SS.S.S.SSS..#SS.S.##...SS.S..SS#S#S#S.SS#SS..S.S.S.S.SSS.S.S#S.#.S.
S..SSS..SS..#S##S..#.S.S.S..S#S......#S..S.S..#.#.SSS#SS.S.SSS#.S...#.#.S#S..#.....###..SS#...S..SSS.
.#S..S.S..S.S#S..###..##.SSSS.#SS.S...S#S.S.##...S...SS.#.S..SS.SS##S.###....SSSS.#.#S#.SS#.S#..SSSS.
S##S...S..#.#..S#S.S##SS.SS#..S.S..S.S#.#.S.SSS..##S#.#S##S#S#.##SSSS#.S.SSS#S#.SS.SS..S.SSSS...S.S.S
S.###.S.SS#..SSSSSSS#S.#S...##SSSS.#S.......#.#.S..SSS.S....S.#.SSSS##..SS..#S#S...SSS#.#...#.S.#S...
S.#..S.S#S.#.S.SS#.SS.#..S.##S.....#..S#S##S..#.S##S##.SSSS##.SS.S...#SS.SS#.#..S..SS...#.SSS..#.S#..
...#.S.#..S###S..#...#S#..SS#.##S...SSS.S.S..#..S##.#.S#.#.S.S#.#.###..#.S##S##...#.....S........#.#.
S.##.S....#...#SSS.S...S.....##S.#S.#SS#....#.S##....#..#SS#.S.#S..S#.SS..S.#...###SS...S#..#S...SSS#
....SS.###.S.#..#...##...S#S..S.#S..#S.S#.#.S..#.#SSSS#.#S.S..S.#S.#...##SSS.SS#S...#S.S.#.#SS.#S....
S.SS...S..#.#..##.S#..SS.#..#.#S...SS.#.##...SSS....S.S...S.S..S.#.#S.S.....#SS.SSS..#S..##..#SSSS#S#
...S#.S.SS.S..#.##SS..SSS.S..S#.#SS#SSSSSS.S..S...SSS.SS...#SS..#S.#..S#....SS..S....#..#.S.S##.S#.S.
..##.#S....S..#.#S..SS.#S.S..#..###..S....SSS...S.SSS#.#SSS.#SS.#.......S..S.SS#.#SS.SSS#S.#S#..#.S..
.S.SS.S.SS#S###.#S...#S#..S.S.#.S#SS....#..#S....S.SSS.S....S..S.##....S.#SS#SS....S###..#S..S#SSS##.
#.S#S.S.S.#S.#....SSS#.#..SSS.##..SS#..##S#S.#S.###.S...SSS....S.S...S##....#SS#..SS.S...S#.#S....#SS
##S..#.S#.S##..S##..#..#.#...S..#SSS..S......SSS.#.S.S...S#S..SSS....###S.SS#..#S.##.SS.#..#.S.S...S#
.SS##S..SSSS.S...SS.S..S#..S#S.....S#.#SS#S.##S.SS#..S.S.S#S...##.##S.S.S.#S...S.SSS...#S.#S#..S..S#.
#..SSSSS..S.SSS#..#.S.SS.##.......SSSSS...#.#...S#.SS.S.S#SS.SS...SSS#.SS..SS#..#.....#S.S###S#....#.
#S.S.SSSSS#S..#SS#..SS.#S.S#.#SSSS..SS.#S..S#SSS#SS...#.#.S.SSSS#S..#S#....SS...#SS..#..S..S.#S.#S.S#
"""

# Parse grid
lines = grid_input.strip().split('\n')
grid = [list(line) for line in lines]
rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

# Find dragon position
dragon_pos = None
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 'D':
            dragon_pos = (r, c)
            break
    if dragon_pos:
        break

if not dragon_pos:
    print("Dragon not found!")
else:
    # BFS to explore all possible paths
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    # State: (row, col, rounds, frozenset of eaten sheep positions)
    start_state = (dragon_pos[0], dragon_pos[1], 0, frozenset())
    queue = deque([start_state])

    # Track best result for each state
    visited = {}
    max_sheep = 0

    while queue:
        r, c, rounds, eaten_sheep = queue.popleft()

        # If we've done 20 rounds, record result
        if rounds == 20:
            max_sheep = max(max_sheep, len(eaten_sheep))
            continue

        # Try all 4 directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Check bounds
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue

            # Check if wall
            if grid[nr][nc] == '#':
                continue

            # Check if there's a sheep here
            new_eaten = eaten_sheep
            if grid[nr][nc] == 'S' and (nr, nc) not in eaten_sheep:
                new_eaten = eaten_sheep | {(nr, nc)}

            # Create new state
            new_state = (nr, nc, rounds + 1, new_eaten)
            state_key = (nr, nc, rounds + 1, new_eaten)

            # Skip if we've seen this exact state before
            if state_key in visited:
                continue

            visited[state_key] = True
            queue.append(new_state)

    print(f"Maximum sheep eaten in 20 rounds: {max_sheep}")
