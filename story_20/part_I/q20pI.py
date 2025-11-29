###########################################
#  ___                  _     ____   ___  #
# / _ \ _   _  ___  ___| |_  |___ \ / _ \ #
#| | | | | | |/ _ \/ __| __|   __) | | | |#
#| |_| | |_| |  __/\__ \ |_   / __/| |_| |#
# \__\_\\__,_|\___||___/\__| |_____|\___/ #
#                                         #
###########################################
# ---------------------------PART I------------------------------

my_input = """
#T##TTTTTT#TT#TT#TTT#TTT#
.TTT#TT#TT#TT#TTTTTTTTTT.
..TTTTTTTTTTTTTTTTTT###..
...TTT###TTTTTTT#TTTTT...
....#TTTTTTTT#TTTT#TT....
.....TTTTTT#TTTTTT#T.....
......TTT#TT#TTTT#T......
.......##T#T#T#TTT.......
........##TTTTT##........
.........#TTTTTT.........
..........##TTT..........
...........TTT...........
............#............
""".strip().splitlines()

grid = [line.strip(".") for line in my_input]

pairs = 0

for row in grid:
    for x, y in zip(row, row[1:]):
        if x == y == "T":
            pairs += 1

for r, s in zip(grid, grid[1:]):
    for x, y in zip(r[1::2], s[0::2]):
        if x == y == "T":
            pairs += 1

print(pairs)

