#########################################
#  ___                  _       _  ___  #
# / _ \ _   _  ___  ___| |_    / |/ _ \ #
#| | | | | | |/ _ \/ __| __|   | | | | |#
#| |_| | |_| |  __/\__ \ |_    | | |_| |#
# \__\_\\__,_|\___||___/\__|___|_|\___/ #
#                         |_____|       #
#########################################
#-----------------------PART II------------------------------------------------------------------------------
raw_input = """
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
grid = [list(line) for line in raw_input.strip().split("\n")]
rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range (cols):
        if grid[r][c] == "D":
            find_dragon = (r, c)

moving_knight = [
        (2, 1), (2, -1),
        (-2, 1), (-2, -1),
        (1, 2), (1, -2),
        (-1, 2), (-1, -2)
]

def moves_dragon(places):
    spots = []
    r, c = places
    for dr, dc in moving_knight:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            spots.append((nr, nc))
    return spots

position_dragon = {find_dragon}
makan = set()

rounds = 20

for turn in range(rounds):
    new_position = set()
    for places in position_dragon:
        spots = moves_dragon(places)
        for s in spots:
            new_position.add(s)

    position_dragon = new_position

    for (dr, dc) in position_dragon:
        possible_rows = [dr - turn, dr - turn - 1]
        for sr in possible_rows:
            if 0 <= sr < rows:
                if grid[sr][dc] == "S":
                    if grid[dr][dc] != "#":
                        makan.add((sr, dc))

print(len(makan))
