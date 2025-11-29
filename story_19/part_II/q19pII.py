#######################################
#  ___                  _     _  ___  #
# / _ \ _   _  ___  ___| |_  / |/ _ \ #
#| | | | | | |/ _ \/ __| __| | | (_) |#
#| |_| | |_| |  __/\__ \ |_  | |\__, |#
# \__\_\\__,_|\___||___/\__| |_|  /_/ #
#                                     #
#######################################
# ---------------------------PART II-------------------------------
import math
import functools

segments = [
    [19,1,16],
    [33,1,8],
    [33,37,9],
    [58,1,14],
    [85,1,16],
    [85,52,6],
    [100,1,11],
    [114,11,12],
    [114,39,6],
    [137,1,8],
    [150,5,16],
    [150,30,3],
    [167,1,8],
    [193,24,12],
    [193,43,5],
    [204,33,9],
    [229,54,16],
    [229,77,4],
    [253,22,11],
    [278,51,10],
    [278,79,9],
    [288,56,12],
    [316,86,10],
    [316,108,9],
    [343,54,12],
    [359,66,12],
    [359,87,8],
    [384,93,13],
    [410,121,11],
    [410,149,9],
    [423,103,10],
    [436,112,19],
    [436,143,4],
    [458,137,13],
    [471,152,8],
    [471,173,6],
    [491,124,15],
    [518,151,15],
    [518,173,5],
    [547,114,12],
    [574,87,16],
    [574,175,6],
    [599,114,13],
    [613,129,15],
    [613,162,9],
    [632,149,14],
    [646,130,14],
    [646,185,3],
    [665,110,13],
    [688,132,12],
    [688,165,3],
    [716,159,18],
    [732,179,10],
    [732,193,5],
    [753,150,16],
    [774,173,12],
    [774,203,6],
    [793,189,15],
    [809,210,10],
    [809,227,3],
    [824,191,11],
    [848,217,12],
    [848,246,3],
    [862,228,9],
    [874,241,9],
    [874,262,7],
    [901,212,10],
    [922,184,15],
    [922,259,9],
    [950,214,11],
    [973,184,10],
    [973,263,3],
    [991,200,13],
    [1011,225,11],
    [1011,241,5],
    [1027,236,17],
    [1050,211,6],
    [1050,286,3],
    [1061,199,8],
    [1087,221,12],
    [1087,247,8],
    [1102,202,9],
    [1126,173,16],
    [1126,240,7],
    [1154,208,7],
    [1181,177,12],
    [1181,247,3],
    [1193,165,9],
    [1221,133,18],
    [1221,219,7],
    [1249,165,11],
    [1276,187,14],
    [1276,219,6],
    [1288,201,14],
    [1305,179,13],
    [1305,250,9],
    [1326,159,11],
    [1353,128,17],
    [1353,204,9],
    [1378,8,107]
]

segments_dict = {}
for x, h, o in segments:
    if x not in segments_dict:
        segments_dict[x] = []
    segments_dict[x].append((h,o))

@functools.cache
def solve(position, height):
    future_pos = sorted(pos for pos in segments_dict if pos > position)
    if len(future_pos) == 0:
        return 0
    next_pos, *future_pos = future_pos

    optimal = float("inf")
    global_minhr = 0
    global_maxhr = float("inf")

    for pos in future_pos:
        lh, _ = min(segments_dict[pos])
        hh, ho = max(segments_dict[pos])
        global_minhr = max(global_minhr, lh - (pos - next_pos))
        global_maxhr = min(global_maxhr, hh + ho - 1 + (pos - next_pos))

    for H, O in segments_dict[next_pos]:
        minhr = max(global_minhr, H)
        maxhr = min(global_maxhr, H + O - 1)

        minsprint = max(0, int(math.ceil((minhr - height + next_pos - position) / 2)))
        maxsprint = max(0, (maxhr - height + next_pos - position) // 2)

        for sprint in range(minsprint, maxsprint + 1):
            newheight = height + sprint - (next_pos - position - sprint)
            optimal = min(optimal, sprint + solve(next_pos, newheight))

    return optimal

print(solve(0, 0))

