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

lines = grid_input.strip().split('\n')
grid = [list(line) for line in lines]
rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0

# Find dragon
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
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Track positions reachable at each round
    current_positions = {dragon_pos}
    total_sheep = 0
    
    for round_num in range(1, 21):
        next_positions = set()
        sheep_this_round = set()
        
        for r, c in current_positions:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                    next_positions.add((nr, nc))
                    
                    # If there's a sheep here, count it
                    if grid[nr][nc] == 'S':
                        sheep_this_round.add((nr, nc))
        
        round_sheep_count = len(sheep_this_round)
        total_sheep += round_sheep_count
        print(f"Round {round_num}: {round_sheep_count} sheep, Total so far: {total_sheep}")
        
        current_positions = next_positions
    
    print(f"\nFinal answer: {total_sheep}")
