#######################################
#  ___                  _     _  ___  #
# / _ \ _   _  ___  ___| |_  / |/ _ \ #
#| | | | | | |/ _ \/ __| __| | | (_) |#
#| |_| | |_| |  __/\__ \ |_  | |\__, |#
# \__\_\\__,_|\___||___/\__| |_|  /_/ #
#                                     #
#######################################
# ---------------------------PART I-------------------------------
import math
"""
segments = [
    [7, 7, 2],
    [12, 0, 4],
    [15, 5, 3],
    [24, 1, 6],
    [28, 5, 5],
    [40, 8, 2],
]
"""
segments = [
    [8, 5, 6],
    [13, 10, 7],
    [21, 19, 5],
    [27, 10, 7],
    [34, 17, 6],
    [43, 26, 7],
    [50, 34, 6],
    [59, 22, 6],
    [65, 28, 7],
    [74, 38, 6],
    [79, 42, 7],
    [88, 30, 7],
]

segments.sort()

flaps = 0
position = 0
height = 0

for i in range(len(segments)):
    minhr = 0
    next_pos = segments[i][0]

    for x, h, _ in segments[i:]:
        minhr = max(minhr, h - (x - next_pos))

    sprint = max(0, int(math.ceil((minhr - height + next_pos - position) / 2)))
    flaps += sprint

    height += sprint - (next_pos - position - sprint)
    position = next_pos

print(flaps)

